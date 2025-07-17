import streamlit as st
from datetime import datetime
from src.stock_picker.crew import StockPicker
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="📊 AI Stock Picker", layout="wide")

st.title("📈 AI-Powered Stock Picker")
st.markdown(
    """
    This application uses a multi-agent CrewAI system to:
    - Find trending companies in the news 📰  
    - Perform in-depth financial research 📊  
    - Recommend the best company for investment ✅  
    """
)

# Sidebar input
st.sidebar.header("Configuration")
sector = st.sidebar.selectbox(
    "Choose a sector to analyze:",
    ["Finance", "Technology", "Healthcare", "Energy", "Consumer Goods"]
)

run_button = st.sidebar.button("🚀 Run Stock Picker")

# Trigger AI crew when user clicks
if run_button:
    st.sidebar.info("Running CrewAI agents...")
    st.info("⏳ Analyzing news, researching financials, and choosing the best investment...")

    with st.spinner("AI is working..."):
        inputs = {
            "sector": sector,
            "current_date": str(datetime.now())
        }

        result = StockPicker().crew().kickoff(inputs=inputs)

    st.success("✅ Analysis Complete!")

    # Display output
    st.subheader("📌 Final Decision")
    st.code(result.raw, language="markdown")

    # Optionally download results
    st.download_button(
        label="📥 Download Decision",
        data=result.raw,
        file_name=f"{sector}_stock_pick.txt",
        mime="text/plain"
    )
