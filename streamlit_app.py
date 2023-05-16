import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("🥣 My parents healthy new diner")

streamlit.header("🥗 Breakfast Menu")
streamlit.text("🐔 Omega 3 & raspberry Oatmeal")
streamlit.text("🥑 Kale, Spinach & Rocket smoothie")
streamlit.text("🍞 Hard-boiled Free-rage egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
if fruits_selected==[]:
  streamlit.dataframe(my_fruit_list)
else:
  # Display the table on the page.
  streamlit.dataframe(fruits_to_show)
  
streamlit.header("Fruityvice Fruit Advice!")
#New api display

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# it normilize the json function for the data
streamlit.text(fruityvice_response)
if fruityvice_response=="<Response [404]>":
  streamlit.text("hi")
elae:
  streamlit.text("bye")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# onverts the data into table
streamlit.dataframe(fruityvice_normalized)
