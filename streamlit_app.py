import streamlit
import pandas
import requests
from urrlib.error import URLError


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
fruit = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit)


streamlit.header('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
streamlit.text("Snowflake info")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
streamlit.header('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')




# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


streamlit.stop()
import snowflake.connector
cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
cur = cnx.cursor()
cur.execute("select * from fruit_load_list")
data_rows = cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(data_rows)

fruit2be_added = streamlit.text_input("What fruit would you like to add ?")
cur.execute("insert into fruit_load_list values ('from streamlit')")
streamlit.write('Thanks for adding ', fruit2be_added)





