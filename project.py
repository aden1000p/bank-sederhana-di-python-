import os
# MEMBUAT BANK SEDERHANA 
# 1. MEMBUAT DATA BANK 
# 2. MEMASUKAN KODE AKUN BANK 
# 3. MENAMPILKAN SALDO
# 4. MENTRANSFERKAN SALDO
# 5. MEMNAMBAHKAN ISI SALDO 
# 6. MENGAMBIL SALDO
# 7. KELUAR

# OPSIONALNYA
# 1. BUATLAH HASIL PAJAK DARI MENGAMBIL DAN MENTRANSFERKAN SALDO
# 2. TAMPILKAN PERINGKAT SALDO TERBANYAK 
# 3. BUATLAH DATA BARU DARI BANK 
# 4. ISI SENDIRI 

data_Bank = {
    '099880':{'nama':'fadly', 'harga':10_000_000},
    '987654':{'nama':'agus', 'harga':10_000_000}
}

menu = ['Tampilkan saldo', 'Transfer Saldo', 'Menambahkan saldo', 'mengambil saldo', 'menambahkan data baru', 'keluar']

data_sort = []

def baris(n):
    print("=" * n)

def tampilkan_saldo(key):
    global data_Bank
    if data_Bank[key]:
        for x, y in data_Bank[key].items():
            print(f"{x}: {y}")


def transfer_saldo(key, penerima, jumlah):
    global data_Bank
    if data_Bank[key]:
        data_Bank[penerima]['harga'] += jumlah
        data_Bank[key]['harga'] -= jumlah
        
        return f"isi saldo kamu yang atas nama {data_Bank[key]['nama']} adalah {data_Bank[key]['harga']}"

def menambahkan_saldo(key, jumlah):
    global data_Bank
    if data_Bank[key]:
        data_Bank[key]['harga'] += jumlah
        return f"sekarang nilai saldo dari jumlah {jumlah} = {data_Bank[key]['harga']}"

def mengambil_saldo(key, jumlah):
    global data_Bank
    if data_Bank[key]:
        data_Bank[key]['harga'] -= jumlah
        return f"sekarang nilai saldo yang diambil dari {jumlah} = {data_Bank[key]['harga']}"

os.system('cls')


while True:
    baris = lambda x: '=' * x
    kode_verifikasi = input("masukan kode yang ada: ")
    
    
    
    try:     
        if data_Bank[kode_verifikasi]:
            for i in range(len(menu)):
                baris(30)
                if i == 3:
                        print("hallo selamat datang", data_Bank[kode_verifikasi]['nama'], "di bank dunia sederhana ")
                        for index, x in enumerate(menu):
                            print(f'{index + 1} {x}')
                        
                        pilihan = input("pilih opsi: ")
                        
                        if pilihan == "1":
                            tampilkan_saldo(kode_verifikasi)
                        elif pilihan == "2":
                            penerima = input('tentukan  penerima dari data banknya dengan kode verifikasi: ')
                            jumlah = int(input("masukan jumlah: "))
                            print(transfer_saldo(kode_verifikasi, penerima, jumlah))
                        elif pilihan == "3":
                            jumlah = int(input("masukan jumlah uang: "))
                            print(menambahkan_saldo(kode_verifikasi, jumlah))
                        elif pilihan == "4":
                            jumlah = int(input("masukan jumlah saldo: "))
                            print(mengambil_saldo(kode_verifikasi, jumlah))

                           
                        elif pilihan == "5":
                            break
    except KeyError:
        for i in range(1):
            key = input("masukan hash key: ")
            nama = input("masukan nama: ")
            harga = input("masukan harga yang diinput: ")
            data_Bank[key] = {'nama':nama, 'harga': harga}
        print("data telah ditambahkan ")


print("program selesai")