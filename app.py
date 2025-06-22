import streamlit as st

st.set_page_config(page_title="자기소개", layout="centered")

st.title("👤 자기소개")

st.write("안녕하세요. 저는 홍길동입니다.")

st.write("💼 직업: 전기공사산업기사")
st.write("🎓 학력: ○○대학교 전기공학과 졸업")
st.write("📌 관심분야: 전기 안전, 디지털 전환, 자동화 시스템")
st.write("✝️ 신앙: 천주교 신자")
st.write("📧 이메일: hong@example.com")
st.write("📱 연락처: 010-1234-5678")

st.markdown("---")  # 구분선

st.subheader("✨ 나의 한마디")
st.markdown("> 진리는 하느님께 있으며, 저는 그 길을 따라 묵묵히 나아가고자 합니다.")
st.subheader("🙏 신앙 고백")
st.write("어떤 상황에서도 하느님의 정의와 진리를 믿고 따르려 합니다.")
