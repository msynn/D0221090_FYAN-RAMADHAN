data = [0,2,2,1,0,9,0] #NILAI DIDAPAT DARI NIM SAYA YAKNI "0221090"
# n ini adalah pnjang data
n = len(data)

def enter():
    garis()
    enter = input("Enter kembali ke Menu!")
    if enter == enter :
        menu()
        
def hasil(hitung):
    print("="*40)
    print(f"HASIL {hitung}".center(40," "))
    print("="*40)

def garis():
    print("-"*40)

def menu():
    garis()
    print("PROGRAM SEDERHANA".center(40, " "))
    garis()
    print(f"Data : {data}")
    garis()
    print('''
    1. Mencari Nilai Mean
    2. Mencari Nilai Modus
    3. Mencari Nilai Median
    4. keluar
    ''')
    pilih = input("Pilih nilai yang dicari : ")
    if pilih == '1':
        hitungMean()
        
    elif pilih == '2':
        hitungModus(data)
        
    elif pilih == '3':
        hitungMedian()
        
    elif pilih == '4':
        pass
    else :
        print("Masukkan Kode Menu!!!")
        enter()
        menu()

def hitungMean():
    hasil('MEAN')
    jumlahData = 0
    # Menjumlahkan Seluruh Data
    for i in data:
        jumlahData += i
    
    # Rumus dari mean adalah sigma x (Jumlah nilai dalam data)/ n
    mean = jumlahData / n
    garis()
    print("sigma X \t :", jumlahData)
    print("n \t\t :", n)
    print(f"Nilai Mean \t : {mean}")
    
    enter()
    
    
    
def hitungModus(deret):
    hasil("MODUS")
      # dictionary untuk mapping nilai terbanyak
    frekuensi = {}

  # perulangan satu-persatu tiap bilangan
    for bilangan in deret:
    # periksa apakah sudah pernah muncul atau belum
        if bilangan in frekuensi:
            frekuensi[bilangan] += 1
        else:
            frekuensi[bilangan] = 1
            

# Menampilkan jumlah masing-masing Nilai dari Data     
    print("Jumlah dari masing-masing Nilai :")
    for idx, value in frekuensi.items():
        print(idx, "muncul sebanyak", value, "kali")     

    # Mencari idx dengan frekuensi tertinggi (modus)
    modus = []
    frekuensi_tertinggi = 0
    for angka, frek in frekuensi.items():
        if frek > frekuensi_tertinggi:
            frekuensi_tertinggi = frek
        else :
            pass  
    for angka, frek in frekuensi.items():
        if frek == frekuensi_tertinggi:
            modus.append(angka)
    # 
    if modus == data:
        modus = []
    else :
        pass
            

    print("Nilai yang sering muncul/ Modus : ",modus)
    enter()

    
def hitungMedian():
    hasil("MEDIAN")
    def bubble_sort():
        # Sebelum mencari nilai median terlebih dahulu kita mengurutkan data yang kita miliki,
        # disini saya membuat algoritma bubblesort untuk mengurutkan data tersebut
        n = len(data)
        for i in range(n): 
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    
    bubble_sort()
    
    # Selanjutnya sesuai rumus menghitung median yaitu sesuai dengan panjang data yang dimiliki
    # berbeda rumus ketika jumlah panjang data bernilai genap atau ganjil
    # jadi disni saya membuat kondisi seperti berikut
    
    # LENGHT GENAP
    if n %2 == 0:    
        x1 = n / 2
        x2 = n/2+1
        date1 = data[int(x1)]
        date2 = data[int(x2)]
        x = date1 + date2
        median = x/2
        garis()
        print("Data diurutkan \t :", data)
        print("Nilai tengah 1 \t :", date1)
        print("Nilai tengah 2 \t :", date2)
        print("Median \t\t :",median)
        
        enter() 
    
    # LENGHT GANJIL
    else :
        x = (n+1) / 2
        median = data[int(x-1)]
        garis()
        print("Data diurutkan \t :", data)
        print(f"Urutan ke\t : {int(x)}")
        print("Median \t\t :",median)
        
        
        enter()   
    
menu()

