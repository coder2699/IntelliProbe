from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from streamlit_chat import message

# Load environment variables
load_dotenv()


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string


def extract_text_from_url(url):
    # Fetch the content from the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text content from the webpage
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text


def process_text(text):
    # Split the text into chunks using langchain
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Convert the chunks of text into embeddings to form a knowledge base
    embeddings = OpenAIEmbeddings()
    knowledgeBase = FAISS.from_texts(chunks, embeddings)

    return knowledgeBase


def main():
    st.title("Query Wizard 🪄")

    confluence_link = st.text_input('Paste the URL of the Confluence Page:')

    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []

    # container for chat history
    response_container = st.container()
    # container for text box
    text_container = st.container()

    if confluence_link:
        extracted_texts = extract_text_from_url(confluence_link)

        # Create the knowledge base object
        knowledgeBase = process_text(extracted_texts)

        with text_container:
            query = st.text_input("Query: ", key="input")
            if query:
                #FAISS similarity search
                docs = knowledgeBase.similarity_search(query)
                llm = OpenAI()
                chain = load_qa_chain(llm, chain_type='stuff')

                with st.spinner("typing..."):
                    with get_openai_callback() as cost:
                        response = chain.run(input_documents=docs, question=query)
                        print(cost)
                st.session_state.requests.append(query)
                st.session_state.responses.append(response)

        with response_container:
            if st.session_state['responses']:

                for i in range(len(st.session_state['responses'])):
                    message(st.session_state['responses'][i], key=str(i))
                    if i < len(st.session_state['requests']):
                        message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')


if __name__ == "__main__":
    main()
