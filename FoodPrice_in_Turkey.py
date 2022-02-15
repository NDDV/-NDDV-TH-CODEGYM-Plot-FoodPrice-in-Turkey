#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("FoodPrice_in_Turkey.csv")
df_sorted = df.sort_values(['Month'],ascending=True)
df_sorted
#%%
#Vẽ biểu đồ cột so sánh giá gạo (Rice-Retail) tháng 12 năm 2019 của Ankara, Istanbul, Izmir và National Average.

df_RiceRetail = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Rice - Retail')]
df_RiceRetail.info()
plt.bar(df_RiceRetail['Place'],df_RiceRetail['Price'])
plt.show()
# %%
#Vẽ biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail) trung bình cả nước (National Average) trong năm 2019 tại Thổ Nhĩ Kì.

df_NationalAverage = df_sorted[(df_sorted['Place'] == 'National Average') & (df_sorted['Year'] == 2019) & (df_sorted['ProductName'] == 'Rice - Retail')]
df_NationalAverage
plt.plot(df_NationalAverage['Month'],df_NationalAverage['Price'],'--g')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()
# %%
#Vẽ biểu đồ Scatter phân tích mối liên quan giữa giá gạo và giá gas trung bình quốc gia (National Average) tại Thổ Nhĩ Kì.
x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]
plt.scatter(x['Price'], y['Price'])
plt.show()

# %%
