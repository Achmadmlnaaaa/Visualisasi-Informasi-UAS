import pandas as pd
import matplotlib.pyplot as plt

# Langkah 3: Membaca data
data = pd.read_csv('data.csv')
# Langkah 4: Menghitung jumlah jenis usaha di setiap kecamatan
grouped_data = data.groupby(['kecamatan', 'wilayah']).size().unstack().fillna(0)


# Langkah 5: Membuat grafik
grouped_data.plot(kind='bar', stacked=True,figsize=(12, 6), )
plt.grid(which="major", axis='x', color='#DAD8D7', alpha=0.5, zorder=1)
plt.grid(which="major", axis='y', color='#DAD8D7', alpha=0.5, zorder=1)
plt.xlabel('Kecamatan')
plt.ylabel('Jumlah Usaha')
plt.title('Sebaran Kecamatan di Setiap Wilayah Berdasarkan Banyaknya Jenis Usaha')
plt.legend(title='Wilayah')
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.3, top=0.95)
plt