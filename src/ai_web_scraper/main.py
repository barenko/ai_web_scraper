import streamlit as st
from parse import parse_with_ollama
from scrape import (
    clean_body_content,
    extract_body_content,
    scrape_website,
    split_dom_content,
)

st.title("AI Web Scraper")
url = st.text_input("Enter the URL to scrape")

if st.button("Start Scraping"):
    st.write("Loading...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content


if "dom_content" in st.session_state:
    with st.expander("View Scraped DOM Content"):
        st.text_area("DOM Content", st.session_state.dom_content, height=300)

    parse_description = st.text_area(
        "Describe what you want to do with the scraped DOM content"
    )

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
