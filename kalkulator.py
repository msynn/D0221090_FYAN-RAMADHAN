print('|',' '*38,'|')
print('|'," KALKULATOR ".center(38,'-'),'|')
print('|',' '*38,'|')
a = int(input("| INPUT NUMBER \t: "))
print('|',' '*38,'|')
print('|',"SELECT OPERATION".center(38,' '),'|')
print('|',' '*38,'|')
print('|','| + | - | * | / |'.center(38,' '),'|')
pilihan = input("| : ")
print('|',' '*38,'|')
b = int(input("| INPUT NUMBER \t: "))
print('|',' '*38,'|')
angka = []
if pilihan == '+':
    hasil = a + b
    angka.append(hasil)
elif pilihan == '-':
    hasil = a - b
    angka.append(hasil)
elif pilihan == '*':
    hasil = a * b
    angka.append(hasil)
elif pilihan == '/':
    hasil = a / b
    angka.append(hasil)
while True :
    print('|',' '*38,'|')
    print('|',"SELECT OPERATION".center(38,' '),'|')
    print('|',' '*38,'|')
    print('|','| + | - | * | / | = |'.center(38,' '),'|')
    pilihan2 = input("| \t: ")
    if pilihan2 == '=':
        print(hasil)
        break
    print('|',' '*38,'|')
    print('|','INPUT NUMBER'.center(38,' '),'|')
    print('|',' '*38,'|')
    c = int(input("| \t :"))
    if pilihan2 == '+':
        hasil = hasil + c
        angka.append(hasil)
    elif pilihan2 == '-':
        hasil = hasil - c
        angka.append(hasil)
    elif pilihan2 == '*':
        hasil = hasil * c
        angka.append(hasil)
    elif pilihan2 == '/':
        hasil = hasil / c
        angka.append(hasil)