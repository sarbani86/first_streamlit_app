import streamlit
import pandas as pd
streamlit.title('Look !!my first app')
streamlit.header('Breakfast Manu')
streamlit.text('Omega 3 & Blue berry Oat Meal')
streamlit.text('Kale ,Spinach & Rocket smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



