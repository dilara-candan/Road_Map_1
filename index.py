def sayiKontrol (value, type = None):
    if (not(value.isdigit())):
        return sayiKontrol(input("Tekrar giriniz:"), type)    

    value = int(value)

    if ((type == "harfNotu" and value >= 0 and value <= 100) or 
        (type == "menu" and value > 0 and value < 4) or type == None):
        return value
    
    return sayiKontrol(input("Tekrar giriniz:"), type)

def bolunenSayiBulma (min_sayi, max_sayi, bolunecek_sayi):
    tamBolunenler = []

    if (min_sayi >= max_sayi):
        print("Minimum sayı maximum sayıdan büyük veya eşit olamaz.")

        return "";

    for i in range(min_sayi, max_sayi + 1):
        if (i % bolunecek_sayi == 0):
            tamBolunenler.append(i)
    
    return {
        "tamBolunenler": tamBolunenler,
        "toplam_sayi": len(tamBolunenler)
    };

def sayiOkunusu(sayi):
    stringNumber = str(sayi)

    birler  =   [ "" , "Bir" , "İki" , "Üç" , "Dört" , "Beş" , "Altı" , "Yedi" , "Sekiz" , "Dokuz" ]
    onlar  = [ "" , "On" , "Yirmi" , "Otuz" , "Kırk" , "Elli" , "Altmış" , "Yetmiş" , "Seksen" , "Doksan" ]
    
    return onlar[int(stringNumber[0])] + " " + birler[int(stringNumber[1])]

def sayiAtama(sayi):
    if (sayi < 10 or sayi > 99):
        print("Lütfen 2 basamaklı bir sayı giriniz.")
        return "";

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

    secenek = sayiKontrol(input("Seçim yapınız: "), "menu")

    if (secenek == 1):
        min_sayi = sayiKontrol(input("Min Sayi:"))
        max_sayi = sayiKontrol(input("Max Sayi:"))
        bolunecekSayi = sayiKontrol(input("Bölünecek Sayı:"))
        
        print(bolunenSayiBulma(min_sayi, max_sayi, bolunecekSayi))
        
    elif (secenek == 2):
        sayi = sayiKontrol(input("Okunuşu gösterilecek sayı:"))

        print(sayiAtama(sayi))
        
    elif (secenek == 3):
        vize1 = sayiKontrol(input("Vize 1:"), "harfNotu")
        vize2 = sayiKontrol(input("Vize 2:"), "harfNotu")
        final = sayiKontrol(input("Final:"), "harfNotu")

        print(harfNotuHesaplama(vize1, vize2, final))


main();
