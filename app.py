import streamlit as st

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# -------------------------------
# 배경색 및 글자색 설정
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0B1F5E;
    color: white;
}

h1, h2, h3, p, div, span {
    color: white !important;
}

.stButton>button {
    background-color: white;
    color: #0B1F5E;
    border-radius: 10px;
    border: none;
    padding: 0.5em 1em;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #d9d9d9;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 화면 상태 관리
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# -------------------------------
# 메인 화면
# -------------------------------
if st.session_state.page == "main":

    st.markdown(
        "<h1 style='text-align:center;'>👋 안녕하세요</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("나도 인사하기"):
        st.session_state.page = "result"
        st.rerun()

# -------------------------------
# 결과 화면
# -------------------------------
else:

    st.balloons()

    st.markdown(
        "<h2 style='text-align:center;'>🎉 첫 웹페이지 제작을 축하해요!</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
