import streamlit
import pandas
import requests
from urllib.error import URLError
import snowflake.connector



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Display the table on the page.
streamlit.title("Youhoo my first Streamlit app is here!!")
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞🥑 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits2show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_selected)
streamlit.dataframe(fruits2show)


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit = streamlit.text_input('What fruit would you like information about?')
  if not fruit:
    streamlit.error("Please select a fruit to get information")
  else:
    streamlit.write('The user entered', fruit)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()


streamlit.header('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
streamlit.text("Snowflake info")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
streamlit.header('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(data_rows)

fruit2be_added = streamlit.text_input("What fruit would you like to add ?")
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
streamlit.write('Thanks for adding ', fruit2be_added)





