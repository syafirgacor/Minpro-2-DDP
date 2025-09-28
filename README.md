# Mini Project: Sistem Manajemen Hewan (CRUD dengan Role-Based Access)

## Deskripsi
Program Python sederhana ini menerapkan operasi CRUD (Create, Read, Update, Delete) untuk mengelola data hewan di kebun binatang. Program menggunakan dictionary untuk menyimpan data, looping dan functions untuk navigasi menu, serta error handling untuk validasi input. Terdapat sistem login dengan dua role:
- **Admin**: Akses penuh (Tambah, Lihat, Edit, Hapus hewan).
- **Pengunjung**: Hanya bisa melihat list hewan (Read-only).

Data disimpan in-memory (array of dictionaries). Library bonus:
- `PrettyTable`: Untuk tampilan tabel yang rapi.
- `stdiomask`: Untuk menyembunyikan input password.

## Persyaratan Sistem
- Python 3.x
- Library: `prettytable`, `stdiomask` (install via `pip install prettytable stdiomask`)

## Cara Menjalankan
1. Clone repo: `git clone https://github.com/yourusername/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt` (buat file ini dengan isi: prettytable\nstdiomask)
3. Jalankan: `python main.py` (ganti dengan nama file Anda)
4. Login:
   - Admin: username `admin`, password `password`
   - Pengunjung: username `pengunjung`, password `password`

## Fitur
- **Login System**: Validasi username/password.
- **CRUD Operations** (Admin only):
  - Create: Tambah hewan baru dengan validasi (nama, spesies, kelamin, tahun).
  - Read: Tampilkan list hewan dalam tabel.
  - Update: Edit data hewan existing.
  - Delete: Hapus hewan dengan konfirmasi.
- **Role Access**: Pengunjung hanya bisa lihat list.
- **Error Handling**: Validasi input (e.g., tahun harus integer >0, kelamin hanya "Cowo"/"Cewe").

## Flowchart
Berikut flowchart program yang menggambarkan alur utama (login, menu, CRUD):

![Flowchart](flowchart.png)  
*(Penjelasan: Mulai dari Menu Utama → Login (branch ke Admin/Pengunjung/Error) → Menu Role-specific → CRUD Functions → Logout/Keluar. Error handling ditangani di setiap input.)*

## Screenshot Output Terminal
### 1. Menu Utama dan Login Admin
![Menu Utama](screenshots/menu_utama.png)  
*(Tampilan: Tabel menu, input login berhasil untuk admin.)*

### 2. Menu Admin dan List Hewan
![Menu Admin](screenshots/menu_admin.png)  
*(Tampilan: Tabel menu admin, output list hewan menggunakan PrettyTable.)*

### 3. Tambah Hewan (Create)
![Tambah Hewan](screenshots/tambah_hewan.png)  
*(Tampilan: Input validasi, tabel updated setelah tambah.)*

### 4. Edit Hewan (Update)
![Edit Hewan](screenshots/edit_hewan.png)  
*(Tampilan: Cari nama, input baru, tabel updated. Error jika tahun invalid.)*

### 5. Hapus Hewan (Delete)
![Hapus Hewan](screenshots/hapus_hewan.png)  
*(Tampilan: Konfirmasi y/n, tabel updated setelah hapus.)*

### 6. Menu Pengunjung (Read-Only)
![Menu Pengunjung](screenshots/menu_pengunjung.png)  
*(Tampilan: Tabel menu sederhana, hanya list hewan. Logout kembali ke utama.)*

### 7. Error Handling (Invalid Login/Input)
![Error Example](screenshots/error_login.png)  
*(Tampilan: Pesan error untuk login salah atau input tidak valid, e.g., tahun non-numeric.)*

## Struktur Kode
- `data_hewan`: List dictionary untuk data.
- Functions: `list_hewan()` (Read), `tambah_hewan()` (Create), `edit_hewan()` (Update), `hapus_hewan()` (Delete), `menu_utama()` (Main loop).
- Error Handling: Try-except untuk int conversion, while loops untuk validasi.

## Keterbatasan dan Perbaikan Masa Depan
- Data hilang saat program ditutup (bisa ditambah JSON persistence).
- Password hardcoded (bisa gunakan hashing untuk security).
- UI lebih advanced (e.g., GUI dengan Tkinter).

## Repository Link
https://github.com/yourusername/your-repo (ganti dengan link repo Anda).

Terima kasih!
