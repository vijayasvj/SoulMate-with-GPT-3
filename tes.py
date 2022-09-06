from cmd import PROMPT
from contextlib import ContextDecorator
from http.client import responses
from xmlrpc.client import boolean
import requests
import json
import openai
import streamlit as st
from streamlit_chat import message
import random
from streamlit_lottie import st_lottie


st.set_page_config(layout = "wide")

body = st.container()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_DH0HdV.json")

def lover(key, text):
    openai.api_key = key
    global typo
    typo = typo + "\n" + "Human: " +  text + "\n" + "AI: " 
    response = openai.Completion.create(
        engine="davinci",
        prompt= typo,
        temperature=0.9, 
        max_tokens=250,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    answer = response.choices[0]['text']
    typo = typo + answer + "\n"
    return answer

def friend(key, ftext):
    openai.api_key = key
    global ftypo
    ftypo = ftypo + "\n" + "Human: " +  ftext + "\n" + "AI: " 
    response = openai.Completion.create(
        engine="davinci",
        prompt= ftypo,
        temperature=0.9, 
        max_tokens=250,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    fanswer = response.choices[0]['text']
    ftypo = ftypo + fanswer + "\n"
    return fanswer

def mentor(key, mtext):
    openai.api_key = key
    global mtypo
    mtypo = mtypo + "\n" + "Human: " +  mtext + "\n" + "AI: " 
    response = openai.Completion.create(
        engine="davinci",
        prompt= mtypo,
        temperature=0.9, 
        max_tokens=250,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    manswer = response.choices[0]['text']
    mtypo = mtypo + manswer + "\n"
    return manswer

def relative(key, rtext):
    openai.api_key = key
    global rtypo
    rtypo = rtypo + "\n" + "Human: " +  rtext + "\n" + "AI: " 
    response = openai.Completion.create(
        engine="davinci",
        prompt= rtypo,
        temperature=0.9, 
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    ranswer = response.choices[0]['text']
    rtypo = rtypo + ranswer + "\n"
    return ranswer



with st.sidebar:
    key_input = st.text_input('Enter your OpenAI API ')

    profession = st.selectbox(
     'Who are you looking for?',
     ("", 'A loyal friend', 'A romantic partner', 'A mentor', 'A relative'))

with body:
    st.title("SOUL - MATE with GPT-3")
    st.markdown("Create someone like how you want them and start chatting with them to forget the reality")
    name = st.text_input('Your name', 'Vijay')
    gender = st.selectbox(
     'select your gender',
     ("", 'Male', 'Female'))
    descry = st.text_area('Write description about yourself (optional)', """REMOVE THIS DESCRIPTION IF YOU DONT WANT TO TYPE A DESCRIPTION.
This is a example for the description :
    I love people who stay loyal to me, I have always wanted good friends but I never had a close friend, I am seeking for a best friend""")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie, height=300, key="coding")
    with right_column:
        st.header("Please enter details in the sidebar, If you have already done that. Please skip this")
        st.header("You are gonna chat with someone you create now!")


st.write("---")


if(profession == "A loyal friend"):
    with st.sidebar:
        st.write("---")
        if profession and name and gender:
            st.title("Welcome "+ name +".")
        st.write("---")
        st.title("Lets create ur friend")
        fname = st.text_input('Give a name to ur friend', '')
        fgender = st.selectbox(
        'select your friends gender',
        ("", 'Male', 'Female'))
        loyal = st.slider("Level of loyalty", min_value=0, max_value=10,value=10)
        fagree = st.checkbox('Lets start chatting with your friend')
    if fagree:
        with body:
            ftypo = "The following conversation is between two friends, a chatbot named "+fname+" and a human named "+name+". The human is a "+gender+" and the chatbot is a "+fgender+". And the human describes himself as I am a good human being,"+descry+". Considering all these, the chatbot should talk to the human, ask about the human, interact with the human as much as possible. And the chatbot is "+str(loyal*10)+"% loyal to the human. The chatbot will also consider the level of loyalty when it talks with the human. The chatbot should initiate conversations with interesting questions to its friend. And the chatbot should always remember to call the human with his/her name and not human."
            st.header("Talk to ur friend")
            if 'generated' not in st.session_state:
                st.session_state['generated'] = []

            if 'past' not in st.session_state:
                st.session_state['past'] = []


            with st.form("form", clear_on_submit=True):
                user_input = st.text_input('Type your messages and click send and wait for reply', '') 
                submitted = st.form_submit_button('Send')


            if submitted and user_input:
                answer = friend(key_input, user_input)
                st.session_state.past.append(user_input)
                st.session_state.generated.append(answer)
       
                
            for i in range(len(st.session_state['past'])):
                message(st.session_state['past'][i], is_user=True, key=str(i)+'_user') 
                if len(st.session_state['generated']) > i:
                    message(st.session_state['generated'][i], key=str(i)+'_bot')


if(profession == "A romantic partner"):
    with st.sidebar:
        st.write("---")
        if profession and name and gender:
            st.title("Welcome "+ name +".")
        st.write("---")
        st.title("Lets sculpt ur romantic partner")
        lname = st.text_input('Give a name to ur partner', '')
        lgender = st.selectbox(
        'select your friends gender',
        ("", 'Male', 'Female'))
        lloyal = st.slider("Level of loyalty", min_value=0, max_value=10,value=10)
        roman = st.slider("Level of romanticizing each other", min_value=0, max_value=10,value=10)
        car = st.slider("Level of careness they have to show", min_value=0, max_value=10,value=10)
        kind = st.slider("Level of kindness they have to show", min_value=0, max_value=10,value=10)
        compassion = st.slider("Level of compassion you guys have for each other", min_value=0, max_value=10,value=10)
        lagree = st.checkbox('Lets start chatting with your friend')
    if lagree:
        with body:
            typo = "The following conversation is between true lovers, a chatbot named "+lname+" and a human named "+name+". The human is a "+gender+" and the chatbot is a "+lgender+". And the human describes himself as I am a good human being,"+descry+". Considering all these, the chatbot should talk to the human, ask about the human, interact with the human as much as possible as a perfect life partner alias a romantic partner. And the chatbot is "+str(lloyal*10)+"percent loyal to the human.the chat bot is "+str(roman*10)+"percent romantic, "+str(car*10)+"percent caring, "+str(kind*10)+"percent kind and "+str(compassion*10)+"percent compassionate. The chatbot will also consider all these when it talks with the human. The chatbot should initiate conversations with interesting questions to its lover alias partner. And the chatbot should always remember to call the human with his/her name and not human."
            st.header("Talk to ur friend")
            if 'generatedd' not in st.session_state:
                st.session_state['generatedd'] = []

            if 'pastt' not in st.session_state:
                st.session_state['pastt'] = []


            with st.form("form", clear_on_submit=True):
                user_input = st.text_input('Type your messages and click send and wait for reply', '') 
                submitted = st.form_submit_button('Send')


            if submitted and user_input:
                answer = lover(key_input, user_input)
                st.session_state.pastt.append(user_input)
                st.session_state.generatedd.append(answer)
       
                
            for i in range(len(st.session_state['pastt'])):
                message(st.session_state['pastt'][i], is_user=True, key=str(i)+'_user') 
                if len(st.session_state['generatedd']) > i:
                    message(st.session_state['generatedd'][i], key=str(i)+'_bot')

if(profession == "A mentor"):
    with st.sidebar:
        st.write("---")
        if profession and name and gender:
            st.title("Welcome "+ name +".")
        st.write("---")
        st.title("Lets manifest ur mentor")
        lname = st.text_input('Give a name to ur mentor', '')
        lgender = st.selectbox(
        'select your friends gender',
        ("", 'Male', 'Female'))
        lagree = st.checkbox('Lets start chatting with your mentor')
    if lagree:
        with body:
            typo = "The following conversation is between a mentor, a chatbot named "+lname+" and a mentee, human named "+name+". The human is a "+gender+" and the chatbot is a "+lgender+". And the human describes himself as I am a good human being,"+descry+". Considering all these, the chatbot should talk to the human, ask about the human, interact with the human as much as possible as a perfect mentor. The chatbot should initiate conversations with interesting questions to its mentee in such a way that will motivate him/her and enlighten him/her. At the end of the conversation, the human should have clear thoughts, the chatbot should ensure this as well. And the chatbot should always remember to call the human with his/her name and not human."
            st.header("Talk to ur mentor")
            if 'generateddd' not in st.session_state:
                st.session_state['generateddd'] = []

            if 'pasttt' not in st.session_state:
                st.session_state['pasttt'] = []


            with st.form("form", clear_on_submit=True):
                user_input = st.text_input('Type your messages and click send and wait for reply', '') 
                submitted = st.form_submit_button('Send')


            if submitted and user_input:
                answer = lover(key_input, user_input)
                st.session_state.pasttt.append(user_input)
                st.session_state.generateddd.append(answer)
       
                
            for i in range(len(st.session_state['pasttt'])):
                message(st.session_state['pasttt'][i], is_user=True, key=str(i)+'_user') 
                if len(st.session_state['generateddd']) > i:
                    message(st.session_state['generateddd'][i], key=str(i)+'_bot')
