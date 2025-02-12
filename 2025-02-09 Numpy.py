import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
print(np_array)

print(np_array.shape)  # Outputs: (5,)
print(np_array.size)   # Outputs: 5
print(np_array.dtype)  # Outputs: dtype('int32') or dtype('int64') depending on the platform

List1=[1, 2, 3, 4, 5]
result = np_array + 10 #ok

print(f"{result}")
result2 = List1 + 10 #error

element = np_array[2]    # Access the third element
sub_array = np_array[:3] # Access the first three elements
print(element, sub_array)

arange_array = np.arange(0, 10, 2) #Od, do, step(skok)
print(arange_array)

linspace_array = np.linspace(0, 1, 11)
print(linspace_array)

zeros_array = np.zeros((2,3))
print(zeros_array)

ones_array = np.ones((2,3))
print(ones_array)

full_array = np.full((4,4), 7)
print(full_array)

np_array = np.array([1, 4, 9, 16, 25])
sqrt_array = np.sqrt(np_array)
print(sqrt_array)

mean_val = np.mean(np_array)
print(mean_val)  # Outputs: 11.0

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a)
print(b)

product = np.dot(a, b) #matematická multiplikace dvou matic
print(product)
# Outputs:
# [[19 22]
#  [43 50]]

print(a*b) #programátorské násobení matic každý s každým

random_ints = np.random.randint(low=1, high=10, size=5)
print(random_ints)

np_array = np.arange(10, 20)
print(np_array)
index_array = np.array([3, 5, 7])
print(np_array[index_array])

bool_index = np_array > 15
print(bool_index)
print(np_array[bool_index>15])  # Outputs: [16 17 18 19]

print(np_array[np_array>15]) 

total_sum = np.sum(np_array)
print(total_sum)  # Outputs: 145

print(np.nan)
np_array_with_nan = np.array([1, "NaN", 3, 4, np.nan])

filtered_array = np_array_with_nan[~np.isnan(np_array_with_nan)]
print(filtered_array)  # Outputs: [1. 3. 4.]

filled_array = np.nan_to_num(np_array_with_nan, nan=0)
print(filled_array)  # Outputs: [1. 0. 3. 4. 0.]

sales_data = np.random.randint(100, 500, size=(5, 12))
print(sales_data)

print(np.sum(sales_data))
product_totals = np.sum(sales_data, axis=1)
print(product_totals)

high_selling_products = sales_data[product_totals > 3000]
print(high_selling_products)

a = np.array([1, 2, 3])
b = 2
print(a * b)   # Scalar `b` is broadcast to match the shape of `a`

a_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')  # C order
a_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')  # Fortran order
print(a_c)

print(a_f)

#---------------------------------------------------
import numpy as np
import pandas as pd

data=pd.read_csv("sample_weather_data.csv")
data.head()

teplota=np.array(data.values)
print(teplota)

