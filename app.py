import streamlit as st
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''Fulfill the requested information to receive the taxifare''')

pickup_date = st.date_input('date', value = None,  format="YYYY/MM/DD")

pickup_time = st.time_input('time', value = None)

pickup_longitude = st.number_input('pickup_longitude', min_value=None, max_value=None,
                                   value='min', format="%0.2f")

pickup_latitude = st.number_input('pickup_latitude', min_value=None, max_value=None,
                                   value="min", format=None)

dropoff_longitude = st.number_input('dropoff_longitude', min_value=None, max_value=None,
                                   value="min", format=None)

dropoff_latitude = st.number_input('dropoff_latitude', min_value=None, max_value=None,
                                   value="min", format=None)

passenger_count = st.number_input('passengers', min_value=None, max_value=None,
                                   value="min", format="%0.0f")

fare_button = st.button('Get Taxifare')

if fare_button:
    pickup_datetime = f"{pickup_date } {pickup_time}"

    params = pd.DataFrame.from_dict({
        'pickup_datetime': [pickup_datetime],
        'pickup_longitude':[pickup_longitude],
        'pickup_latitude': [pickup_latitude],
        'dropoff_longitude': [dropoff_longitude],
        'dropoff_latitude': [dropoff_latitude],
        'passenger_count': [passenger_count]})

    params['pickup_datetime'] = pd.to_datetime(params['pickup_datetime'], utc=True)



url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(url, params=params)

status_code_dict = {
    200:'sucesso',
    400:'erro do cliente',
    401:'falta de autenticação',
    403:'falta de autenticação',
    500:'erro no servidor'}

if response.status_code == 200:
    print(f'The estimated taxifare is {response.json()}')

elif response.status_code in status_code_dict.key:
    print(status_code_dict[response.status_code])

else:
    print('erro desconhecido')
