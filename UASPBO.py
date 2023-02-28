# class Hitung Luas
# Class Volume Lingkaran = Tabung, 
# Persegi = Kubus/Balok
# Segitiga = Limas Segitiga


class MenghitungLuas():
    def enter():
        print('\n')
        enter = input("Tekan ENTER :")
    def menu(namaBangun):
        print("\n")
        print("-"*40)
        print(f"Menghitung Luas {namaBangun}".center(40,' '))
        print("-"*40)
        if namaBangun == 'Persegi':
            sisi = float(input("Masukkan Sisi :"))
            MenghitungLuas.persegi(sisi)
            MenghitungLuas.enter()
            MenghitungLuas.start()
        elif namaBangun == 'Segitiga':
            a = float(input("Masukkan panjang Alas :")) 
            t = float(input("Masukkan Tinggi :"))
            MenghitungLuas.segitiga(a, t)
            MenghitungLuas.enter()
            MenghitungLuas.start()
        elif namaBangun == 'Lingkaran':
            r = float(input("Masukkan Jari - Jari :"))
            MenghitungLuas.lingkaran(r)
            MenghitungLuas.enter()
            MenghitungLuas.start()
        else:
            MenghitungLuas.start()
                
                
        
    def start():
        print("\n")
        print("-"*40)
        print("MENU".center(40, ' '))
        print("Menghitung Luas".center(40, ' '))
        print("-"*40)
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. kembali ke Menu")
        pilihmenu = input("Masukkan kode Menu :")
        if pilihmenu == '1':
            MenghitungLuas.menu("Persegi")
        elif pilihmenu == '2':
            MenghitungLuas.menu("Lingkaran")
        elif pilihmenu == '3':
            MenghitungLuas.menu("Segitiga")
        else:
            pass

    def persegi (input_sisi):
        luas = input_sisi * input_sisi
        print("Luas Persegi :", luas, 'Cm2')
    
    def lingkaran (r):
        if r%7 == 0 :
            phi = 22/7
        else :
            phi = 3.14    
        luas = phi * r**2
        print("Luas Lingkaran :", luas, 'Cm2')
        
    def segitiga (a, t):
        luas = 1/2 * a * t
        print("Luas Segitiga :", luas , 'Cm2')


class menghitungVolume():

    def enter():
        print('\n')
        enter = input("Tekan ENTER :")
        
    def menu(namaBangunRuang):
        print("\n")
        print("-"*40)
        print(f"Menghitung Volume {namaBangunRuang}".center(40,' '))
        print("-"*40)
        if namaBangunRuang == 'kubus':
            sisi = float(input("Masukkan Panjang Sisi :"))
            menghitungVolume.kubus(sisi)
            menghitungVolume.enter()
            menghitungVolume.start()
        elif namaBangunRuang == 'limasSegitiga':
            a = float(input("Masukkan panjang Alas :")) 
            ts = float(input("Masukkan Tinggi Alas :"))
            t = float(input("Masukkan Tinggi :"))
            menghitungVolume.limasSegitiga(a, ts, t)
            menghitungVolume.enter()
            menghitungVolume.start()
        elif namaBangunRuang == 'tabung':
            r = float(input("Masukkan Jari - Jari :"))
            t = float(input("Masukkan Tinggi Tabung :"))
            menghitungVolume.tabung(0, r, t)
            menghitungVolume.enter()
            menghitungVolume.start()
        else:
            pass
                
    
    def start():
        print("\n")
        print("-"*40)
        print("MENU".center(40, ' '))
        print("Menghitung Volume".center(40, ' '))
        print("-"*40)
        print("1. Kubus")
        print("2. Tabung")
        print("3. Limas Segitiga")
        print("4. kembali ke Menu")
        pilihmenu = input("Masukkan kode Menu :")
        if pilihmenu == '1':
            menghitungVolume.menu("kubus")
        elif pilihmenu == '2':
            menghitungVolume.menu("tabung")
        elif pilihmenu == '3':
            menghitungVolume.menu("limasSegitiga")
        else:
            pass
        
    def kubus(sisi):
        v = sisi **3
        print("Volume Kubus :", v , 'Cm3')
        # V = phi * r**2 * t
        
    def tabung(phi, r, t):
        if r%7 == 0 :
            phi = 22/7
        else :
            phi = 3.14    
        vol = phi * r**2 * t
        print("Volume dari Tabung :", vol, 'Cm3')
     
    # V = 1/3 * (luas alas * tinggi)
    #               Atau
    # V = 1/3 * (1/2 * a * ts * tinggi) 
    def limasSegitiga(a, ts, t):
        la = 1/2 * a * ts
        v = 1/3 * (la * t)
        print("Volume Limas :", v, 'Cm3')


while True :
    print('-'*40)
    print('PROGRAM SEDERHANA'.center(40,' '))
    print('Menghitung Luas dan Volume'.center(40,' '))
    print('-'*40)
    print("Input Menu")
    print("1. Menghitung Luas")
    print("2. Menghitung Volume")
    print("3. Exit Program")
    menu = input("Masukkan Kode Menu :")
    if menu == '1':
        MenghitungLuas.start()
    elif menu == '2':
        menghitungVolume.start()
    else :
        break
        
