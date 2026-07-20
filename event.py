import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


col1, col2, = st.columns([1,6])
with col1:
    st.image('C:\\Users\\user\\Desktop\\강.jpg', width=250)

with col2:
    st.title("인화여자고등학교 도서관 공식 행사 안내")

left, right = st. columns([7,3])
with left:
    keywords = st.text_input(
        "Hidden Label", label_visibility="collapsed",
        placeholder="검색어를 입력해주세요"
    )

with right:
    st.button("행사 검색")


from streamlit_calendar import calendar

with st. container():
    con1, con2, con3, con4 = st.columns([2,1,3,2])

    with con1:
        st.subheader("여름맞이 책표지 창작 공모전")
        st.write("📅2026-07-07~2026-07-16")
    with con2:
        st.write("📅2026-07-07, 학생회")
    with con3:
        st.image('C:\\Users\\user\\Desktop\\독.jpg', width= 90)
        
    with con4:
        calendar(
            options={
            "initialView": "dayGridMonth",
            "headerToolbar": {
                "left": "prev,next",
                "center": "title",
                "right": ""
            },
            "height": 400, 
        },
        key="calendar"
    )





with st. container():
    f1, f2, f3 = st.columns([2,1,3])
    with f1:
        st.subheader("여름방학 독서 캠페인")
        st.write("📅2026-07-10~2026-07-17")
    with f2:
        st.write("📅2026-07-10, 도서부")

    with f3:
        st.image('C:\\Users\\user\\Desktop\\문.jpg', width= 90)

with st. container():
    st.subheader("(종료)한국 소설 비평문 접수 안내")
    st.write("📅2026-07-6")

with st. container():
    st.subheader("(종료)점심시간 캘리그라피 이벤트")
    st.write("📅2026-07-7")


st.pagination(10)
