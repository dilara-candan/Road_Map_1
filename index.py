def bolunenSayiBulma (min_sayi, max_sayi, bolunecek_sayi):
    tamBolunenler = []

    if (min_sayi >= max_sayi):
        print("Girilen değerler validate değil.")

    for i in range(min_sayi, max_sayi):
        if (bolunecek_sayi % i == 0):
            tamBolunenler.append(i)
    
    return {
        "tamBolunenler": tamBolunenler,
        "toplam_sayi": len(tamBolunenler)
    };

def sayiOkunusu(sayi):
    birler  =   [ "" , "Bir" , "İki" , "Üç" , "Dört" , "Beş" , "Altı" , "Yedi" , "Sekiz" , "Dokuz" ]
    onlar  = [ "" , "On" , "Yirmi" , "Otuz" , "Kırk" , "Elli" , "Altmış" , "Yetmiş" , "Seksen" , "Doksan" ]
    
    birlerBasamagi = sayi % 10
    onlarBasamagi = sayi // 10

    return onlar[onlarBasamagi] + " " + birler[birlerBasamagi]

def sayiAtama(sayi):
    if (sayi < 10 or sayi > 99):
        print("Lutfen 2 basamaklı bir sayı giriniz")

    return sayiOkunusu(sayi)

def harfNotuHesaplama(vize1, vize2, final):
    ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4;

    if (ortalama >= 90):
        return "AA"
    elif (ortalama >= 85):
        return "BA"
    elif (ortalama >= 80):
        return "BB"
    elif (ortalama >= 75):
        return "CB"
    elif (ortalama >= 70):
        return "CC"
    elif (ortalama >= 65):
        return "DC"
    elif (ortalama >= 60):
        return "DD"
    elif (ortalama >= 55):
        return "FD"
    elif (ortalama < 55):
        return "FF"

def main():
    print("Secenekler: \n1 - Bolunen sayi bulma\n2 - Sayı okunuşu\n3 - Harf notu hesaplama")

    secenek = int(input("Seçim yapınız: "))

    if (secenek == 1):
        min_sayi = int(input("Min Sayi:"))
        max_sayi = int(input("Max Sayi:"))
        bolunecekSayi = int(input("Bölünecek Sayı:"))
        
        print(bolunenSayiBulma(min_sayi, max_sayi, bolunecekSayi))
    elif (secenek == 2):
        sayi = int(input("Okunuşu gösterilecek sayı:"))

        print(sayiAtama(sayi))
    elif (secenek == 3):
        vize1 = int(input("Vize 1:"))
        vize2 = int(input("Vize 2:"))
        final = int(input("Final:"))

        print(harfNotuHesaplama(vize1, vize2, final))


main();