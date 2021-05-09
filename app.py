import streamlit as st
import requests, uuid, json
st.title("Scripter")
text=st.text_area("Enter your text",value="Hi")
target_lang=st.text_input("Enter target language", value='it')
subscription_key = "3e7d57d42487401e9ea1b73c0b0c4c75"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "eastus"
path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': target_lang[:2]
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

if st.button("Submit"):
	st.write(response[0]['translations'][0]['text'])
