import streamlit as st
import google.generativeai as genai

st.title("🔎 모델 이름 찾기")

# 1. API 키 설정
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    st.write("내 키로 사용 가능한 모델 목록을 조회합니다...")
    
    # 2. 구글 서버에 있는 모델 목록을 다 가져옵니다
    models = genai.list_models()
    
    found_any = False
    for m in models:
        # 'generateContent' 기능이 있는 모델만 보여줍니다
        if 'generateContent' in m.supported_generation_methods:
            st.success(f"사용 가능 👉 {m.name}")
            found_any = True
            
    if not found_any:
        st.error("❌ 사용 가능한 모델이 하나도 검색되지 않습니다. API 키를 새로 발급받아야 할 수도 있습니다.")
        
except Exception as e:
    st.error(f"오류 발생: {e}")
