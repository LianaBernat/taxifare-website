import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''Fulfill the requested information to receive the taxifare''')

pickup_date = st.date_input('date', value = None,  format="YYYY/MM/DD")

pickup_time = st.time_input('time', value = None)

pickup_longitude = st.number_input('pickup_longitude', min_value=None, max_value=None,
                                   value='min', format="%0.6f")

pickup_latitude = st.number_input('pickup_latitude', min_value=None, max_value=None,
                                   value="min", format="%0.6f")

dropoff_longitude = st.number_input('dropoff_longitude', min_value=None, max_value=None,
                                   value="min", format="%0.6f")

dropoff_latitude = st.number_input('dropoff_latitude', min_value=None, max_value=None,
                                   value="min", format="%0.6f")

passenger_count = st.number_input('passengers', min_value=1, max_value=8,
                                   value="min", format="%d")

fare_button = st.button('Get Taxifare')


url = 'https://taxifare.lewagon.ai/predict'

status_code_dict = {
    200:'sucesso',
    400:'erro do cliente',
    401:'falta de autenticação',
    403:'falta de autenticação',
    500:'erro no servidor'}


if fare_button:
    pickup_datetime = datetime.combine(pickup_date, pickup_time)
    pickup_datetime = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S")

    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude':pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count}
    st.write("📤 Enviando parâmetros:", params)

    try:
        response = requests.get(url, params=params)
        st.write("📨 Status:", response.status_code)  # DEBUG
        st.write("📨 Resposta raw:", response.text)   # DEBUG
    except Exception as e:
        st.error(f"❌ Erro na requisição: {e}")
        st.stop()


    if response.status_code == 200:
        st.success(f"💰 Estimated fare: {response.json()}")

    else:
       st.error(f"❌ Erro {response.status_code} — {status_code_dict.get(response.status_code, 'desconhecido')}")
