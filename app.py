import openai
import streamlit as st
import os

st.title("ChatGPT-like Chatbot")

openai.api_key = st.secrets['OPEN_API_KEY']

client = openai.OpenAI(api_key = st.secrets['OPEN_API_KEY'])#(os.getenv("OPEN_API_KEY"))

if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = "gpt-3.5-turbo"

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role" : "user","content" : prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


    # with st.chat_message("assistant"):
    #     message_placeholder = st.empty()    
    #     full_response = ""
    #     # for response in openai.chat.completions.create(
    #     for response in client.chat.completions.create(
    #         model = st.session_state["openai_model"],
    #         messages=[
    #             {"role" : m["role"],"content":m["content"]}
    #             for m in st.session_state.messages   
    #         ],
    #         stream = True,

    #     ):
    #         # full_response+=response.choices[0].delta.get("content","")
    #         full_response+=response.choices[0].message.content.strip()#("content","")
    #         message_placeholder.markdown(full_response + "")
    #     message_placeholder.markdown(full_response)
    # st.session_state.messages.append({"role":"assistant","content":full_response})
