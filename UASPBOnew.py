class Luas():
    def __init__(self, sisi, alas, tinggi, jari_jari):
         self.input_sisi = sisi
         self.input_alas = alas
         self.input_tinggi = tinggi
         self.input_jari = jari_jari
         
    def persegi(self):
        luaspersegi = self.input_sisi * self.input_sisi
        print("Luas Persegi :", luaspersegi)

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
            input_sisi = float(input("Masukkan Sisi :"))
            persegi = Luas(input_sisi, 0,0,0)
            Luas.persegi(persegi)
            
        # elif pilihmenu == '2':
        #     MenghitungLuas.menu("Lingkaran")
        # elif pilihmenu == '3':
        #     MenghitungLuas.menu("Segitiga")
        else:
            pass
    


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
        Luas.start()
    # elif menu == '2':
    #     menghitungVolume.start()
    else :
        break
        
   