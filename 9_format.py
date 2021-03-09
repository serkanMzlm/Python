#format  doldurulmasinin sonradan olmasini istedigimiz  yerlere  doldurmamizi saglar
metin = """
*****************
Ad : {}
Soyad : {}
Numara : {}
Serhir : {}
****************
"""
metin2 = """
{1:<20}  sola dayalı 
{1:>20}  saga dayali
{1:^20}  ortada 
{0}
"""
ad = input ("adinizi girin : ")
soyad = input ("soyadinizi girin : ")
numara = input ("numaranizi girin : ")
sehir = input ("sehir girin : ")

print (metin.format(ad,soyad,numara,sehir))
print (metin2.format(ad,soyad))
