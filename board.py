import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, = st.columns([1,2])
with col1:
    st.image('C:\\Users\\user\\Desktop\\고앵.jpg', width=250)

with col2:
    st.title("인화여고 전자도서관 공식 안내페이지")

