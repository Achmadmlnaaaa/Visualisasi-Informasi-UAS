import pandas as pd
import matplotlib.pyplot as plt

# Langkah 3: Membaca data
data = pd.read_csv('data.csv')
fig = plt.figure()
# Langkah 4: Menghitung jumlah jenis usaha di setiap kecamatan
grouped_data = data.groupby(['wilayah', 'jenis_usaha']).size().unstack().fillna(0)


# Langkah 5: Membuat grafik
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
plt.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)
plt.xlabel('Wilayah')
plt.ylabel('Jumlah Usaha')
plt.ylim(0, 500)
plt.title('Sebaran Jenis Usaha di Setiap Wilayah')
plt.legend(title='Jenis Usaha', loc='upper right')
plt.xticks(rotation=0)
plt