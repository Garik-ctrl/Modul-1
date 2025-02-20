import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = "sample_weather_data.csv" # Načtení dat
data = pd.read_csv(file_path)

# přidání sloupcu na rozporcování daného data
data['Date'] = pd.to_datetime(data['Date']) #pokud nejde rovnou, musíme převést na datum
data['Month'] = data['Date'].dt.month
data['Date'].dt.date

teplota=data['Temperature'].values
srazky=data['Precipitation'].values
rychlost_vetru=data['WindSpeed'].values

moznosti_dat = ["Vše"] + list(range(1, 13)) #výběr měsíce
selected_month = st.sidebar.selectbox("Vyberte měsíc", moznosti_dat)

moznosti_promenne=["Vše","Temperature", "Precipitation","WindSpeed"] #výběr proměnné
variable = st.sidebar.selectbox("Vyberte proměnnou",moznosti_promenne)

# Titulek aplikace
st.title("Analýza dat 16.02.2025")
st.subheader("Přehled")

# Výběr  měsíce
if selected_month == 'Vše':
    data_filtered = data # Filtrování podle měsíce
else:
    data_filtered = data[data['Month'] == selected_month] # Filtrování podle roku a měsíce

col1, col2=st.columns(2)
with col1:
# Boxplot
    st.subheader("Boxplot hodnot") 
    fig, ax= plt.subplots()
    if variable == 'Vše':
        df_boxplot = data_filtered[["Temperature", "Precipitation","WindSpeed"]].boxplot(ax=ax)
    else:
        data_filtered[[variable]].boxplot(ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Základní statistiky") # Základní statistiky                                               
#Data
    if variable == "Vše":
        st.write(data_filtered[["Temperature", "Precipitation","WindSpeed"]].describe())
    else:
        st.write(data_filtered[variable].describe())

# Liniový graf
st.subheader("Liniový graf")
fig, ax = plt.subplots()
ax.set_xlabel("Datum")
ax.set_ylabel(variable)
plt.xticks(rotation=45)
if variable == "Vše":
    ax.plot(data_filtered['Date'], data_filtered[["Temperature", "Precipitation","WindSpeed"]], marker='o', linestyle='-')   
else:
    ax.plot(data_filtered['Date'], data_filtered[variable], marker='o', linestyle='-')
st.pyplot(fig)
# Tabulka s daty
st.subheader("Tabulka s daty")
num_rows = st.number_input("Počet zobrazených řádků", min_value=1, max_value=len(data), value=5)
st.write(data_filtered.head(int(num_rows)))

# Výběr dne a zobrazení hodnot
st.subheader("Hodnoty pro vybraný den")
selected_day = st.date_input("Zvolte den k zobrazení", min_value=data_filtered['Date'].min(), max_value=data_filtered['Date'].max())
st.write(data_filtered[data_filtered['Date'] == selected_day])




# Min, max, průměr pro daný měsíc
st.subheader("Min, max, průměr pro daný měsíc")
if variable == "Vše":
    st.write(f"Minimální hodnota: {data_filtered[["Temperature", "Precipitation","WindSpeed"]].min()}")
    st.write(f"Maximální hodnota: {data_filtered[["Temperature", "Precipitation","WindSpeed"]].max()}")
    st.write(f"Průměrná hodnota: {data_filtered[["Temperature", "Precipitation","WindSpeed"]].mean()}")
else:
    min_val = data_filtered[variable].min()
    max_val = data_filtered[variable].max()
    mean_val = data_filtered[variable].mean()
    st.write(f"Minimální hodnota: {min_val}")
    st.write(f"Maximální hodnota: {max_val}")
    st.write(f"Průměrná hodnota: {mean_val}")







