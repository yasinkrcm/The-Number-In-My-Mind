import random

isim = input("İsminiz : ")
sayac  = 5 
sayi = random.randint(1,20)
tahmin = 0
hak = 1 

print("Merhaba",isim,"1 ile 20 arasında bir sayı tuttum bilmek için 5 şansın var ")


while sayac != 0:
    sayac -= 1
    tahmin = int(input("Tahminin : "))
    if sayi == tahmin:
        print("Harika",hak,"defada bildin")
        break
    if sayi < tahmin:
        print("aklımdaki sayı daha küçük , kalan deneme hakkkın :",sayac )
    elif sayi > tahmin :
        print("aklımdaki sayı daha büyük , kalan deneme hakkın : ",sayac)
    hak+=1

if sayac == 0 :
    print("üzgünüm bilemedin aklımdaki sayı  :",sayi)
