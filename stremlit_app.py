import streamlit
streamlit.title ('🥣 My parents New Healthy Diner')
streamlit.header('🥗 Breakfast menu')
streamlit.text ('🐔 Omega 3 and Blue berry Oatmeal')
streamlit.text ('🥑Kale, Spinach and Rocket Smoothie')
streamlit.text ('🍞Hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick a fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
# display the table on the page
streamlit.dataframe(my_fruit_list)
