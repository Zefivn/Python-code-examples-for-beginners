while True:  # Burada KUllanıcı adının sonsuz dögüsünü açıyorum.
    kulad = input("Kullanici adini giriniz: ")


    if kulad == "batuhan":
        while True:  #Burada ise Şifrenin sonsuz dögüsünü açıyorum.
            sifre = input("Şifrenizi giriniz: ")

   
            if sifre == "123456":
                print("Hoşgeldiniz")
                break  
            else:
                print("Şifre hatali! Tekrar deneyin.")
        break 
    else:
        print("Kullanici adi hatali! Tekrar deneyin.")
