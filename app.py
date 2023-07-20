import streamlit as st
import requests
import json

# Define the URL of the Lambda function
url = 'https://ovsw43fsp76f4gaf7zn7lmpztm0jkqrb.lambda-url.ap-southeast-2.on.aws/'

# Set up Streamlit
st.title('Automated Essay Scoring')
prompt = st.text_input('Prompt')
essay = st.text_area('Essay', height=200)


if st.button('Predict'):
    # Define the data to send
    data = {
        "prompt": prompt,
        "essay": essay
    }

    with st.spinner('Predicting...'):
        # Send a POST request
        response = requests.post(url, data=json.dumps(data))

    # Parse the JSON response
    response_data = response.json()
    print(response_data)

    # Extract the predictions
    content_prediction = round(response_data['content'])
    written_context_prediction = round(response_data['written_context'])

    # Display the predictions
    st.write('Content: ', content_prediction)
    st.write('Development | Structure | Coherence: ', written_context_prediction)

