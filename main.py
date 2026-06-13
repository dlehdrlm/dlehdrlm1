import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

st.title("🎮 MBTI 포켓몬 추천기")
st.markdown("### ✨ 나와 가장 잘 어울리는 포켓몬은?")
st.write("MBTI를 입력하면 성격에 맞는 포켓몬을 추천해줄게!")

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠 🧠",
        "desc": "전략적이고 독립적인 리더형. 뛰어난 분석력과 강한 의지를 가지고 있어."
    },
    "INTP": {
        "pokemon": "후딘 🔮",
        "desc": "호기심이 많고 아이디어가 넘치는 탐구형. 새로운 지식을 좋아해."
    },
    "ENTJ": {
        "pokemon": "리자몽 🔥",
        "desc": "강한 추진력과 리더십을 가진 카리스마형."
    },
    "ENTP": {
        "pokemon": "팬텀 👻",
        "desc": "재치 있고 창의적인 아이디어 뱅크. 사람들을 놀라게 하는 걸 좋아해."
    },
    "INFJ": {
        "pokemon": "루기아 🌊",
        "desc": "깊은 통찰력과 따뜻한 마음을 가진 이상주의자."
    },
    "INFP": {
        "pokemon": "이브이 🌈",
        "desc": "감수성이 풍부하고 가능성이 무한한 몽상가."
    },
    "ENFJ": {
        "pokemon": "피카츄 ⚡",
        "desc": "주변 사람들에게 에너지를 주는 인기쟁이."
    },
    "ENFP": {
        "pokemon": "뮤 🌟",
        "desc": "자유롭고 창의적인 모험가. 어디로 튈지 모르는 매력이 있어."
    },
    "ISTJ": {
        "pokemon": "거북왕 💧",
        "desc": "책임감이 강하고 믿음직한 현실주의자."
    },
    "ISFJ": {
        "pokemon": "해피너스 💖",
        "desc": "배려심이 많고 주변을 잘 챙기는 수호자."
    },
    "ESTJ": {
        "pokemon": "보스로라 🛡️",
        "desc": "원칙을 중요하게 생각하는 든든한 리더."
    },
    "ESFJ": {
        "pokemon": "푸린 🎤",
        "desc": "친화력이 뛰어나고 사람들과 어울리는 것을 좋아해."
    },
    "ISTP": {
        "pokemon": "루카리오 🥊",
        "desc": "냉철하고 실용적인 문제 해결사."
    },
    "ISFP": {
        "pokemon": "나인테일 ✨",
        "desc": "감각적이고 예술적인 매력을 가진 자유로운 영혼."
    },
    "ESTP": {
        "pokemon": "번치코 🔥",
        "desc": "도전 정신이 강하고 행동력이 뛰어난 승부사."
    },
    "ESFP": {
        "pokemon": "꼬부기 😎",
        "desc": "유쾌하고 에너지 넘치는 분위기 메이커."
    }
}

mbti = st.text_input(
    "🔍 MBTI를 입력해봐!",
    placeholder="예: ENFP"
).upper()

if st.button("🎁 포켓몬 추천받기"):
    if mbti in pokemon_data:
        result = pokemon_data[mbti]

        st.balloons()

        st.success(f"🎉 {mbti}에게 가장 잘 어울리는 포켓몬!")

        st.markdown(
            f"""
            <div style="
                padding:20px;
                border-radius:15px;
                background:linear-gradient(135deg,#FFD700,#FFF8DC);
                color:black;
                text-align:center;
                ">
                <h1>{result['pokemon']}</h1>
                <h3>🌟 성향 분석</h3>
                <p style="font-size:18px;">
                {result['desc']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info("💡 MBTI는 참고용일 뿐! 재미로 즐겨줘 😄")

    else:
        st.error("❌ 올바른 MBTI를 입력해줘! (예: INFP, ESTJ)")
