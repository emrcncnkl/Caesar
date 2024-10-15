alfabe = ['a', 'b', 'c','ç' 'd', 'e','f','g','ğ','h','ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o','ö','p','q','r','ş','s','t', 'u','ü',
            'v', 'w', 'x', 'y', 'z']


def caesar(orjinal_metin, kaydirma_sayisi, sifrele_coz):
    cikan_metin = ""
    if sifrele_coz == "çözümle":
        kaydirma_sayisi *= -1

    for harf in orjinal_metin:

        if harf not in alfabe:
            cikan_metin += harf
        else:
            kaymis_hali = alfabe.index(harf) + kaydirma_sayisi
            kaymis_hali %= len(alfabe)
            cikan_metin += alfabe[kaymis_hali]
    print(f"{orjinal_metin} cümlenizin sifrelenmiş hali : \n {cikan_metin}")


devam_edilsin_mi = True

while devam_edilsin_mi:

    sorgu = input("Mesajınızı Şifrelemek için 'şifrele', Şifreli mesajı çözmek istiyorsanız 'çözümle' yazınız. :\n").lower()
    mesaj = input("Mesajınızı giriniz:\n").lower()
    kaydir = int(input("Mesaj'daki harfler ne kadar kaydırılsın ?:\n"))

    caesar(orjinal_metin=mesaj, kaydirma_sayisi=kaydir, sifrele_coz=sorgu)

    yeniden = input("Yeni bir işlem için 'evet' yazın, istemiyorsanız 'hayır' yazınız...\n").lower()
    if yeniden == "hayır":
        devam_edilsin_mi = False
        print("Görüşmek Üzere!")