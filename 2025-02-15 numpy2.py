import numpy as np
import pandas as pd

"""
1) vytvoření pole o 20 prvcích, kde jsou náhodné hodnoty z intevalu [-5,10)
2) vypsat prvních 5 prvků
3) vypsat posledních 5 prvků
4) vypsat každy druhý prvek
5) vypsat pouze sudé hodnoty
"""
arr = np.random.randint(-5,10,size=20)
print(arr)
print(arr[:5])
print(arr[-5:])
print(arr[1::2])
arr2 = arr[arr % 2 == 0]
print(arr)
#---------------------------------------------
#Live coding
"""
Load Weather Data into NumPy Arrays
Load the provided weather_data.csv file, which contains daily weather measurements (temperature, precipitation, wind speed) for a year, into a NumPy array.

Weather data is loaded into a NumPy array for analysis.
"""
data = pd.read_csv("sample_weather_data.csv")
print(data.head())

teplota=data['Temperature'].values
precipitation=data['Precipitation'].values
wind_speed=data['WindSpeed'].values
"""
Calculate Basic Statistical Measures
Compute basic statistical measures (mean, median, and standard deviation) for temperature, precipitation, and wind speed across the dataset.

Mean, median, and standard deviation for each weather measurement are computed using NumPy.
"""
priemer_t=np.mean(teplota) #priemer
median_t=np.median(teplota) #median
smer_t=np.std(teplota) #smerodatna odchylka

priemer_pr=np.mean(precipitation) #priemer
median_pr=np.median(precipitation) #median
smer_pr=np.std(precipitation) #smerodatna odchylka

priemer_ws=np.mean(wind_speed) #priemer
median_ws=np.median(wind_speed) #median
smer_ws=np.std(wind_speed) #smerodatna odchylka

import matplotlib.pyplot as plt
boxplot_data=pd.DataFrame({"teplota": teplota})
boxplot_data.boxplot(column="teplota")
plt.title("Boxplot pro teploty")
plt.show

#0. kvartil = 0. percentil = minimum
#1. kvartil = 25. percentil
#2. kvartil = 50. percentil = median
#3. kvartil = 75. percentil = median
#4. kvartil = 100. percentil = maximum

print(np.max(teplota))
print(np.min(teplota))
"""
Identify Extreme Weather Days
Use NumPy to identify days with extreme weather conditions. Define 'extreme' as temperatures above the 90th percentile or precipitation above the 95th percentile.

Days with extreme weather conditions are identified based on temperature and precipitation percentiles.
"""
teplota_90perc=np.percentile(teplota,90)
srazky_95perc=np.percentile(precipitation,95)

print(teplota_90perc)
print(srazky_95perc)

datum=data['Date'].values
print(datum)
data.head()

extremni_teplota=teplota>teplota_90perc
extremni_srazky=precipitation>srazky_95perc

extremni_hodnoty=extremni_teplota | extremni_srazky
extremni_dny=datum[extremni_hodnoty]

extremni_dny2=datum[(teplota>np.percentile(teplota,90)) | (precipitation>np.percentile(precipitation,95)) ]
print(extremni_dny)
print(extremni_dny2)

# normální dny
# vypsat dny, které mají teplotu mezi 25. a 75. percentilem nebo rychlost větru < 60. percentil

teplota_25perc=np.percentile(teplota,25)
teplota_75perc=np.percentile(teplota,75)
wind_speed_60=np.percentile(wind_speed,60)

normalni_teplota1=teplota>teplota_25perc
normalni_teplota2=teplota<teplota_75perc
normalni_vitr=wind_speed<wind_speed_60

normalni_dny=datum[(normalni_teplota1 & normalni_teplota2) | normalni_vitr]
print(normalni_dny)

"""
Analyze Wind Speed Patterns
Analyze wind speed data to find the month with the highest average wind speed. Additionally, calculate the variance in wind speed for each month.

Month with the highest average wind speed and monthly wind speed variances are calculated.
"""
data['Mesic']=data['Date'].dt.month
data.head()

mesicni_prumer_rychlosti_vetru=data.groupby('Mesic')['WindSpeed'].mean()
print(mesicni_prumer_rychlosti_vetru.idxmax())

#var() pro teplotu, zagrupujeme dle měsíce
#vytisknout měsíc s nejmenší rozptylem a hodnotu korespondující
mesicni_rozptyl_teploty=data.groupby('Mesic')['Temperature'].var()
print(f"Nejmenší rozptyl je {mesicni_rozptyl_teploty.idxmin()}. měsíci a hodnota je {mesicni_rozptyl_teploty.min()}")

data['Rok']=data['Date'].dt.year
data.head()

mesicni_rozptyl_teploty=data.groupby(['Mesic','Rok'])['Temperature'].var()
print(mesicni_rozptyl_teploty)
print(f"Nejmenší rozptyl je {mesicni_rozptyl_teploty.idxmin()}. měsíci a hodnota je {mesicni_rozptyl_teploty.min()}")