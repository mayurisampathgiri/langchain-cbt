import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

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
                llm = ChatOpenAI(
                    temperature=0.7,
                    openai_api_key=os.getenv("OPENAI_API_KEY")
                )
                prompt = PromptTemplate.from_template(
                    "You are a CBT therapist. Help the user analyze this thought using cognitive behavioral therapy techniques:\n\n{user_input}"
                )
                chain = prompt | llm
                result = chain.invoke({"user_input": user_input})
                st.success("🧘 Here's a CBT-style reframing:")
                st.markdown(f"**{result}**")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
