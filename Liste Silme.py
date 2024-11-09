liste = ['Elma', 'armut', 'Kabak', 'Karpuz']
print(liste)

a = int(input("Silmek istediğiniz ögenin sirasini giriniz: "))

# Belirtilen sıradaki öğeyi sil
if 0 <= a < len(liste):  # Geçerli bir sıra olup olmadığını kontrol et
    del liste[a]
    print("Güncellenmiş liste:", liste)
else:
    print("Geçersiz sira numarasi!")
