import streamlit as st
import requests
import json

# Define the URL of the Lambda function
essay_score_url = 'https://ovsw43fsp76f4gaf7zn7lmpztm0jkqrb.lambda-url.ap-southeast-2.on.aws/'
summarize_text_url = 'https://ycbavt4o65otge4hyqojzxri6e0alynh.lambda-url.ap-southeast-2.on.aws/'

# Automated Essay Scoring
st.title('Automated Essay Scoring')
prompt = st.text_input('Prompt')
essay = st.text_area('Essay', height=200)

if st.button('Predict Essay Score'):
    # Define the data to send
    data = {
        "prompt": prompt,
        "essay": essay
    }

    with st.spinner('Predicting Essay Score...'):
        # Send a POST request
        response = requests.post(essay_score_url, data=json.dumps(data))

    # Parse the JSON response
    response_data = response.json()

    # Extract the predictions
    content_prediction = round(response_data['content'])
    written_context_prediction = round(response_data['written_context'])

    # Display the predictions
    st.write('Content: ', content_prediction)
    st.write('Development | Structure | Coherence: ', written_context_prediction)


# Summarize Written Text Prediction
st.title('Summarize Written Text Prediction')
passage = st.text_area('Passage', height=200)
response = st.text_area('Response')

if st.button('Predict Summarized Text'):
    # Define the data to send
    data = {
        "passage": passage,
        "user_response": response
    }

    with st.spinner('Predicting Summarized Text...'):
        # Send a POST request
        response = requests.post(summarize_text_url, data=json.dumps(data))

    # Parse the JSON response
    response_data = response.json()

    # Extract the predictions
    content_prediction = response_data['content']

    # Display the predictions
    st.write('Content: ', content_prediction)
