
# Setup Flask Application

Panduan ini menjelaskan cara menyiapkan dan menjalankan aplikasi Python menggunakan Flask.

## Prasyarat

Sebelum memulai, pastikan Anda memiliki hal berikut:

- **Python 3.x** terinstal di sistem Anda. Anda dapat mengunduhnya dari [sini](https://www.python.org/downloads/).
- **PIP** (Package Installer for Python) terinstal. Biasanya, PIP sudah terinstal secara otomatis dengan Python.

## Langkah-langkah untuk Menjalankan Aplikasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan dan menjalankan aplikasi Flask Anda:

### 1. Clone Repository

Clone repository ke direktori lokal Anda. Gunakan perintah berikut:

```bash
git clone https://github.com/riskiputraalamzah/monolith-car-project.git

### 2. Masuk ke Direktori Proyek

Pindah ke direktori proyek yang baru saja Anda clone:

```bash
cd monolith-car-project
```

### 3. Membuat Virtual Environment

Sangat disarankan untuk membuat virtual environment untuk proyek Anda. Ini membantu mengelola dependensi proyek tanpa mengganggu sistem Python Anda.

```bash
python -m venv venv
```

### 4. Aktivasi Virtual Environment

Aktifkan virtual environment:

- **Untuk Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **Untuk macOS dan Linux:**

  ```bash
  source venv/bin/activate
  ```

### 5. Instal Dependensi

Instal dependensi yang diperlukan dengan menggunakan `pip`. Biasanya, dependensi proyek dicantumkan dalam file `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 6. Menjalankan Aplikasi

Setelah semua dependensi terinstal, Anda dapat menjalankan aplikasi Flask. Gunakan perintah berikut:

```bash
flask run
```

Secara default, aplikasi akan berjalan di `http://127.0.0.1:5000/`.

### 7. Mengakses Aplikasi

Buka browser Anda dan masukkan URL berikut untuk mengakses aplikasi:

```
http://127.0.0.1:5000/
```

## Catatan Tambahan

- Pastikan untuk mengatur variabel lingkungan jika diperlukan. Anda mungkin perlu mengatur `FLASK_APP` dan `FLASK_ENV`. Contoh:

  ```bash
  export FLASK_APP=app.py
  export FLASK_ENV=development
  ```

- Untuk menghentikan aplikasi, tekan `CTRL + C` di terminal.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan fork repository ini dan kirim pull request.

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
