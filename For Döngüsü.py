liste=[1,2,3,4,5,6]

for sayi in liste: # Liste İçerisinde bulunan elemanların hepsini teker teker döner.
    print(sayi)

print("----------------------------------------")

for sayi_aralik in range(4): # Range komutu ile 0 ile belirtilen sayı arasındakileri ekrana yazdırır.
    print(sayi_aralik)

print("----------------------------------------")

for sayi_çift in range(21): # Range komutu ile 0 ile belirtilen sayı arasındaki çift sayıları ekrana yazdırır.
    if sayi_çift % 2 == 0:
     print(sayi_çift)

print("----------------------------------------")

dizi=[2,5,7,6,9]
toplam=0

for sayilar in dizi:  # Sırayla döndürülen sayıları toplayarak ekrana yazdırır.
    toplam=toplam+sayilar
    print(toplam)