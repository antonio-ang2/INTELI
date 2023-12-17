import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Carregue o DataFrame
df = pd.read_csv('dados.csv')
df.rename(columns={'Annual Income (k$)': 'Income'}, inplace=True)
df.rename(columns={'Spending Score (1-100)': 'Score'}, inplace=True)

# Defina a configuração da página
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Carregue o estilo personalizado
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

url = "http://127.0.0.1:8000/predict_csv"

payload={}
files=[
  ('data',('dados.csv',open('dados.csv','rb'),'text/csv'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

predictions = response.json()["predictions"]  # Certifique-se de que "predictions" é a chave correta no JSON retornado


pred = response.text

df['pred'] = pred

    # Crie o gráfico scatter com os pontos previstos
# st.scatter_chart(data=df, x='pred', y='Income')

st.line_chart(df[['Age', 'pred']])



