#eval : evaluate (değerlendirme)  kendine verilen  verilen karakter dizilerini  degerlendirir
#eval ve exec arasında ki fark exec değişkene deger atanabilir
veri = "print ('abcd')"
print (veri)
deger = eval(veri) #burda veri içinde bulunan print normal kod gibi davranır
exec ("a=10") # burad bulunun atama eval ile yapılamaz
print (a)
