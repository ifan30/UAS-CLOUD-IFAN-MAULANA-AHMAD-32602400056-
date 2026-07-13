# UAS-CLOUD

UAS-CLOUD adalah aplikasi web berbasis Flask untuk manajemen pembuatan dan simulasi penyimpanan CV di lingkungan lokal yang meniru AWS S3. Aplikasi ini mendukung login admin, pembuatan CV, penyimpanan dokumen teks ke folder simulasi bucket, dan pengelolaan daftar CV.

## Fitur Utama

- Login admin dengan kredensial statis
- Dashboard menampilkan jumlah CV dan statistik pendidikan
- Form input CV untuk nama, email, nomor HP, pendidikan, dan tema desain
- Simulasi penyimpanan objek AWS S3 menggunakan folder lokal `simulasi_s3_bucket`
- Daftar CV dengan pencarian, unduhan, dan penghapusan objek

## Struktur Proyek

- `app_web.py` - entrypoint aplikasi Flask
- `core/config.py` - konfigurasi aplikasi dan pembuatan folder simulasi bucket
- `core/database.py` - data pengguna dan penyimpanan CV sementara
- `core/services.py` - layanan simpan, baca, dan hapus objek CV
- `routes/auth.py` - route otentikasi, login, dan logout
- `routes/cv.py` - route dashboard, pembuatan CV, daftar, unduhan, dan hapus
- `templates/` - halaman HTML untuk login, dashboard, pembuatan CV, dan daftar CV

## Teknologi

- Python 3.x
- Flask
- HTML + Tailwind CSS via CDN

## Persyaratan

1. Python 3.8+ terpasang
2. `pip` tersedia di sistem
3. Akses terminal / PowerShell

## Instalasi dan Jalankan (Windows)

### 1. Buka terminal di folder proyek

Buka PowerShell atau Command Prompt, lalu pindah ke folder proyek:

```powershell
cd "c:\Users\Lenovo\OneDrive\TUGAS\uas-cloud"
```

### 2. Buat virtual environment

Gunakan perintah berikut untuk membuat environment isolasi:

```powershell
python -m venv venv
```

Jika perintah `python` tidak ditemukan, coba `py -3 -m venv venv`.

### 3. Aktifkan virtual environment

Jalankan:

```powershell
venv\Scripts\Activate.ps1
```

Jika PowerShell menolak menjalankan skrip, jalankan sebagai administrator atau izinkan eksekusi sementara:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

Setelah aktif, prompt akan berubah menjadi `(venv)`.

### 4. Install dependensi

Di dalam virtual environment, install Flask:

```powershell
pip install Flask
```

### 5. Verifikasi instalasi

Pastikan Flask terpasang dan Python mengenali package:

```powershell
python -c "import flask; print(flask.__version__)"
```

Jika tidak ada error, instalasi berhasil.

### 6. Jalankan aplikasi

Masih di folder proyek, jalankan:

```powershell
python app_web.py
```

Aplikasi akan berjalan di mode debug dan terbuka pada port 5000.

### 7. Buka aplikasi di browser

Akses URL berikut di browser:

```text
http://127.0.0.1:5000/
```

## Akun Default

- Email: `admin@gmail.com`
- Password: `12345`

## Penggunaan Aplikasi

1. Login dengan akun default.
2. Di dashboard, lihat ringkasan CV dan statistik pendidikan.
3. Gunakan menu "Buat CV Baru" untuk membuat CV baru.
4. Data CV akan disimpan sebagai file teks di folder lokal `simulasi_s3_bucket`.
5. Gunakan menu "Direktori S3" untuk melihat semua CV, unduh, atau hapus objek.

## Direktori Simulasi S3

- Folder `simulasi_s3_bucket` dibuat otomatis oleh `core/config.py`
- File CV disimpan sebagai teks di folder ini sebagai simulasi bucket S3
- Menghapus CV di aplikasi juga menghapus file di folder ini

## Catatan Penting

- Data CV ditampung sementara di memori (`CV_DATABASE`) selama runtime.
- Aplikasi ini cocok untuk demonstrasi dan tugas, bukan untuk produksi.
- Jika ingin menghentikan aplikasi, tekan `Ctrl+C` di terminal.

## Lisensi

Disesuaikan untuk tugas UAS dan penggunaan akademis.