#Ctrl+C zastavuje stremlit

import streamlit as st

@st.cache_data #Dekorator
def expensive_computation():
    # Time-consuming computation here
    return result


st.title('My First Streamlit App') #titulek
st.write('Welcome to your first Streamlit app. Enter your name:') #textový formát
user_name = st.text_input('Name') #vstupní text
st.write(f'Hello, {user_name}!') #výstupní text


age = st.slider('How old are you?', 0, 80, 25) #slider od-do-skok
st.write("I'm ", age, 'years old')

with st.form(key='my_form'):
    text_input = st.text_input(label='Enter some text')
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write(f'Hello, {text_input}!')
    

age = st.slider("Your age", 0, 100)
st.write(f"You are {age} years old.")
if age < 18:
    st.error("You must be at least 18 years old.")

option = st.selectbox("Choose an option", ['A', 'B'])

with st.form("form"):
    if option == 'A':
        st.text_input("A's input")
    else:
        st.text_input("B's input")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted")
    
