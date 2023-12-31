import streamlit 
import pandas
import requests 
import snowflake.connector
from urllib.error import URLError

streamlit.title("My parents healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Blueberry Oat Meal")
streamlit.text("🥗 Strawberry Cornflakes")
streamlit.text("🥑 Avoca Chocos")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("FruityVice Fruit Advice")
# streamlit.text(fruityvice_response.json())

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains: ")
streamlit.dataframe(my_data_row)


what_fruit = streamlit.text_input('What fruit would you like to add ?','Kiwi')
streamlit.write('Thanks for adding', what_fruit)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")


