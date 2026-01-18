import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="나만의 AI 챗봇", page_icon="🤖")

# 2. API 키 설정 (Streamlit Secrets에서 가져옴)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("API 키가 설정되지 않았습니다. Streamlit Secrets를 확인해주세요.")

# 3. 화면 디자인
st.title("🤖 무엇이든 물어보세요")
st.caption("Google Gemini 2.5 기반 최신 AI입니다.")

# 4. 챗봇 로직 (대화 기록 저장)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요! 저는 최신 Gemini 2.5 모델입니다. 무엇을 도와드릴까요?"}]

# 이전 대화 내용 화면에 출력
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 5. 사용자 입력 처리
if prompt := st.chat_input():
    # 사용자 입력 화면에 표시
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # AI 응답 생성 시도
    try:
        # ★여기가 핵심! 아까 조회된 최신 모델 이름으로 변경함★
        model = genai.GenerativeModel("gemini-2.5-flash") 
        
        response = model.generate_content(prompt)
        msg = response.text
        
        # AI 응답 화면에 표시 및 저장
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
        
    except Exception as e:
        st.error(f"에러가 발생했습니다: {e}")
