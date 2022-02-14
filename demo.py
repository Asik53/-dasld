"""
sayi = int(input("SAYI GİRİNİZ: "))

teksayi = 0
ciftsayi = 0
for x in range (1,sayi+1):
        if x % 2 == 0:
                ciftsayi += x
        else:
                teksayi += x

print("ÇİFT SAYILARIN TOPLAMI : {0}".format(ciftsayi))
print("TEK SAYILARIN TOPLAMI : {0}".format(teksayi))




sayi = int(input("SAYI GİRİNİZ: "))
a = 0
b = 0 
teksayi = 0
ciftsayi = 0
for x in range (1,sayi+1):
        if x % 2 == 0:
                a += 1
                ciftsayi += x 
        else:
                b += 1
                teksayi += x
print("ÇİFT SAYILARIN TOPLAMI : {0}".format(ciftsayi / a))
print("TEK SAYILARIN TOPLAMI : {0}".format(teksayi / b))




def dairealan(yaricap):
        alan=float(yaricap)*float(yaricap)*3.14
        print("alan: ",alan)
        return alan

r = input("yarıçap nedir")
dairealan(r)



sifre = input("sifre girin: ")
if sifre == sifre[::-1]:
 print(sifre)



sifre = int(input("şifre giriniz: "))
sezai = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

"""



