import streamlit as st

# Page config
st.set_page_config(page_title="🔢 Session Counter")

st.title("🔢 Counter using Session Storage")
st.write("Counter value is stored using Streamlit session_state")

# Initialize session storage
if "count" not in st.session_state:
    st.session_state.count = 0

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment"):
        st.session_state.count += 1

with col2:
    if st.button("➖ Decrement"):
        st.session_state.count -= 1

with col3:
    if st.button("🔄 Reset"):
        st.session_state.count = 0

# Display counter
st.subheader("Current Count")
st.success(st.session_state.count)
