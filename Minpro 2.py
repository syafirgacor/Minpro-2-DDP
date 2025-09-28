# NAMA = SYAFIR AHZAMI
# NIM  = 2509116074


from prettytable import PrettyTable
from stdiomask import getpass

data_hewan = [
    {"Nama": "Jerapah", "Spesies": "Masai", "Kelamin": "Cowo", "Tahun Ditambahkan": 2020},
    {"Nama": "Zebra", "Spesies": "Gunung", "Kelamin": "Cewe", "Tahun Ditambahkan": 2021},
    {"Nama": "Harimau", "Spesies": "Sumatra", "Kelamin": "Cewe", "Tahun Ditambahkan": 2022},
    {"Nama": "Orangutan", "Spesies": "Kalimantan", "Kelamin": "Cowo", "Tahun Ditambahkan": 2021},
    {"Nama": "Panda", "Spesies": "Raksasa", "Kelamin": "Cewe", "Tahun Ditambahkan": 2023}
]

def list_hewan():
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Spesies", "Kelamin", "Tahun Ditambahkan"]
    for Hewan in data_hewan:
        tabel.add_row([Hewan["Nama"], Hewan["Spesies"], Hewan["Kelamin"], Hewan["Tahun Ditambahkan"]])
    print(tabel)


def tambah_hewan():
    print("Tambahkan hewan...")
    while True:
        Nama = input("Masukkan nama hewan: ")
        if Nama:
            break
        print("Nama tidak boleh kosong!")
    while True:
        Spesies = input("Masukkan spesies hewan: ")
        if Spesies: 
            break
        print("Spesies tidak boleh kosong!")
    kelamin_valid = ["Cowo", "Cewe"]
    while True:
        kelamin = input("Masukkan kelamin hewan (Cowo/Cewe): ").strip().title()
        if kelamin in kelamin_valid:
            break
        print("Input kelamin tidak valid. Silakan masukkan 'Cowo' atau 'Cewe'.")
    while True:
        try:
            Tahun_Ditambahkan = int(input("Masukkan tahun ditambahkan: ").strip())
            if Tahun_Ditambahkan > 0:  
                break
        except ValueError:
            print("Tolong masukkan angka yang valid.") 
    data_hewan.append({"Nama": Nama, "Spesies": Spesies, "Kelamin": kelamin, "Tahun Ditambahkan": Tahun_Ditambahkan})
    print("Berhasil menambahkan")
    list_hewan()

def edit_hewan():
    print("Edit hewan...")
    list_hewan() 
    nama_hewan = input("Masukkan nama hewan yang ingin diedit: ")

    for Hewan in data_hewan:
        if Hewan["Nama"].lower() == nama_hewan.lower():
            print("Masukkan data baru (biarkan kosong jika tidak ingin mengubah):")
            new_nama = input(f"Nama ({Hewan['Nama']}): ") or Hewan['Nama']
            new_spesies = input(f"Spesies ({Hewan['Spesies']}): ") or Hewan['Spesies']
            new_kelamin = input(f"Kelamin ({Hewan['Kelamin']}): ") or Hewan['Kelamin']
            new_tahun = input(f"Tahun Ditambahkan ({Hewan['Tahun Ditambahkan']}): ") or Hewan['Tahun Ditambahkan']

            Hewan.update({"Nama": new_nama, "Spesies": new_spesies, "Kelamin": new_kelamin, "Tahun Ditambahkan": new_tahun})
            print(f"Hewan {nama_hewan} berhasil diperbarui.")
            return 
    print(f"Hewan {nama_hewan} tidak ditemukan.")

def hapus_hewan():
    print("Hapus hewan...")
    list_hewan() 
    nama_hewan = input("Masukkan nama hewan yang ingin dihapus: ")
    if not nama_hewan:
        print("Nama hewan tidak boleh kosong.")
        return

    for Hewan in data_hewan:
        if Hewan["Nama"].lower() == nama_hewan.lower():
            data_hewan.remove(Hewan)
            print(f"Hewan {nama_hewan} berhasil dihapus.")
            return 
    print(f"Hewan {nama_hewan} tidak ditemukan.")

def logout():
    print("Logout berhasil... Kembali ke menu utama.")

def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        menu_utama_pilihan = [
            {"Nomor": "1", "Pilihan": "Login"}, 
            {"Nomor": "2", "Pilihan": "Keluar Program"},
        ]
        tabel = PrettyTable()
        tabel.field_names = ["Nomor", "Pilihan"]
        for menu in menu_utama_pilihan:
            tabel.add_row([menu["Nomor"], menu["Pilihan"]])
        print(tabel)

        pilihan_utama = input("Pilih opsi (1-2): ").strip()

        if pilihan_utama == '1':
            username = input("Masukkan username: ")
            password = getpass("Masukkan password: ")

            if username == "admin" and password == "password":
                print("Selamat datang admin!")
                while True:
                    menu_pilihan = [
                        {"Nomor": "1", "Pilihan": "Tambah hewan"}, 
                        {"Nomor": "2", "Pilihan": "List hewan"},  
                        {"Nomor": "3", "Pilihan": "Edit hewan"},
                        {"Nomor": "4", "Pilihan": "Hapus hewan"}, 
                        {"Nomor": "5", "Pilihan": "Logout"},
                    ]
                    tabel = PrettyTable()
                    tabel.field_names = ["Nomor", "Pilihan"]
                    for menu in menu_pilihan:
                        tabel.add_row([menu["Nomor"], menu["Pilihan"]])
                    print(tabel)

                    pilihan = input("Pilih opsi (1-5): ").strip()

                    if pilihan == '1':
                        tambah_hewan()
                    elif pilihan == '2':
                        list_hewan()
                    elif pilihan == '3':
                        edit_hewan()
                    elif pilihan == '4':
                        hapus_hewan()
                    elif pilihan == '5':
                        logout()
                        break
                    else:
                        print("Opsi tidak valid! Silahkan pilih antara 1-5.")

            elif username == 'pengunjung' and password == 'password':
                print("Selamat datang pengunjung!")
                while True:
                    print("\nMenu Pengunjung:")
                    print("1. Lihat List Hewan")
                    print("2. Logout")
                    
                    pilihan = input("Pilih opsi (1-2): ").strip()

                    if pilihan == '1':
                        list_hewan()
                    elif pilihan == '2':
                        logout()
                        break
                    else:
                        print("Opsi tidak valid! Silahkan pilih antara 1 dan 2.")
            else:
                print("Login tidak valid! Coba lagi.")
                continue

        elif pilihan_utama == '2':
            print("Terima kasih! Program dihentikan.")
            break
        else:
            print("Opsi tidak valid! Silahkan pilih 1 atau 2.")

menu_utama()