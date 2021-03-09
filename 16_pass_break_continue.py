#pass  pas gecmek anlaminda 
#break  donguyu sonlandirmak
#continue donguyu basa sarmak
for a in range(15):
	if a == 3:
		print ("a = ",a,"pass calisti")
		pass
	if a ==  8:
		print ("a = ",a,"continue calisti")
		continue 
	if a == 10:
		print ("a = ",a,"break calisti ")
		break
	print ("a = ",a)
print ("islem sonlandirildi...")
