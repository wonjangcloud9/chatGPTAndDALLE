import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT 와 DALL-E를 활용한 텍스트로 이미지 생성")

with st.form(key="my_form"):
    user_input = st.text_input("프롬프트")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button(label="전송")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appeareance of the input. Response it shortly in 20 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })
    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=gpt_prompt,
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size,
        )

    st.image(dalle_response["data"][0]["url"], width=1024)


