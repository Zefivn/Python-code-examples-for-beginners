liste=['Kabuk','Ayakkabi']

while True:
   
   eklenen=input("Eklemek istediginiz metni giriniz: ")
   liste.append(eklenen)
   print(liste)

   durum=input("Başka bir metin eklemek istiyor musunuz (E/H)")
   if durum=="E":
      continue
   elif durum=="H":
     break
   else:
    print("Hatali bir komut girdiniz! ")

    



