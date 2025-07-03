# app.py is The Streamlit UI

import streamlit as st
from login_manager import login_mstock
from secrets_manager import save_credentials

st.title("🔐 mStock Login")

user_id = st.text_input("User ID")
password = st.text_input("Password", type="password")
api_key = st.text_input("API Key (A)")
pi_key = st.text_input("PI Key (B)")
otp = st.text_input("Enter OTP from your mobile")

if st.button("Login"):
    result = login_mstock(user_id, password, api_key)
    if result.get("code") == "0":
        st.success("✅ Logged in successfully!")
        save_credentials({
            "user_id": user_id,
            "api_key": api_key,
            "pi_key": pi_key,
            "access_token": result.get("data", {}).get("accessToken")
        })
    else:
        st.error("❌ Login failed: " + result.get("message", "Unknown error"))
