import streamlit as st
import random


st.set_page_config(
   page_title="🤖 Camilo Franco",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)



st.title("Mi Primera Aplicación *Piedra Papel o Tijeras!*")

options = ['Piedra', 'Papel', 'Tijeras']

user_select = st.selectbox('Select one option : ', options)


st.write("User Select :  ",user_select)


random_options = (random.randint(0,2))
computer_option = options[random_options]

st.write("Computer select : ",computer_option)


if user_select == computer_option:
    st.header("!!Empate!! 🥴 ")

elif user_select == "Piedra":
    if computer_option =="Tijeras":
        st.header("Usuario Gana Piedra rompe tijeras😀")
    else :
        if computer_option == "Papel":
             st.header("Computador Gana papel tapa a piedra ☹️")

elif user_select == "Papel":
    if computer_option == "Tijeras":
        st.header("Computador gana tijeras corta a papel 😢")
    else :
        if computer_option == "Piedra":
            st.header("Usuario Gana papel tapa a piedra 😀") 

elif user_select == "Tijeras":
    if computer_option == "Piedra":
        st.header("Computador gana piedra rompe tijeras ☹️")
    else :
        if computer_option == "Papel":
            st.header("Usuario Gana tijeras corta papel 😀")

