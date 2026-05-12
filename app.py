import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="FIT TALK",
    page_icon="👕"
)

# 화면 제목
st.title("👕 FIT TALK")
st.subheader("AI Personal Styling Chatbot")

st.write("오늘의 상황과 원하는 스타일을 입력하면 AI가 코디를 추천해주는 챗봇입니다.")

# 사용자 입력창
user_input = st.text_input("오늘 어떤 스타일이 필요하세요?")

# 버튼
if st.button("추천 받기"):
    if user_input:
        st.write("입력한 내용:")
        st.write(user_input)

        st.write("AI 추천 결과:")
        st.write("아직 AI 연결 전입니다. 다음 단계에서 Gemini API를 연결할 예정입니다.")
    else:
        st.warning("먼저 내용을 입력해주세요.")