#nama : Fyan Ramadhan
#nim : D0221090
#kelas : Informatika F

class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi) :
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class Lingkaran(BangunDatar):
    def __init__(self,jari2):
        self.jari2 = jari2
        if self.jari2%7 == 0 :
            self.phi = 22/7
        else :
            self.phi = 3.14
        

    def luas(self):
        return self.phi * (self.jari2**2)

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3

class Limas(BangunRuang):
    def __init__(self,panjang_alas,tinggi_alas,tinggi_limas):
        self.panjang_alas = panjang_alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas

    def volume(self):
        return (self.panjang_alas*self.tinggi_alas/2) * self.tinggi_limas / 3

class Tabung(BangunRuang):
    def __init__(self,jari2,tinggi):
        self.jari2 = jari2
        self.tinggi = tinggi
        if self.jari2%7 == 0 :
            self.phi = 22/7
        else :
            self.phi = 3.14

    def volume(self):
        return self.phi * (self.jari2**2) * self.tinggi

def menu_bangundatar():
    while True : 
        print("="*40)
        print(" Menu Bangun Datar ".center(40,"="))
        print("="*40)
        print('''1. persegi
2. segitiga
3. lingkaran
4. kembali''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            print("menghitung luas persegi")
            sisi = int(input("masukkan panjang sisi : "))
            persegi = Persegi(sisi)
            print("luas persegi = ",persegi.luas()) 
        elif pilihan == 2 : 
            print("menghitung luas segitiga")
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi = int(input("masukkan panjang tinggi segitiga : "))
            segitiga = Segitiga(alas,tinggi)
            print("luas segitiga = ",segitiga.luas())
        elif pilihan == 3 : 
            print("menghitung luas lingkaran")
            jari2 = int(input("masukkan panjang jari-jari : "))
            lingkaran = Lingkaran(jari2)
            print("luas lingkaran = ",int(lingkaran.luas()))
        elif pilihan == 4 : 
            break
        else : 
            print("masukkan kode menu dengan benar!")


def menu_bangunruang():
    while True : 
        print("="*40)
        print(" Menu Bangun Ruang ".center(40,"="))
        print("="*40)
        print('''1. kubus
2. limas segitiga
3. tabung
4. kembali
''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            print(" Menghitung volume Kubus ".center(40,"="))
            sisi = int(input("masukkan panjang sisi : "))
            kubus = Kubus(sisi)
            print("volume kubus = ",kubus.volume()) 
        elif pilihan == 2 : 
            print(" Menghitung volume Limas Segitiga".center(40,"="))
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi_alas = int(input("masukkan panjang tinggi alas segitiga : "))
            tinggi_limas = int(input("masukkan panjang tinggi limas : "))
            limas = Limas(alas,tinggi_alas,tinggi_limas)
            print("volume limas segitiga = ",limas.volume())
        elif pilihan == 3 : 
            print("Menghitung volume Tabung".center(40,"="))
            jari2 = int(input("masukkan panjang jari-jari : "))
            tinggi = int(input("masukkan tinggi tabung : "))
            tabung = Tabung(jari2,tinggi)
            print("volume tabung = ",int(tabung.volume()))
        elif pilihan == 4 : 
            break
        else : 
            print("masukkan kode menu dengan benar!")

def menu_program():
    while True :
        print("="*40)
        print(" SELAMAT DATANG ".center(40,"="))
        print("="*40)
        print(" PROGRAM SEDERHANA ".center(40," "))
        print(" Menghitung Luas dan Volume ".center(40," "))
        print("="*40)
        print('''1. Hitung Luas
2. Hitung Volume
3. Keluar''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            menu_bangundatar()
        elif pilihan == 2 : 
            menu_bangunruang()
        elif pilihan == 3 :
            break
        else : 
            print("masukkan pilihan dengan benar")

menu_program()