import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("🥣 My parents healthy new diner")

streamlit.header("🥗 Breakfast Menu")
streamlit.text("🐔 Omega 3 & raspberry Oatmeal")
streamlit.text("🥑 Kale, Spinach & Rocket smoothie")
streamlit.text("🍞 Hard-boiled Free-rage egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
