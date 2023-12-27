import streamlit 
import pandas
streamlit.title("My parents healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Blueberry Oat Meal")
streamlit.text("🥗 Strawberry Cornflakes")
streamlit.text("🥑 Avoca Chocos")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
