📋 Data Siswa App - Portfolio Project

Aplikasi sederhana berbasis Python Flask untuk mencatat data siswa dan mengevaluasi kelulusan berdasarkan nilai. Aplikasi ini mendukung input data, edit, hapus, filter, serta ekspor ke PDF dan Excel. Proyek ini cocok dijadikan sebagai portfolio untuk melamar kerja di bidang IT / Web Developer / Python Developer.

🚀 Fitur Utama

✅ Input nama dan nilai siswa

🧠 Penilaian otomatis (Predikat + Status kelulusan)

🔍 Fitur cari dan filter siswa tidak lulus

📊 Statistik ringkasan (jumlah, rata-rata, nilai tertinggi & terendah)

✏️ Edit dan hapus data siswa

📁 Ekspor ke Excel dan PDF

🗑️ Hapus semua data sekaligus

🧰 Teknologi yang Digunakan

Python 3

Flask (framework web)

SQLite (database ringan)

Pandas (untuk ekspor Excel)

FPDF (untuk ekspor PDF)

HTML + Bootstrap 5 (tampilan web)

🗂️ Struktur Proyek

data_siswa_project/
├── app.py
├── data_siswa.db
├── venv/ (opsional - virtual environment)
└── templates/
    ├── index.html
    └── edit.html

▶️ Cara Menjalankan

Aktifkan virtual environment:

python -m venv venv
venv\Scripts\activate   # (Windows)

Install dependencies:

pip install flask pandas fpdf

Jalankan aplikasi:

python app.py

Akses di browser:

http://localhost:5000

📸 Tampilan Aplikasi

Form input siswa

Tabel data siswa + tombol aksi

Statistik ringkasan

Tombol ekspor dan hapus semua

📌 Catatan

Predikat ditentukan otomatis:

Nilai ≥ 85 → A (Lulus)

Nilai ≥ 70 → B (Lulus)

Nilai ≥ 60 → C (Lulus)

Nilai < 60 → D (Tidak Lulus)

Ekspor file langsung dari browser

🙋‍♂️ Tentang Developer

Proyek ini dibuat sebagai latihan sekaligus portfolio oleh [Nama Kamu], seorang pembelajar Python yang sedang merintis karier di dunia IT. Dibimbing dan disusun bersama bantuan AI ChatGPT.

🧠 Lisensi

Free to use untuk pembelajaran, modifikasi, dan pengembangan.

📫 Ingin tahu lebih lanjut atau kerja sama? Hubungi saya via email: sahputrasurbakti888@gmail.com