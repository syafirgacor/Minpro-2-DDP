# Mini Project: Sistem Manajemen Hewan (CRUD dengan Role-Based Access)

## Deskripsi
Program Python sederhana ini menerapkan operasi CRUD (Create, Read, Update, Delete) untuk mengelola data hewan di kebun binatang. Program menggunakan dictionary untuk menyimpan data, looping dan functions untuk navigasi menu, serta error handling untuk validasi input. Terdapat sistem login dengan dua role:
- **Admin**: Akses penuh (Tambah, Lihat, Edit, Hapus hewan).
- **Pengunjung**: Hanya bisa melihat list hewan (Read-only).

- `PrettyTable`: Untuk tampilan tabel yang rapi.
- `stdiomask`: Untuk menyembunyikan input password.

## Flowchart
Berikut flowchart program yang menggambarkan alur utama (login, menu, CRUD):

<img width="2000" height="1270" alt="minpro2" src="https://github.com/user-attachments/assets/6e170abe-a741-4564-8f78-7176e0d65c49" />

## Fitur
- **Login System**: Validasi username/password.
- **CRUD Operations** (Admin only):
  - Create: Tambah hewan baru dengan validasi (nama, spesies, kelamin, tahun).
  - Read: Tampilkan list hewan dalam tabel.
  - Update: Edit data hewan existing.
  - Delete: Hapus hewan dengan konfirmasi.
- **Role Access**: Pengunjung hanya bisa lihat list.
- **Error Handling**: Validasi input (e.g., tahun harus integer >0, kelamin hanya "Cowo"/"Cewe").


## Screenshot Output Terminal
### 1. Menu Utama dan Login Admin
<img width="1394" height="953" alt="Screenshot 2025-09-28 185824" src="https://github.com/user-attachments/assets/8a6b7f38-ef71-402d-b84a-0646af836032" />

saat run program akan muncul menu utama dan jika memilih pilihan 1 akan muncul output untuk menginput password dan username

### 2. Menu Admin
<img width="1406" height="605" alt="Screenshot 2025-09-28 193952" src="https://github.com/user-attachments/assets/d5f1408f-93ef-4123-93e1-8f26124b538c" />

Jika kita memasukkan username dan password untuk admin, akan muncul output seperti diatas.

### 3. Tambah Hewan (Create)
<img width="1405" height="675" alt="Screenshot 2025-09-28 194911" src="https://github.com/user-attachments/assets/785ceba9-d112-4d83-83b2-9df42482c2c6" />

*(Pilihan 1 akan membuat kita bisa menambahkan hewan ke dalam list dengan mengisi output yang sudah diberikan. Saat selesai menambah hewan akan muncul output dari list2 hewan yang sudah ditambahkan.)*

### 4. List Hewan (Read)
<img width="1398" height="522" alt="Screenshot 2025-09-28 200623" src="https://github.com/user-attachments/assets/fcd3ceb5-fa79-4bd2-9169-1fed89557d7b" />

*(Pilihan ke 2 akan membuat output dari list hewan yang sudah di input)*

### 5. Edit Hewan (Update)
<img width="1394" height="737" alt="Screenshot 2025-09-28 201456" src="https://github.com/user-attachments/assets/555f2172-99c7-42ce-b273-406d110ff06d" />  

*(Pilihan ke 3 akan membuat admin dapat mengedit hewan dari list yang sudah disediakan.)*

### 6. Hapus Hewan (Delete)
<img width="1402" height="620" alt="Screenshot 2025-09-28 201724" src="https://github.com/user-attachments/assets/f53088a0-fe8e-4dae-ae40-1a9834622d0b" />

*(Pilihan ke 4 membuat admin dapat menghapus seekor hewan dari list hewan yang sudah disediakan.)*

### 7. Log-out
  <img width="1399" height="514" alt="Screenshot 2025-09-28 201811" src="https://github.com/user-attachments/assets/fe289abd-afc1-432f-9e84-d639af746627" />

*(Pilihan ke 4 akan membuat admin kembali ke menu utama)*

### 8. Login Pengunjung
<img width="1412" height="448" alt="Screenshot 2025-09-28 202333" src="https://github.com/user-attachments/assets/ef012a0a-0d24-4c8e-b922-a0be3dbf7447" />

*(Selanjutnya jika kita login sebagai pengunjung, hanya akan muncul ouput 2 pilihan yaitu lihat list hewan dan logout)*

### 9. Lihat List Hewan (Read)
<img width="1392" height="478" alt="Screenshot 2025-09-28 202455" src="https://github.com/user-attachments/assets/c7543eca-ded8-4f75-a488-64cb6308c8d0" />

*(Jika memilih pilihan 1 akan muncul output list hewan.)*

### 10.Log-out
<img width="1415" height="413" alt="Screenshot 2025-09-28 202648" src="https://github.com/user-attachments/assets/92152817-4bff-4f94-955e-7bf10ae33b1d" />

*(Jika memilih pilihan 2 akan dikembalikan lagi ke menu utama.)*


Terima kasih!
