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

# 아래부터 앞으로의 꿈 + 영상
st.subheader("🌱 앞으로의 꿈")
st.write("""
저는 앞으로도 건양대학교 재난안전소방학과에 계속 다니며 박사과정까지 밟는 것을 목표로 하고 있습니다.  
특히 디지털 전환과 신재생에너지 자립을 실현하여 전기 및 소방 분야에서 획기적인 에너지 절약 기술을 개발하고,  
국제적으로 이슈가 되는 탄소세의 제약을 뛰어넘어 세계 환경산업을 선도하는 인재가 되고자 합니다.

이를 통해 우리나라가 다시 경제적 활력을 되찾는 데 기여하고,  
사회의 지속가능한 발전에 실질적인 도움을 주는 전문가로 성장하는 것이 저의 꿈입니다.
""")

st.subheader("🎥 영상 소개")
st.video("https://www.youtube.com/watch?v=46mebsp1Q4M")
st.video("https://www.youtube.com/watch?v=4N2ygGH6b70")