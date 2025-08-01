# LLM RAG Bot Setup Instructions

Hey there! Welcome to my LLM RAG Bot project! 🎉 I’ve put together two versions of this Retrieval-Augmented Generation (RAG) chatbot:
- **Local Version**: Runs using Ollama models right on your laptop ( it works!).
- **API Version**: Meant to use Hugging Face API models, but it’s not working yet (more on that below).

The `docs` folder is the heart of both versions, holding your PDF or PPTX files for the bot to dig into. Let’s get the local version up and running—here’s how! The API version needs some work, which I couldn’t crack in time, but it’s there.

## How to Run the Local Version

This version uses Ollama to power things locally, so it’s super handy if you’ve got it set up. Here’s a step-by-step guide to get you going:

### Prerequisites
- **Python 3.8 or Higher**: Grab it from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" when installing on Windows.
- **Ollama**: Download it from [ollama.com](https://ollama.com/download) and get it running. You’ll need these models:
  - Embeddings: `mxbai-embed-large`
  - LLM: `dolphin-mistral:7b`
  - Fire up Ollama and pull the models with:
    1. ollama pull mxbai-embed-large
    2. ollama pull dolphin-mistral:7b
Keep Ollama running in the background while using the bot.

### Steps
- **Download and Extract**:
- Snag the zip file from the Google Drive link shared by me (Mayank).
- Unzip it somewhere handy, like `C:\Users\YourName\RAG API` on Windows or `~/RAG API` on macOS/Linux.

- **Set Up the `docs` Folder**:
- Make a `docs` folder inside the unzipped directory if it’s not there already.
- Drop your PDF or PPTX files in there—I’ve included a sample, `Neural_Dust_Solo_Project_Mayank_Dhapodkar (1).pdf`, to get you started.

- **Virtual Environment (Optional but Nice)**:
- Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and hop into the folder: cd path\to\your\folder
- Example: `cd C:\Users\YourName\RAG API`
- Create a virtual environment:python -m venv venv
- Activate it:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`
- You’ll see `(venv)` in your terminal—cool, you’re set!

- **Install Dependencies**:
- Install the packages with:pip install -r requirements.txt
- The `requirements.txt` covers both versions, but for now, the local one is what matters.

- **Run the Local Version**:
- Use the script `ragbot(local llm).py`:python ragbot(local llm).py
- 
- You should see:
📂 Loading documents...
✅ Loaded X documents.
✂️ Splitting into chunks...
🔍 Creating vector store...
🤖 Starting chatbot with Dolphin-Mistral...
❓ Ask your question (or type 'exit'):
- Ask something about your docs (like "What is Neural Dust?") and hit Enter. Type `exit` to stop.

#### Quick Look at Local Run
Check out my LinkedIn post where I showed this working: [https://www.linkedin.com/posts/mayank3969_ai-langchain-ollama-activity-7354602505487499264-9b-W?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEtFTnwBqlwxnNwXN8O3k4kR-PvLYqKUgUo](https://www.linkedin.com/posts/mayank3969_ai-langchain-ollama-activity-7354602505487499264-9b-W?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEtFTnwBqlwxnNwXN8O3k4kR-PvLYqKUgUo)

#### Notes
- Make sure Ollama is up and running with the right models before starting.
- The bot uses `dolphin-mistral:7b` for answers and `mxbai-embed-large` for embeddings.
- If it hiccups, double-check Ollama and your `docs` files.

## API Version (Not Working Yet)

The `rag.py` script was my shot at using the Hugging Face API with models like `sentence-transformers/all-MiniLM-L6-v2` for embeddings and `microsoft/DialoGPT-medium` for the LLM. Sadly, I hit a wall and couldn’t get it to work despite giving it my all. It’s included for reference if you’re feeling adventurous and want to debug it:
- You’d need a Hugging Face API token in a `.env` file (check `.env.example`).
- Tweak the `HuggingFaceEndpointEmbeddings` and `ChatHuggingFace` setups.

For now, stick with the local version. I might revisit this later if I figure it out!

## Common Files and Folders

- **`docs/`**: Where your document magic happens—add your PDFs or PPTXs here. The sample file is a starting point.
- **`requirements.txt`**: Lists all dependencies for both versions. Install everything, but only the local setup is active now.
- **`.env.example`**: A template for the API version’s token. Copy to `.env` and add your token if you tackle the API version.

## Additional Info

- **LinkedIn Post**: I posted about the local version running smoothly. Take a peek: [https://www.linkedin.com/posts/mayank3969_ai-langchain-ollama-activity-7354602505487499264-9b-W?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEtFTnwBqlwxnNwXN8O3k4kR-PvLYqKUgUo](https://www.linkedin.com/posts/mayank3969_ai-langchain-ollama-activity-7354602505487499264-9b-W?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEtFTnwBqlwxnNwXN8O3k4kR-PvLYqKUgUo).
- **GitHub Link**: My GitHub repo has the local version for now, but it’s pretty bare. Check it out: [https://github.com/Mayank3969/rag](https://github.com/Mayank3969/rag). I’ll update it as I go!

## Troubleshooting

- **Ollama Issues**: If it won’t start, confirm Ollama is running and models are pulled.
- **Missing Packages**: Run `pip install -r requirements.txt` again and look for errors.
- **PDF Problems**: Make sure `poppler` and `tesseract` are installed and in your PATH (Windows users, see links in prerequisites).
- **API Version Glitches**: If you try the API, ensure a valid token and internet connection.

## Acknowledgments

I poured a lot of effort into this! The local version is up and running, and I shared my journey on LinkedIn. If you’ve got tips for the API version or want to collab, I’m all ears. Thanks for checking it out.
