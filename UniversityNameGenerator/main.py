import streamlit as st
import langchain_helper  # make sure this has generate_major_and_universities()

st.title("University Finder by Province")

province = st.sidebar.selectbox(
    "Choose a Province",
    (
        "British Columbia",
        "Alberta",
        "Saskatchewan",
        "Manitoba",
        "Ontario",
        "Quebec",
        "New Brunswick",
        "Prince Edward Island",
        "Nova Scotia",
        "Newfoundland and Labrador"
    )
)

if province:
    response = langchain_helper.generate_major_and_universities(province)

    # Display Major
    st.subheader(f"Trending Major in {province}")
    st.write(response['major'].strip())

    # Display Universities
    st.subheader("Top Universities Offering This Major")
    universities = response['text'].strip().split(",")
    for uni in universities:
        st.write("-", uni.strip())

