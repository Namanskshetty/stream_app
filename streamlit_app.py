import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # it normilize the json function for the data
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # onverts the data into table
    return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
#New api display
try:
  fruit_choice=streamlit.text_input("what fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

streamlit.header("The Fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


#if len(add_my_fruit)!=0:
 # my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('"+add_my_fruit+"')")
 # streamlit.write('Thanks for adding ', add_my_fruit)
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
    return "Thanks for adding "+new_fruit
add_my_fruit=streamlit.text_input('Add new fruit')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
streamlit.stop()
















