# 🧠 AI Agent (Google Gemini + Python)

This project is a command-line AI agent capable of performing actions like reading, writing, and executing Python files using Google's Gemini API. This is a simple project to learn a bit about AI agents.

## 🚀 Features

* 🔍 List files in a directory
* 📖 Read file contents (limit: 10,000 characters)
* 🐍 Execute a Python file
* ✏️ Write or overwrite a text file
* 🤖 Intelligent function calling via Gemini

## 🛠️ Technologies

* Python 3
* [Google Generative AI (Gemini)](https://ai.google.dev/)
* Modules: `subprocess`, `os`, `dotenv`

## 📦 Installation

1. Clone the repo
2. Create a `.env` file with:

   ```env
   GEMINI_API_KEY=your_google_key
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

```bash
python3 main.py "Read the file calculator.py"
```

Optional: add `--verbose` to display token usage and full response.

## 📁 Security

The agent is sandboxed to a working directory to prevent unauthorized system access.
