import streamlit
streamlit.title ('🥣 My parents New Healthy Diner')
streamlit.header('🥗 Breakfast menu')
streamlit.text ('🐔 Omega 3 and Blue berry Oatmeal')
streamlit.text ('🥑Kale, Spinach and Rocket Smoothie')
streamlit.text ('🍞Hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import Pandas
my_fruit_list = Pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.Dataframe(my_fruit_list)
