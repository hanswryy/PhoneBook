import os
import re

class Kontak:
    name = ""
    number = ""

    def __init__(self, name, number):
        self.name = name
        self.number = number

def pressEnter():
    while 1:
        enter = input("\nTekan enter untuk melanjutkan...")
        if enter=="":
            break

def printMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selamat datang!\n")
    print("1. Tambah kontak")
    print("2. Daftar kontak")
    print("3. Hapus kontak")
    print("4. Cari kontak")
    print("5. Update kontak")
    print("6. Keluar")

def inputContact(name, number):
    printMenu()
    k = Kontak(name, number)
    f = open("Contacts.txt", 'a')
    f.write(k.name + token + k.number + "\n")
    f.close()

def searchContact(inpNama):
    with open("Contacts.txt", 'r') as f:
        for line in f:
            x = re.split(r';|\n', line)
            if x[0] == inpNama:
                print(x[0] + " " + x[1])
                pressEnter()
                f.close()
        print("Ga ada euy")
        pressEnter()
        f.close()

def printContact():
    printMenu()
    print("\n")
    with open("Contacts.txt", 'r') as f:
        for line in f:
            x = re.split(r';|\n', line)
            print(x[0] + " " + x[1])
    
    pressEnter()
    f.close()

def deleteContact(inpName):
    c = True
    with open("Contacts.txt", "r") as masuk:
        with open("temp.txt", "w") as keluar:
            for line in masuk:
                x = re.split(r';|\n', line)
                if x[0] != inpName:
                    keluar.write(line)
                else:
                    c=False
    if c==True:
        print("Ga ada euy")
        pressEnter()
        c=True
    
    os.replace('temp.txt', 'Contacts.txt')

def updateContact(inpName, numBaru):
    with open("Contacts.txt", "r") as masuk:
        with open("temp.txt", "w") as keluar:
            for line in masuk:
                x = re.split(r';|\n', line)
                if x[0] != inpName:
                    keluar.write(line)
                else:
                    keluar.write(x[0] + token + numBaru + "\n")

    os.replace('temp.txt', 'Contacts.txt')


err = False
token = ';'

while 1:
    printMenu()

    if err:
        print ("Input tidak valid!")
        err = False
    
    try:
        inp = int(input("\nPilih : "))
    except ValueError:
        continue

    match inp:
        case 1:
            name = input("\nInput nama : ")
            number = input("Nomor telepon : ")
            inputContact(name, number)
        case 2:
            printContact()
        case 3:
            inpName = input("Siapa yang ingin dihapus? : ")
            deleteContact(inpName)
        case 4:
            inpName = input("Siapa yang dicari? : ")
            searchContact(inpName)
        case 5:
            inpName = input("Kontak mana yang ingin diupdate : ")
            newNum = input("Masukkan nomor baru : ")
            updateContact(inpName, newNum)
        case 6:
            exit()
        case _:
            err = True
            continue