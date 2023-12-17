import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_prediction(data):
    pass

df = pd.read_csv('dados.csv')
df.rename(columns={'Annual Income (k$)': 'Income'}, inplace=True)
df.rename(columns={'Spending Score (1-100)': 'Score'}, inplace=True)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.subheader('Line chart parameter')
line_data = st.sidebar.selectbox('Select data', ('Income', 'Score'))

st.sidebar.markdown('''
---
Created with ❤️ by me
''')

st.subheader('Comparation')

# Create a line chart
st.line_chart(df[[line_data, 'Age']])

# Create histograms
st.subheader('Histograms')

# Histogram for Age
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=30, alpha=0.5, color='b', label='Age')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)

# Histogram for Income
fig, ax = plt.subplots()
ax.hist(df[line_data], bins=30, alpha=0.5, color='g', label='Income')
ax.set_xlabel(line_data)
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)
