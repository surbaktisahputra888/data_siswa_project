from flask import Flask, render_template, request, redirect, url_for, flash, send_file, session
import sqlite3
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import io

app = Flask(__name__)
app.secret_key = 'secret_key_anda'

# --- Database Setup ---
def get_db():
    conn = sqlite3.connect('data_siswa.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                nilai INTEGER NOT NULL,
                predikat TEXT,
                status TEXT,
                waktu_input TEXT
            )
        ''')
init_db()

# --- Fungsi Utilitas ---
def hitung_predikat(nilai):
    if nilai >= 85:
        return "A", "Lulus"
    elif nilai >= 70:
        return "B", "Lulus"
    elif nilai >= 60:
        return "C", "Lulus"
    else:
        return "D", "Tidak Lulus"

# --- Routing ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    db = get_db()
    if request.method == 'POST':
        nama = request.form['nama']
        nilai = int(request.form['nilai'])
        predikat, status = hitung_predikat(nilai)
        waktu_input = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.execute('INSERT INTO siswa (nama, nilai, predikat, status, waktu_input) VALUES (?, ?, ?, ?, ?)',
                   (nama, nilai, predikat, status, waktu_input))
        db.commit()
        flash('Data siswa berhasil ditambahkan!')
        return redirect(url_for('index'))

    keyword = request.args.get('cari', '')
    filter_val = request.args.get('filter', '')
    filter_predikat = request.args.get('filter_predikat', '')
    sort = request.args.get('sort', '')

    query = 'SELECT * FROM siswa WHERE nama LIKE ?'
    params = [f'%{keyword}%']
    if filter_val == 'tidak_lulus':
        query += ' AND status = ?'
        params.append('Tidak Lulus')

    if filter_predikat:
        query += ' AND predikat = ?'
        params.append(filter_predikat)

    if sort == 'asc':
        query += ' ORDER BY nilai ASC'
    elif sort == 'desc':
        query += ' ORDER BY nilai DESC'

    siswa = db.execute(query, params).fetchall()

    # Ringkasan
    semua = db.execute('SELECT * FROM siswa').fetchall()
    tidak_lulus = len([s for s in semua if s['status'] == 'Tidak Lulus'])
    jumlah = len(semua)
    rata2 = round(sum([s['nilai'] for s in semua]) / jumlah, 2) if jumlah > 0 else 0
    tertinggi = max(semua, key=lambda x: x['nilai'], default=None)
    terendah = min(semua, key=lambda x: x['nilai'], default=None)

    return render_template('index.html', siswa=siswa, keyword=keyword,
                           filter_val=filter_val, filter_predikat=filter_predikat, sort=sort,
                           tidak_lulus=tidak_lulus, jumlah=jumlah, rata2=rata2,
                           tertinggi=tertinggi, terendah=terendah)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    db = get_db()
    siswa = db.execute('SELECT * FROM siswa WHERE id = ?', (id,)).fetchone()
    if not siswa:
        flash('Data tidak ditemukan!')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nama = request.form['nama']
        nilai = int(request.form['nilai'])
        predikat, status = hitung_predikat(nilai)
        db.execute('UPDATE siswa SET nama=?, nilai=?, predikat=?, status=? WHERE id=?',
                   (nama, nilai, predikat, status, id))
        db.commit()
        flash('Data siswa berhasil diupdate!')
        return redirect(url_for('index'))

    return render_template('edit.html', siswa=siswa)

@app.route('/hapus/<int:id>')
def hapus(id):
    db = get_db()
    db.execute('DELETE FROM siswa WHERE id = ?', (id,))
    db.commit()
    flash('Data siswa telah dihapus!')
    return redirect(url_for('index'))

@app.route('/hapus_semua')
def hapus_semua():
    db = get_db()
    db.execute('DELETE FROM siswa')
    db.commit()
    flash('Semua data berhasil dihapus!')
    return redirect(url_for('index'))

@app.route('/export_excel')
def export_excel():
    db = get_db()
    data = db.execute('SELECT * FROM siswa').fetchall()
    df = pd.DataFrame(data, columns=data[0].keys() if data else ['id','nama','nilai','predikat','status','waktu_input'])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Data Siswa')
    output.seek(0)
    return send_file(output, download_name="data_siswa.xlsx", as_attachment=True)

@app.route('/export_pdf')
def export_pdf():
    db = get_db()
    data = db.execute('SELECT * FROM siswa').fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Data Siswa", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 10)
    pdf.cell(10, 8, "No", 1)
    pdf.cell(40, 8, "Nama", 1)
    pdf.cell(20, 8, "Nilai", 1)
    pdf.cell(25, 8, "Predikat", 1)
    pdf.cell(25, 8, "Status", 1)
    pdf.cell(60, 8, "Waktu Input", 1)
    pdf.ln()

    pdf.set_font("Arial", '', 10)
    for i, s in enumerate(data, 1):
        pdf.cell(10, 8, str(i), 1)
        pdf.cell(40, 8, s['nama'], 1)
        pdf.cell(20, 8, str(s['nilai']), 1)
        pdf.cell(25, 8, s['predikat'], 1)
        pdf.cell(25, 8, s['status'], 1)
        pdf.cell(60, 8, s['waktu_input'], 1)
        pdf.ln()

    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return send_file(output, download_name="data_siswa.pdf", as_attachment=True)

@app.route('/grafik')
def grafik():
    db = get_db()
    data = db.execute('SELECT predikat, COUNT(*) as jumlah FROM siswa GROUP BY predikat').fetchall()

    predikat = [row[0] for row in data]
    jumlah = [row[1] for row in data]

    return render_template('grafik.html', predikat=predikat, jumlah=jumlah)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '123':
            session['logged_in'] = True
            flash('Login berhasil!')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout berhasil!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)