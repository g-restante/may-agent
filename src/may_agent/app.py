import streamlit as st
import requests

BASE_URL = "http://localhost:8000/api/v1"

def clear_chat_history():
    """
    Clears the chat history in the session state.
    """
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me some questions about your files!"}]

def upload_file(doc):
    """
    Handles file upload and sends it to the backend for processing.

    Args:
        doc: The file uploaded by the user.

    Returns:
        str: Success or error message.
    """
    if not doc:
        return "No file selected. Please upload a file."
    
    try:
        with st.spinner("Processing..."):
            response = requests.post(url=f"{BASE_URL}/embedding/upload", files={'file': doc})
            if response.status_code == 202:
                return "File processed successfully!"
            else:
                return f"Error: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

def get_answer(prompt):
    """
    Sends a question to the backend and retrieves the AI-generated answer.

    Args:
        prompt (str): The user's question.

    Returns:
        str: The AI-generated answer or an error message.
    """
    try:
        response = requests.get(f"{BASE_URL}/ask", params={"question": prompt})
        if response.status_code == 200:
            return response.json().get('body', "No response body found.")
        else:
            return f"Error: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

def main():
    """
    Main function to render the Streamlit app.
    """
    st.set_page_config(
        page_title="MayAgentAI",
        page_icon="🤖"
    )

    # Sidebar for uploading files
    with st.sidebar:
        st.title("Menu:")
        doc = st.file_uploader(
            "Upload your Files and Click on the Submit & Process Button", accept_multiple_files=False)
        if st.button("Submit & Process"):
            message = upload_file(doc)
            if "Error" in message:
                st.error(message)
            else:
                st.success(message)

        st.button('Clear Chat History', on_click=clear_chat_history)

    # Main content area for chat
    st.title("Chat with your files using MayAgentAI 🤖")
    st.write("Welcome to the chat!")

    if "messages" not in st.session_state:
        clear_chat_history()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Display bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_answer(prompt)
                if "Error" in response:
                    st.error(response)
                else:
                    st.write(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()