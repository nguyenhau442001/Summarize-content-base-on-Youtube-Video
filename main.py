# import module
import streamlit as st
 
# Title
st.title("Summary Video Tool !!!")

# Add an edit box
user_input = st.text_input("Enter your text here:")
st.write("You entered:", user_input)
