from re import S


website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?

sonuc = len(website)

sonuc = len(kursAdi)


# 2- 'website' içinden www karakterlerini alın.


# 3- 'website' içinden com karakterlerini alın.


# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
sonuc = kursAdi[0:16]

sonuc = kursAdi[43:58]


# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.

sonuc = kursAdi[::-1]

#print(sonuc)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'

s = s[0:6] + 'W' + s[-4:]

#print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

#print('abc' * 3)



# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.' 

name, age, job = 'İbrahim SEVEN', 18, 'öğrenci' 

# me = 'Benim adım ' + name + ', yaşım ' + str(age) + ' ve mesleğim ' + job + '.'

# me = 'Benim adım {0} ,yaşım {1} ve mesleğim {2}.'.format(name,age,job)

me = f'Benim adım {name},Yaşım {age} ve mesleğim {job}.'

print(me)

