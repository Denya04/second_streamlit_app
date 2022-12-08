import streamlit
import requests
import snowflake.connector

txt_quote = "'"
streamlit.title('Zina' + txt_quote + 's Amazing Athleisure Catalog')

#Snowflake-related functions
def get_catalog():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from catalog_for_website")
       return my_cur.fetchall()
      
# Add a button to load catalog list
if streamlit.button('Get Catalog'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_catalog()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)      

color_selection = my_data_rows.set_index('COLOR_OR_STYLE')

option = streamlit.selectbox(
    'Pick a sweatsuit color or style:',
     list(color_selection.index),[])

#fruits_selected = streamlit.multiselect("Pick a sweatsuit color or style:", list(my_data_rows.index),[])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
