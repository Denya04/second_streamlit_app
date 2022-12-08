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
