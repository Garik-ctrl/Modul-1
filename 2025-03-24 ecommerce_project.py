import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv("ecommerce_data.csv", parse_dates=True, index_col="Date")
df = pd.read_csv("ecommerce_data.csv")
df= df.set_index(pd.to_datetime(df["Date"]).dt.date)
df= df.drop(columns=["Date"]) 
#df = df.sort_index()

st.title("E-commerce Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Summary Statistics")
st.write(df.describe(include='all'))

st.sidebar.header("Filtry")

min_date = df.index.min()
max_date = df.index.max()
date_range = st.sidebar.date_input("Vyberte datum", [min_date, max_date])


categories = df['Product'].dropna().unique()
selected_categories = st.sidebar.multiselect("Vyber Produkt", categories, default=categories)
df = df[df['Product'].isin(selected_categories)]


regions = df['Region'].dropna().unique()
selected_regions = st.sidebar.multiselect("Select Regions", regions,default=regions)
df = df[df['Region'].isin(selected_regions)]

st.subheader("Vývoj Revenue v čase")
Revenue_over_time = df.groupby(df.index)['Revenue'].sum().reset_index()
st.line_chart(Revenue_over_time.set_index('Date'))

st.subheader("Barchart - produkty a Revenue")
top_products = df.groupby('Product')['Revenue'].sum()
st.bar_chart(top_products)

st.subheader("Pie chart - region")
Revenue_by_region = df.groupby('Region')['Revenue'].sum()
fig, ax = plt.subplots()
ax.pie(Revenue_by_region, labels=Revenue_by_region.index, autopct='%1.1f%%')
st.pyplot(fig)
