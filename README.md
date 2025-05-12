# MayAgentAI 🤖

MayAgentAI is an innovative and intelligent assistant designed to help you interact with your documents effortlessly. Powered by cutting-edge AI technologies, it allows you to upload files, process them, and ask questions to extract meaningful insights. Whether you're a developer, researcher, or business professional, MayAgentAI is here to make your life easier.

## Features 🚀

- **Document Embedding**: Upload your files and convert them into embeddings for efficient processing.
- **AI-Powered Q&A**: Ask questions about your documents and get accurate, context-aware answers.
- **Streamlit Interface**: A user-friendly web interface for seamless interaction.
- **FastAPI Backend**: A robust and scalable API for handling requests.
- **Chroma Vector Store**: Efficient storage and retrieval of document embeddings.
- **Customizable**: Easily extend and adapt the project to your needs.
- **Upcoming Features**: Development is underway to support reading and processing PDFs, audio, video, images ecc.

## How It Works 🛠️

1. **Upload Your Files**: Use the Streamlit interface to upload your documents.
2. **Process Files**: The backend processes your files, creating embeddings using advanced AI models.
3. **Ask Questions**: Interact with your documents by asking questions and receiving precise answers.

## Technologies Used 🧠

- **[LangChain](https://github.com/hwchase17/langchain)**: For building AI-powered applications.
- **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast (high-performance) web framework for building APIs.
- **[Streamlit](https://streamlit.io/)**: For creating an intuitive and interactive user interface.
- **[Chroma](https://www.trychroma.com/)**: A vector database for efficient document retrieval.
- **[Ollama](https://ollama.com/)**: State-of-the-art AI models for embeddings and language understanding.

## Installation & Setup ⚙️

1. Clone the repository:

    ```bash
    git clone https://github.com/g-restante/may-agent.git
    cd may-agent
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the backend:

    ```bash
    uvicorn src.may_agent.main:app --reload
    ```

4. Run the Streamlit interface:

    ```bash
    streamlit run src/may_agent/app.py
    ```

## Access the app

- Backend API: <http://localhost:8000>
- Streamlit Interface: <http://localhost:8501>

## License 📜

This project is licensed under the Apache License 2.0.

## 🌟 Why Choose MayAgentAI?

MayAgentAI is more than just a tool—it's your personal assistant for document management and knowledge extraction. With its powerful AI capabilities and easy-to-use interface, you'll save time and unlock the full potential of your data.

Give it a try today and experience the future of document interaction!
