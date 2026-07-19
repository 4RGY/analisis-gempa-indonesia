<h1 align="center">Analisis Data Gempa Terkini Indonesia 🌍</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Portfolio_Project-success?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Data_Source-BMKG_Open_Data-blue?style=flat-square" alt="Data Source">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

Proyek portofolio data analytics sederhana menggunakan Open Data BMKG (Badan Meteorologi, Klimatologi, dan Geofisika). Script ini secara otomatis mengambil data XML terbaru, mengubahnya menjadi format tabular (CSV), lalu melakukan analisis deskriptif.

---

## 🛠️ Stack Teknologi

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-ffffff?style=flat-square&logo=python&logoColor=black" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=python&logoColor=white" alt="Seaborn">
</p>

## 📈 Insight Utama (Berdasarkan 15 gempa terakhir)
<details>
  <summary><b>Klik untuk melihat detail insight</b></summary>
  <br>

- **Gempa Terbesar:** Terjadi dengan magnitudo **6.8 SR** di wilayah **196 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT** pada 26 Jun 2026 pukul 18:34:39 WIB.
- **Rata-rata Kekuatan:** Sekitar **5.66 SR**. Mayoritas gempa terkini berada di rentang menengah yang terpantau oleh sistem peringatan dini.
- **Rata-rata Kedalaman:** **51.87 km**. 
</details>

## 📊 Visualisasi Data

### 1. Distribusi Kekuatan Gempa (Magnitudo)
Melihat sebaran magnitudo dari data gempa terbaru.
![Distribusi Magnitudo](output/distribusi_magnitudo.png)

### 2. Hubungan Magnitudo vs Kedalaman
Mengetahui apakah ada korelasi antara besarnya gempa dengan kedalaman pusat gempanya. Semakin ke bawah pada grafik, pusat gempa semakin dalam.
![Magnitudo vs Kedalaman](output/magnitudo_vs_kedalaman.png)

## 📁 Struktur Folder
- `data/`: Berisi raw dataset `gempa_terkini.csv`.
- `output/`: Berisi hasil visualisasi.
- `analyze.py`: Script penarikan dan analisis data.
