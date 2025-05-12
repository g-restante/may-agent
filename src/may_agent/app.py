import streamlit as st
import requests

BASE_URL = "http://localhost:8000/api/v1"

def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me some questions about your files!"}]

def main():
    st.set_page_config(
        page_title="MayAgentAI",
        page_icon="🤖"
    )

    # Sidebar for uploading PDF files
    with st.sidebar:
        st.title("Menu:")
        doc = st.file_uploader(
            "Upload your Files and Click on the Submit & Process Button", accept_multiple_files=False)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                response = requests.post(url=f"{BASE_URL}/embedding/upload", files={'file': doc})
                if response.status_code == 202:
                    st.success("Done")
                else:
                    st.error("Error: " + response.text)
                    full_response = "Error: " + response.text

    # Main content area for displaying chat messages
    st.title("Chat with your files using MayAgentAI🤖")
    st.write("Welcome to the chat!")
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    # Chat input
    # Placeholder for chat messages

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me some questions about your files!"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Display chat messages and bot response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = requests.get(f"{BASE_URL}/ask", params={"question": prompt})
                if response.status_code == 200:
                    placeholder = st.empty()
                    full_response = ''
                    placeholder.markdown(response.json().get('body'))
                else:
                    st.error("Error: " + response.text)
                    full_response = "Error: " + response.text
        if response is not None:
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)


if __name__ == "__main__":
    main()