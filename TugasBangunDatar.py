# Tugas PBO : Menghitung luas bidang datar
# 1. Persegi
# 2. Lingkaran
# 3. Segitiga

# Nama  : Fyan Ramadhan
# NIM   : D0221090
# Kelas : Teknik Informatika F

def enter():
    print('\n')
    
def garis1():
    print('-'*42)
    
def garis2():
    print('='*42)

def persegi():
    # rumus dari persegi adalah sisi * sisi
    while True:
        enter()
        garis1()
        print("Menu Menghitung Luas Persegi".center(42,' '))
        garis1()
        sisi = float(input("Masukkan Panjang Sisi Persegi :"))
        luaspersegi = sisi * sisi
        print(f"Luas Persegi yang memiliki sisi {sisi} Cm adalah {luaspersegi} cm^2")
        lanjut = input("Lanjut Y/N :").upper()
        if lanjut == 'Y' :
            pass
        else :
            break
        
def lingkaran():
    # Rumus menghitung Luas Lingkaran adalah 22/7 * r * r atau 3.14 * r * r
    # Jika jari - jari Lingkaran adalah kelipatan 7 maka menggunakan phi 22/7
    #  sedangkan jika bukan kelipatan dari 7 maka menggunakan 3.14
    while True:
        enter()
        garis1()
        print("Menu Menghitung Luas Lingkaran".center(42,' '))
        garis1()
        phi1 = 22/7
        phi2 = 3.14
        r = float(input("Masukkan Jari - Jari : "))
        if r%7 == 0 :
            luasLingkaran = phi1 * r * r 
        else :
            luasLingkaran = phi2 * r * r 
        print("Luas Lingkaran adalah", luasLingkaran, "Cm^2")
        lanjut = input("Lanjut Y/N :").upper()
        if lanjut == 'Y' :
            pass
        else :
            break
        
def segitiga():
    # Rumus Menghitung Luas Segitiga adalah 1/2 * alas * tinggi
    while True:
        enter()
        garis1()
        print("Menu Menghitung Luas Segitiga".center(42,' '))
        garis1()
        alas = float(input("Masukkan Panjang Alas : "))
        tinggi = float(input("Masukkan Tinggi : "))
        luassegitiga = 1/2 * alas * tinggi
        print("Luas Segitiga adalah : ", luassegitiga, "cm^2")
        lanjut = input("Lanjut Y/N :").upper()        
        if lanjut == 'Y' :
            pass
        else :
            break

while True :
    menu = ["\t1. Menghitung Luas Persegi","\t2. Menghitung Luas Lingkaran","\t3. Menghitung Luas Segitiga", "\t4. Keluar"]
        
    garis2()
    print("Program Menghitung Luas Bidang Datar".center(42,' '))
    garis2()

    print("Select Menu")
    for i in menu:
        print(i)
    enter()
    pilihan = input("Masukkan kode Menu Piihan : ")
    if pilihan == '1':
        persegi()
    elif pilihan == '2':
        lingkaran()
    elif pilihan == '3':
        segitiga()
    else :
        break
