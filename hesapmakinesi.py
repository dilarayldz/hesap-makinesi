print("""
Hesap Makinesi
--------------

1) Toplama
2) Çıkarma
3) Çarpma
4) Bölme

(Çıkmak İçin Çıkış Yazınız)
""")

while True:
    sonuc = 0
    sayi1 = float(input("1. sayıyı giriniz: "))
    sayi2 = float(input("2. sayıyı giriniz: "))
    islem = str(input("İşlem Seçiniz: "))

    if(islem == "1"):
        sonuc = sayi1 + sayi2
        print("Sonuç: ", sonuc)
        continue

    elif(islem == "2"):
        sonuc = sayi1 - sayi2
        print("Sonuç: ", sonuc)
        continue

    elif (islem == "3"):
        sonuc = sayi1 * sayi2
        print("Sonuç: ", sonuc)
        continue

    elif(islem == "4"):
        sonuc = sayi1 / sayi2
        print("Sonuç: ", sonuc)
        continue

    elif(islem=="çıkış"):
        break

    else:
        print("Yanlış bir seçim yaptınız")