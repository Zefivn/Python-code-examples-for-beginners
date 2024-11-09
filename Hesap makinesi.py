while True:  
    print("1. Toplama")
    print("2. Cikarma")
    print("3. Carpma")
    print("4. Bölme")

    islem = input("Ne tür islem yapmak istiyorsunuz? ")

    sayi_1 = float(input("1. Sayiyi giriniz: "))
    sayi_2 = float(input("2. Sayiyi giriniz: "))

    if islem == "1":
        print("Sonuç: ", sayi_1 + sayi_2)
    elif islem == "2":
        print("Sonuç: ", sayi_1 - sayi_2)
    elif islem == "3":
        print("Sonuç: ", sayi_1 * sayi_2)
    elif islem == "4":
        if sayi_2 != 0:
            print("Sonuç: ", sayi_1 / sayi_2)
        else:
            print("Bir sayi 0'a bölünemez!")
    else:
        print("Geçersiz bir parametre girdiniz!")

    devam = input("Başka bir işlem yapmak istiyor musunuz? (E/H): ").upper()  
    
    if devam == "H":
        print("Program sonlandiriliyor...")
        break  
    elif devam != "E":
        print("Geçersiz giriş, program sonlandiriliyor...")
        break
