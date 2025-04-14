import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load API key from Streamlit secrets
openai_key = st.secrets["OPENAI_API_KEY"]

# Initialize LLM
llm = ChatOpenAI(api_key=openai_key, model="gpt-3.5-turbo", temperature=0.7)

# Define CBT prompt
prompt = PromptTemplate.from_template("""
You are a compassionate CBT therapist.
Help reframe the user's thought using CBT techniques:

Thought: {user_input}
""")

# Chain setup
chain = prompt | llm

# UI
st.set_page_config(page_title="CBT Thought Reframer", page_icon="🧠")
st.title("🧠 CBT Thought Reframer")
st.markdown("Enter a negative or unhelpful thought below. This app will help reframe it using CBT-style guidance.")

user_input = st.text_area("💬 Your Thought", placeholder="e.g., I feel like I’m failing at everything.")

if st.button("Analyze Thought"):
    if not user_input.strip():
        st.warning("Please enter a thought to analyze.")
    else:
        try:
            with st.spinner("Analyzing with AI therapist..."):
                response = chain.invoke({"user_input": user_input})
                # Extract and display only the content from the LLM response
                if hasattr(response, "content"):
                    st.success("🧘 Here's a CBT-based reframing of your thought:")
                    st.markdown(response.content)
                else:
                    st.error("❌ Unexpected response format.")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
