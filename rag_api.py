import os
from langchain_community.document_loaders import UnstructuredPDFLoader, UnstructuredPowerPointLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_huggingface import ChatHuggingFace

from dotenv import load_dotenv
load_dotenv()

if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = input("Enter your Hugging Face API token: ")

#1 Load all documents
def load_docs(folder_path):
    
    docs = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            print(f"📄 Loading PDF: {filename}")
            loader = UnstructuredPDFLoader(full_path)
        elif filename.endswith(".pptx"):
            print(f"📊 Loading PPTX: {filename}")
            loader = UnstructuredPowerPointLoader(full_path)
        else:
            continue
        docs.extend(loader.load())
    return docs

#Split docs
def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

#Create or load vector store
def create_or_load_vectorstore(chunks):
    embeddings = HuggingFaceEndpointEmbeddings(model_name="minishlab/potion-base-8M")
    db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="chroma_db")
    return db

#Create the QA chain with Retriever and Dolphin-Mistral
def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = ChatHuggingFace(model="Qwen/Qwen2.5-14B-Instruct")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return qa

#Main Interactive Loop
def main():
    folder_path = "docs"
    print("📂 Loading documents...")
    docs = load_docs(folder_path)
    print(f"✅ Loaded {len(docs)} documents.")

    print("✂️ Splitting into chunks...")
    chunks = split_docs(docs)

    print("🔍 Creating vector store...")
    vectorstore = create_or_load_vectorstore(chunks)

    print("🤖 Starting chatbot with Dolphin-Mistral...")
    qa_chain = create_qa_chain(vectorstore)

    while True:
        question = input("\n❓ Ask your question (or type 'exit'): ")
        if question.lower() == 'exit':
            break
        try:
            response = qa_chain.invoke({"query": question})
            print("💬 Answer:", response['result'])
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()
