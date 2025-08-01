# streamlit_app.py
import streamlit as st
from utils import evaluate_strength, calculate_entropy, check_breach, suggest_improvements

st.set_page_config(page_title="Password Strength & Breach Checker", page_icon="🔐")
st.title("🔐 Password Strength & Breach Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength, rules = evaluate_strength(password)
    entropy = calculate_entropy(password)
    breach_count = check_breach(password)

    st.subheader(f"Password Strength: {strength}")
    st.write(f"Entropy Score: `{entropy} bits`")

    if breach_count == -1:
        st.warning("⚠️ Could not check for breaches. API error.")
    elif breach_count == 0:
        st.success("✅ This password has NOT been found in known breaches.")
    else:
        st.error(f"❌ This password has been found in `{breach_count}` breaches!")

    suggestions = suggest_improvements(rules)
    if suggestions:
        st.markdown("**Suggestions to Improve:**")
        for s in suggestions:
            st.write(f"- {s}")
