import pandas as pd


def sozluk(dictionary):
    return pd.DataFrame(dictionary)


def ogrenci_kayit():
    ogrenci_listesi = {'isim': [], 'soyad': [], 'okul_no': [], 'ders': [], 'sinav_puani': [], 'harf_notu': [], 'sonuc': []}
    while True:
        ders = str(input('Ders giriniz: '))
        isim = str(input("Isim giriniz: "))
        soyad = str(input("Soyad giriniz: "))
        okul_no = int(input("Okul no giriniz: "))
        sinav_puani = int(input("Sinav puani giriniz: "))
        sistem = input("Yeni bir ogrenci eklemek icin 'y' basin: ")

        ogrenci_listesi['ders'].append(ders)
        ogrenci_listesi['isim'].append(isim)
        ogrenci_listesi['soyad'].append(soyad)
        ogrenci_listesi['okul_no'].append(okul_no)
        ogrenci_listesi['sinav_puani'].append(sinav_puani)
        if (sinav_puani >= 85):
            ogrenci_listesi['harf_notu'].append('A')
            ogrenci_listesi['sonuc'].append('Geçti')
        elif (sinav_puani <= 84 and sinav_puani >= 70):
            ogrenci_listesi['harf_notu'].append('B')
            ogrenci_listesi['sonuc'].append('Geçti')
        elif (sinav_puani <= 69 and sinav_puani >= 55):
            ogrenci_listesi['harf_notu'].append('C')
            ogrenci_listesi['sonuc'].append('Geçti')
        elif (sinav_puani <= 59 and sinav_puani >= 50):
            ogrenci_listesi['harf_notu'].append('D')
            ogrenci_listesi['sonuc'].append('Geçti')
        else:
            ogrenci_listesi['harf_notu'].append('F')
            ogrenci_listesi['sonuc'].append('Kaldı')

        if (sistem != 'y'):
            break

    return sozluk(ogrenci_listesi)

data = ogrenci_kayit()

writer = pd.ExcelWriter('ogrenci_sistemi.xlsx')

data.to_excel(writer)
writer.save()

