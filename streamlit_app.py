import gspread
import pandas as pd
import numpy as np
import streamlit as st

def get_data():
    credentials = st.secrets.service_account
    gc = gspread.service_account_from_dict(credentials)
    wks = gc.open("pipeline-data").sheet1
    dataframe = pd.DataFrame(wks.get_all_records())
    
    return dataframe

graph_data = get_data()
st.image("https://www.candyrush.nz/cdn/shop/products/Hostess-Twinkie-Original-Unwrapped.png")
st.title(":red[Twinkies] are Forever")
st.text("Hostess Brands Inc (TWNK) daily closing stock price (US $)")
st.line_chart(graph_data.rename(columns={'Date':'index'}).set_index('index'))
st.button('Invest!') 
st.video("https://d1io3yog0oux5.cloudfront.net/_2199c089e968c5816a59e11eeedd0b5e/hostessbrands/db/871/8254/video_mp4/hostess-home.mp4")
