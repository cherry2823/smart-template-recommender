import streamlit as st
from recommender import recommend_templates

st.set_page_config(page_title="Canva-style Template Recommender", page_icon="🎨")

st.title("🎨 Canva-style Template Recommender")
st.write("Type a keyword to get matching design templates!")

# User input
user_input = st.text_input("Enter a keyword (e.g. travel, food, startup)")

# Number of recommendations
top_k = st.slider("Number of templates to recommend", 1, 5, 3)

if st.button("Recommend"):
    if not user_input:
        st.warning("Please enter a keyword.")
    else:
        with st.spinner("Generating recommendations..."):
            try:
                results = recommend_templates(user_input, top_k)
                st.success("Here are your recommended templates:")
                for item in results:
                    st.markdown(f"### {item['title']}")
                    st.write(item["description"])
                    st.markdown(f"**Tags:** `{', '.join(item['tags'])}`")
                    st.markdown("---")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
