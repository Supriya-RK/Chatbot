from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx

# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key = "AIzaSyBlWBPkCXZ1zR1j9v0X970-ReGbFW-N7jE")

#function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history = [])

#Send the message to model and it willl stream the response hich we will later return
def get_gemini_response(question):
    response = chat.send_message(question,stream = True)
    return response

#Initialize Streamlit
st.set_page_config(page_title = "Q&A Demo")
st.title('Gemini-LLM-Application')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input : ",key = "input")
submit = st.button("Ask your Question")

if submit and input:
    response = get_gemini_response(input)

    #Add user input and response in the chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

    st.subheader('The Chat history is')

    for role,text in st.session_state['chat_history']:
        st.write(f"{role}:{text}")

    

