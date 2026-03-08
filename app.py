import streamlit as st
from deep_translator import GoogleTranslator
st.title("Language Translation Tool")
text = st.text_area("Enter text to translate")
source = st.selectbox("Source Language", ["auto", "english", "tamil", "hindi"])
target = st.selectbox("Target Language",["english", "tamil", "hindi", "french"])
if st.button("Translate"):
    if text:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter some text.")
