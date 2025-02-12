import streamlit as st

st.title('User Feedback Collection App')
with st.form(key='feedback_form'):
    name = st.text_input('Name:')
    content_quality = st.slider('Content Quality:', 1, 5, 3)
    speaker_performance = st.slider('Speaker Performance:', 1, 5, 3)
    feedback = st.text_area('Additional Feedback:')
    submit_button = st.form_submit_button('Submit')

if submit_button and name and feedback:
    st.write(f'Thank you, {name}, for your feedback!')
elif submit_button:
    st.error("Please fill out all fields.")