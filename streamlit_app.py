import streamlit
import snowflake.connector
import pandas

txt_quote = "'"
streamlit.title('Zina' + txt_quote + 's Amazing Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from catalog_for_website")
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.dataframe(my_catalog)
my_cnx.close()

streamlit.stop()
color_selection = my_catalog.set_index(0)


option = streamlit.selectbox(
    'Pick a sweatsuit color or style:',
     list(color_selection.index),[])

#fruits_selected = streamlit.multiselect("Pick a sweatsuit color or style:", list(my_data_rows.index),[])
#fruits_to_show = my_fruit_list.loc[fruits_selected]


#Snowflake-related functions
def get_catalog():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from catalog_for_website")
       return my_cur.fetchall()
