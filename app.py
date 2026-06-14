import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("Segmentacija Kupaca")
st.write("Projekat iz Data Mining-a. Analiza kupaca pomocu RFM i K-Means.")



uploaded_file = st.file_uploader("Ubaci CSV fajl ovdje")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Ucitani podaci:", df.head())

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    zadnji_datum = df['InvoiceDate'].max()


    recency = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
    recency['Recency'] = (zadnji_datum - recency['InvoiceDate']).dt.days

    frequency = df.groupby('CustomerID')['InvoiceDate'].count().reset_index()
    frequency.columns = ['CustomerID', 'Frequency']

    monetary = df.groupby('CustomerID')['Amount'].sum().reset_index()
    monetary.columns = ['CustomerID', 'Monetary']

    rfm = recency[['CustomerID', 'Recency']].merge(frequency, on='CustomerID')
    rfm = rfm.merge(monetary, on='CustomerID')

    st.write("Tabela sa RFM vrijednostima:", rfm.head())



    podaci_za_klasterovanje = rfm[['Recency', 'Frequency', 'Monetary']]
    
    kmeans = KMeans(n_clusters=3, random_state=0)
    rfm['Klaster'] = kmeans.fit_predict(podaci_za_klasterovanje)
    
    rfm['Klaster'] = rfm['Klaster'].astype(str)

    st.write("Kupci sa dodijeljenim klasterima:", rfm.head())


    st.write("Grafik: Recency vs Monetary")
    fig = px.scatter(rfm, x='Recency', y='Monetary', color='Klaster')
    st.plotly_chart(fig)

#Luka Tacic 23/101 FIST