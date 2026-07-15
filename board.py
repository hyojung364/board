
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, = st.columns([1,2])
with col1:
    st.image('C:\\Users\\user\\Desktop\\고앵.jpg', width=250)

with col2:
    st.title("인화여고 전자도서관 공식 안내페이지")

left, right = st.columns([7,3])
with left:
    keywords = st.text_input(
        "Hidden Label", label_visibility="collapsed",
         placeholder="검색어를 입력해주세요")

with right:
    st.button("공지 검색")




with st.container():
    st.subheader("도서관 이용 안내")
    st.write("📅 2026-07-01")

with st.container():
    st.subheader("여름방학 중 도서 대출/반납 안내")
    st.write("📅 2026-07-02")

with st. container():
    st.subheader("도서관 신착 도서 안내")
    st.write("📅 2026-07-03")

with st.container():
    st.subheader("도서관 개설 안내")
    st.write("📅 2026-07-04")

st.pagination(10)

