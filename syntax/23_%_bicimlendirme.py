ad = input ("adiniz : ")
numara = int(input("soyad : "))
print ("ad : %s \nnumara: %i"%(ad,numara))

metin = """
adiniz = %(ad)s 
numraniz = %(numara)i
hosgeldiniz  %(ad)s

"""
print (metin%{"ad" : ad,"numara" : numara})
