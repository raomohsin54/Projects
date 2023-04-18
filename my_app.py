import streamlit as st
import os 
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_response(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":prompt}
    ])
    response = completion.choices[0].message.content
    return response

st.write(" Mohsin's bot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = ['i am ready to help you sir']

if 'past' not in st.session_state:
    st.session_state['past'] = ['hey there!']

def get_text():
    input_text = st.text_input("", key="input")
    return input_text

user_input = get_text()
if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')