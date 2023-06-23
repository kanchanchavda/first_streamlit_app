import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title ('🥣 My parents New Healthy Diner')
streamlit.header('🥗 Breakfast menu')
streamlit.text ('🐔 Omega 3 and Blue berry Oatmeal')
streamlit.text ('🥑Kale, Spinach and Rocket Smoothie')
streamlit.text ('🍞Hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick a fruit they want to include
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# display the table on the page
streamlit.dataframe(fruits_to_show)

#create a repeatable code block called function (it's function)
def get_fruityvice_data(this_fruit_choice):
 streamlit.write('The user entered ', fruit_choice)
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")

#import requests
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select the fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
  else:
 
except URLError as e:
    streamlit.error()
#streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from Fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# Allow end user to add fruit to the list
add_my_fruit = streamlit.text_input('what fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding',  add_my_fruit)
my_cur.execute(  "Insert into fruit_load_list values ('from streamlit')")                            
