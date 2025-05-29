# LangGraph Agent

This project demonstrates a conversational agent built with LangGraph that uses Ollama for local LLM inference and can interact with tools.

## Prerequisites

1.  **Python**: Make sure you have Python 3.8+ installed.
2.  **Ollama**: Install Ollama from [https://ollama.com/] and ensure it is running.
3.  **Git**: Required for cloning the repository.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/xinjkeee/python_test
    cd python_test
    ```

2.  **Create and activate a virtual environment:**

    *   On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    *   On Windows (Command Prompt or PowerShell):
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Pull the Ollama model:**
    The application is configured to use the `qwen3:1.7b` model. Pull it using Ollama:
    ```bash
    ollama pull qwen3:1.7b
    ```

**If Ollama is not running, try to close if from tray and use ```ollama serve```**

## Running the Application

Once Ollama is running and the model is downloaded, you can start the LangGraph development server:

```bash
langgraph dev
```

`langgraph dev` provides a UI, use that to interact. 