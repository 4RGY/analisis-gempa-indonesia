import pandas as pd
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Setup folder
Path('data').mkdir(exist_ok=True)
Path('output').mkdir(exist_ok=True)

print("Mengambil data dari BMKG...")
url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.xml"
response = requests.get(url)
root = ET.fromstring(response.content)

data = []
for gempa in root.findall('gempa'):
    data.append({
        'Tanggal': gempa.find('Tanggal').text,
        'Jam': gempa.find('Jam').text,
        'DateTime': gempa.find('DateTime').text,
        'Lintang': gempa.find('Lintang').text,
        'Bujur': gempa.find('Bujur').text,
        'Magnitude': float(gempa.find('Magnitude').text),
        'Kedalaman': gempa.find('Kedalaman').text,
        'Wilayah': gempa.find('Wilayah').text,
        'Potensi': gempa.find('Potensi').text
    })

df = pd.DataFrame(data)
df.to_csv('data/gempa_terkini.csv', index=False)
print(f"Berhasil menyimpan {len(df)} baris data gempa.")

# Cleansing
df['Kedalaman_km'] = df['Kedalaman'].str.replace(' km', '').str.replace(' Km', '').astype(float)

# Analisis & Insights
top_mag = df.loc[df['Magnitude'].idxmax()]
avg_mag = df['Magnitude'].mean()
avg_depth = df['Kedalaman_km'].mean()

# Visualisasi 1: Distribusi Magnitudo
plt.figure(figsize=(10, 6))
sns.histplot(df['Magnitude'], bins=10, kde=True, color='crimson')
plt.title('Distribusi Magnitudo Gempa Terkini di Indonesia', pad=15)
plt.xlabel('Magnitudo (SR)')
plt.ylabel('Jumlah Kejadian')
plt.grid(axis='y', alpha=0.3)
plt.savefig('output/distribusi_magnitudo.png', bbox_inches='tight')
plt.close()

# Visualisasi 2: Hubungan Kedalaman dan Magnitudo
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Magnitude', y='Kedalaman_km', data=df, color='darkblue', alpha=0.7, s=100)
plt.title('Hubungan Magnitudo dan Kedalaman Gempa', pad=15)
plt.xlabel('Magnitudo (SR)')
plt.ylabel('Kedalaman (km)')
plt.gca().invert_yaxis() # Kedalaman makin ke bawah makin dalam
plt.grid(True, alpha=0.3)
plt.savefig('output/magnitudo_vs_kedalaman.png', bbox_inches='tight')
plt.close()

# Bikin README
readme_content = f"""# Analisis Data Gempa Terkini Indonesia

Proyek portofolio data analytics sederhana menggunakan Open Data BMKG (Badan Meteorologi, Klimatologi, dan Geofisika). Script ini secara otomatis mengambil data XML terbaru, mengubahnya menjadi format tabular (CSV), lalu melakukan analisis deskriptif.

## Insight Utama (Berdasarkan {len(df)} gempa terakhir)
- **Gempa Terbesar:** Terjadi dengan magnitudo **{top_mag['Magnitude']} SR** di wilayah **{top_mag['Wilayah']}** pada {top_mag['Tanggal']} pukul {top_mag['Jam']}.
- **Rata-rata Kekuatan:** Sekitar **{avg_mag:.2f} SR**. Mayoritas gempa terkini berada di rentang menengah yang terpantau oleh sistem peringatan dini.
- **Rata-rata Kedalaman:** **{avg_depth:.2f} km**. 

## Visualisasi Data

### 1. Distribusi Kekuatan Gempa (Magnitudo)
Melihat sebaran magnitudo dari data gempa terbaru.
![Distribusi Magnitudo](output/distribusi_magnitudo.png)

### 2. Hubungan Magnitudo vs Kedalaman
Mengetahui apakah ada korelasi antara besarnya gempa dengan kedalaman pusat gempanya. Semakin ke bawah pada grafik, pusat gempa semakin dalam.
![Magnitudo vs Kedalaman](output/magnitudo_vs_kedalaman.png)

## Struktur Folder
- `data/`: Berisi raw dataset `gempa_terkini.csv`.
- `output/`: Berisi hasil visualisasi.
- `analyze.py`: Script penarikan dan analisis data.

## Stack Teknologi
- Python (Pandas, Requests, Matplotlib, Seaborn)
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Visualisasi dan README berhasil dibuat.")
