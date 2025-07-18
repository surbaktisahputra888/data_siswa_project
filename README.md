# 📊 Data Siswa Project

Aplikasi web sederhana berbasis **Flask** untuk mengelola dan memvisualisasikan data nilai siswa. Cocok sebagai project portfolio Python untuk menunjukkan pemahaman database, web, dan data visualization.



## ✨ Fitur Utama

1. ✅ Tambah, edit, hapus data siswa
2. ✅ Hitung predikat & status kelulusan otomatis
3. ✅ Filter siswa berdasarkan:
   - Nama (pencarian)
   - Nilai (urutan naik/turun)
   - Predikat (A/B/C/D)
   - Status kelulusan (Lulus/Tidak Lulus)
4. ✅ Ekspor ke **Excel** & **PDF**
5. ✅ Visualisasi data predikat dengan **Chart.js**
6. ✅ Login sistem sederhana
7. ✅ Flash message untuk feedback pengguna



## ⚙️ Teknologi yang Digunakan

| Komponen     | Teknologi     |
| ------------ | ------------- |
| Backend      | Python, Flask |
| Database     | SQLite        |
| Visualisasi  | Chart.js      |
| Ekspor File  | Pandas, FPDF  |
| UI Framework | Bootstrap 5   |



## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Project

```bash
git clone https://github.com/surbaktisahputra888/data_siswa_project.git
cd data_siswa_project
```

### 2. (Opsional) Aktifkan Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# atau
source venv/bin/activate     # macOS/Linux
```

### 3. Install Library

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Login Default


Username: admin
Password: 123
```



## 📂 Struktur Folder


data_siswa_project/
├── app.py
├── data_siswa.db
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── edit.html
│   ├── login.html
│   └── grafik.html
└── static/            # (optional, jika ada tambahan CSS/JS)
```



## 🧑‍💻 Author

**Sahputra Surbakti**\
Project ini dibuat sebagai latihan mandiri dan untuk portfolio kerja.\
Silakan fork & kembangkan sendiri. 🚀



## 📄 Lisensi

Tidak menggunakan lisensi khusus. Bebas digunakan untuk belajar atau pengembangan pribadi.