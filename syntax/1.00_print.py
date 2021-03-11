#print(,sep=' ', end="\n", file="sys.stdout", flush=False) printf fonksiyonu ön tanımlı şeklidir. 
#sep => ',' ile ayırdığımız kısımlarda ne yapılacağı ön tanımlı olarak bir boşluk atar
#end => print kapatıldıktan sonra ne yapılaçağı  belirlenir ön tanımlı şekilde  bir alt satıra geçme tanımlı 
#file => nereye cıktı verileçeği  belirler ön tanımlı olarak ekrandır
#flush => acılan dosyanın  printf sonra kapatılıp kapatılmayaçağıbelirlenir
cumle = """Python da  tek tirnak, iki tirnak,
uc tirnak icinde kullanilan her sey karakter dizisidir.
Uc tırnak  en onemli farki  tirnagi kapatana kadar alt 
satira gecmeyi ve uzun cümeler yazmada kolaylik saglar."""
# """ bir şey  değişkene atanmazsa  çoklu bir yorum satiri görevi görebilir.
print (cumle)  #tanimli olan değişkeni cağılır
print ("10+15 "+"=",10+15) #python print içinde işlem yapılabilir.
print ("-"*30) #karakterin sonunda bulunan * işareti o kadar tekrarlanacağı anlamına gelir 
print (*"print",sep="\n") #karakter dizisinin başına konan *  karakter dizisini  karakter karakter printe  koyar
print ("-"*30)
print ("n\n","t\t","a\a","r\r","v\v","b\b","f\f") # kaçış dizeleri 
print ("-"*30)
print ("\u0076") # ASCII karakter karşılığını gösterir

