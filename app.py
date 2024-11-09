import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_longitude = st.number_input('pickup longitude', min_value=-90.0, max_value=90.0, value=-73.950655, step=0.1)
pickup_latitude = st.number_input('pickup latitude', min_value=-90.0, max_value=90.0, value=40.783282, step=0.1)
dropoff_longitude = st.number_input('dropoff longitude', min_value=-90.0, max_value=90.0, value=-73.984365, step=0.1)
dropoff_latitude = st.number_input('dropoff latitude', min_value=-90.0, max_value=90.0, value=40.769802, step=0.1)

passenger_count = st.number_input('passenger count', min_value=1, max_value=8)

url_pred = 'https://taxifare.lewagon.ai/predict'

pickup_datetime = datetime.datetime.now()

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

response = requests.get(url_pred, params=params)

prediction = response.json()

pred = round(prediction['fare'], 2)

st.write(f"The predicted fare is {pred}")
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
