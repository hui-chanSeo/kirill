import streamlit as st

st.set_page_config(page_title="자기소개", layout="centered")

st.title("👤 자기소개")

st.write("안녕하세요. 저는 24609502 서희찬 대학원생입니다.")

st.write("💼 직업: 육군훈련소 군무원")
st.write("🎓 학력: 전남대학교 전기공학과 졸업")
st.write("📌 관심분야: 시설안전, 디지털 전환")
st.write("✝️ 신앙: 천주교")
st.write("📧 이메일: knox411@naver.com")
st.write("📱 연락처: 010-4202-6709")

st.markdown("---")

st.subheader("✨ 나의 한마디")
st.markdown("> 이번 학기를 통해 요즘 시대의 최대 화두인 AI 산업에 대해 배울 수 있어 너무 좋았습니다.")

st.subheader("🎨 취미")

col1, col2 = st.columns(2)

with col1:
    st.image("sing.jpg", caption="🎤 노래 부르기", use_container_width=True)

with col2:
    st.image("book.jpg", caption="📚 책 읽기", use_container_width=True)