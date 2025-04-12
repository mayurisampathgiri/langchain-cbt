import streamlit as st
import requests

st.set_page_config(page_title="CBT Thought Reframer", page_icon="🧠")

st.title("🧠 CBT Thought Reframer")
st.markdown("Enter a negative or unhelpful thought below. This app will help reframe it using CBT-style guidance.")

user_input = st.text_area("💬 Your Thought", placeholder="e.g., I feel like I’m failing at everything.")

if st.button("Analyze Thought"):
    if not user_input.strip():
        st.warning("Please enter a thought to analyze.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/cbt/analyze",
                    json={"text": user_input},
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("🧘 Here's a CBT-style reframing:")
                    st.markdown(f"**{data['advice']}**")
                else:
                    st.error(f"Server error ({response.status_code}): {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")