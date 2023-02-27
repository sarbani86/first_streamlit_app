import streamlit
import pandas as pd
streamlit.title('Look !!my first app')
streamlit.header('Breakfast Manu')
streamlit.text('Omega 3 & Blue berry Oat Meal')
streamlit.text('Kale ,Spinach & Rocket smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#want to choose the friut by name
my_fruit_list=my_fruit_list.set_index('Fruit')
#lets pick the fruit
streamlit.multiselect("choose ur fruit : ",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)



