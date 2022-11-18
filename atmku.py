users = [
    {
        "id": "0001",
        "no_rekening": "234121",
        "username": "fyanramadhan11",
        "pin": "2215",
        "saldo": 100000000
    },
    {
        "id": "0002",
        "no_rekening": "234122",
        "username": "andrewirawan12",
        "pin": "2231",
        "saldo": 25000000
    },
    {
        "id": "0003",
        "no_rekening": "234123",
        "username": "ikhsanryu",
        "pin": "2270",
        "saldo": 1000
    },
    {
        "id": "0004",
        "no_rekening": "234124",
        "username": "phutraRR",
        "pin": "2271",
        "saldo": 500
    },
    {
        "id": "0005",
        "no_rekening": "234125",
        "username": "aqmaldani",
        "pin": "2275",
        "saldo": 2500
    }
]

user_id = 0
loop = "n"

def cek_log(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False

def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1

def cek_rek(nmr):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(nmr):
            return int(i)
    return -1

def transfer_uang(uang, no_rek):
    idx1 = cek_user(user_id)
    idx2 = cek_rek(no_rek)
    if idx1 >= 0:
        if users[idx1]['saldo'] >=int(uang):
            users[idx1]['saldo'] = users[idx1]['saldo'] - int(uang)
            users[idx2]['saldo'] = users[idx2]['saldo'] + int(uang)           
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rek)
            print("sisa saldo anda adalah Rp.", users[idx1]['saldo'])
        else :
            print("Maaf Saldomu gak cuku Bro!")
            
def ambil_uang(uang):
    idx1 = cek_user(user_id)
    if idx1 >= 0:
        if users[idx1]['saldo'] >= int(uang):
            users[idx1]['saldo'] = users[idx1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("sisa saldo anda adalah Rp.", users[idx1]['saldo'])
        else:
            print("Maaf Saldomu gak Cukup Bro!")
            
msyn_atm = 'y'
status_login = False

while msyn_atm == "y":
    while not status_login:
        print("SELAMAT DATANG DI ATM BANK MSYNNGROUP")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN Bro : ")
        
        cl = cek_log(pin)
        if cl:
            print("selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Maaf PIN kamu salah Bro!")
            print("")
            print("")
    
    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("SELAMAT DATANG DI ATM MSYNNGROUP")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rek(no_rek)
 
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                transfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
 
        elif a == 5:
            status_login = False
            loop = "n"
            msyn_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"