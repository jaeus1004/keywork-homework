import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="나만의 AI 챗봇", page_icon="🤖")

# 2. API 키 설정 (Streamlit Secrets에서 가져옴)
# 주의: 배포 시 Secrets에 GOOGLE_API_KEY를 등록해야 함
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("API 키가 설정되지 않았습니다.")

# 3. 화면 디자인
st.title("🤖 무엇이든 물어보세요")
st.caption("Google Gemini 기반 AI입니다.")

# 4. 챗봇 로직
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # AI 응답 생성
    model = genai.GenerativeModel("gemini-pro") # 모델명
    response = model.generate_content(prompt)
    msg = response.text
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
