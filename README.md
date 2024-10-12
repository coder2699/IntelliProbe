# IntelliProbe

IntelliProbe is an interactive tool that allows users to input the URL of any article and ask questions related to its content. Built using Langchain, Streamlit, OpenAI, and FAISS, this chatbot efficiently retrieves and analyzes article data to provide accurate responses.

In today’s fast-paced information environment, extracting relevant insights from articles can be time-consuming and overwhelming. IntelliProbe leverages advanced AI technologies to streamline this process. 

Users can simply provide a URL, and the chatbot will fetch the content, enabling them to ask specific questions about the article. This project showcases the power of modern AI techniques and provides an intuitive interface for enhanced user interaction.

<img width="860" alt="288850879-620ea79c-b58c-4e1d-9fc6-e9824b17ec3f" src="https://github.com/coder2699/IntelliProbe/assets/61552810/bba19433-2a59-4510-9ce1-e2bcf18519e2">

### 🪄 Features
***
- **URL Input:** Users can input the URL of any article for analysis.
- **Dynamic Questioning:** Users can pose questions related to the article's content.
- **Fast Content Retrieval:** Utilizes FAISS for efficient indexing and retrieval of article data.
- **Natural Language Processing:** Powered by OpenAI's language model for understanding and generating human-like responses.
- **User-Friendly Interface:** Built with Streamlit for an easy and engaging user experience.
- **Context-Aware Responses:** Provides accurate answers based solely on the content of the provided article.

### 💫 Technologies Used
***
- **Langchain:** For managing the components of the language model and data flow.
- **Streamlit:** To build a simple and interactive web application interface.
- **OpenAI:** For the natural language processing capabilities that power the chatbot.
- **FAISS:** For efficient similarity search and retrieval of article content.

### 🧑‍💻 Setup
***
Setup a python environment & create a .env file to add openai api key:
```
OPENAI_API_KEY = sk-xxxxxxxxxxx
```

To install requirements:
```
pip install -r requirements.txt
pip install streamlit-chat
pip install BeautifulSoup4
pip install tiktoken 
```
To run the application:
```
streamlit run main.py
```

### ©️ License
***
This project is licensed under the MIT License - see the <a href="https://github.com/coder2699/IntelliProbe/blob/main/LICENSE">LICENSE file</a> for details.

### ❤ Show your support
***
</p><p>Give a <g-emoji class="g-emoji" alias="star" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2b50.png">⭐️</g-emoji> if this project helped you!</p>
