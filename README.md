# Analisis Data Gempa Terkini Indonesia

Proyek portofolio data analytics sederhana menggunakan Open Data BMKG (Badan Meteorologi, Klimatologi, dan Geofisika). Script ini secara otomatis mengambil data XML terbaru, mengubahnya menjadi format tabular (CSV), lalu melakukan analisis deskriptif.

## Insight Utama (Berdasarkan 15 gempa terakhir)
- **Gempa Terbesar:** Terjadi dengan magnitudo **6.4 SR** di wilayah **221 km BaratLaut PULAUKARATUNG-SULUT** pada 05 Agu 2026 pukul 11:14:04 WIB.
- **Rata-rata Kekuatan:** Sekitar **5.53 SR**. Mayoritas gempa terkini berada di rentang menengah yang terpantau oleh sistem peringatan dini.
- **Rata-rata Kedalaman:** **19.33 km**. 

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
