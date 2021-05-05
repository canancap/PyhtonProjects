# PYTHON DÖKÜMANI

# visual studio code bir editördür ancak ide kadar güçlüdür.pyhtonu kullanmak için üzerine python.org'dan 
# python indirilmelidir.
# CTRL+F5 RUN
# değişkenlerde type definition yapılmaz. int, float gibi gerek yok.
# ifade sonuna ; konmaz
# yorum satırı seçme: CTRL+KC ya da # işareti koy
# yorum satırını geri almak için : CTRL+KU
# pythonda type safety sorunu var. aynı isimde ikinci bir değişken tanımlayabiliyorsun ikinci tanımlananı geçerli kabul ediyor. dikkat etmek gerekiyor.hata vermiyor aynı isimde verdin diye.

# VARIABLES (DEĞİŞKENLER)-------------------------------

counter = 100        # An integer assignment
miles   = 100.5      # A floating point
name    = "CANAN"    # A string
tc      = "12345677" # tc üzerinde işlerim yapmayacağımız için int olarak belirlemedim string yaptım.
durum   = False
name    = "ÇAP"      # type safety sorunundan dolayı son değişkeni ekrana basar
print(name)
print(type(name))    # değişkenin tipini yazdırmak
print(type(durum))
print("----------------------------------------------")
#-----------------------------------------------------

#CONDITION BLOCKS (ŞART BLOKLARI)---------------------

istenenKredi = 10000
hesap = 50000
minimumOlmasıGerekenHesap = 10000

if hesap>=minimumOlmasıGerekenHesap: # Condition Block yani şart bloğu sonuna : koy ve enter yap. indentation yani boşluk kuralı var.
    print("kredi verilebilir")
elif hesap>=9000 and hesap<=9900: # and ve or operatörleri vardır
    print("Müdüre sorulacak")
elif hesap == 9900: 
    print("Genel Müdüre sorulacak")
else:
    print("kredi almak için bakiyeniz yetersiz")
print("işlem sonu")
print("---------------------------------------------")
#----------------------------------------------------
#şart bloklarına örnek: 3 sayının en büyüğünü bulma
sayi1 = 100
sayi2 = 20
sayi3 = 30
if (sayi1>sayi2 and sayi1>sayi3):
    print("En Büyük Sayı:"+ str(sayi1))
if(sayi2>sayi1 and sayi2>sayi3):
    print("En Büyük Sayı:"+str(sayi2))
if(sayi3>sayi1 and sayi3>sayi2):
    print("En Büyük Sayı:"+str(sayi3))
print("--------------------------------------------")
#---------------------------------------------------


# ARRAYS (DİZİLER)----------------------------------

bosListe = [] #değeri olmayan ama adresi olan bir dizi
urunler = ["Labtop","Mouse","Keyboard"]
print(urunler)
print(type(urunler))
urunler.append("Telefon") #listeye yeni ürün ekle
print(urunler)
ogrenciler1 = ["Canan","Yusuf","Muhammed"]
ogrenciler2 = ["Ali","Veli","Abdürrahim"] 
ogrenciler1 = ogrenciler2  # Nesnel programalamaya giriş.değer-referansa örnek
#ogrenciler1 in tutacağı adres ogrenciler2'nin tutacağı adrestir.bu durumda yapılan atamada..ogrenciler1'i tutan olmadığı için bir süre sonra garbage collection onu siler.
ogrenciler2[0] = "Engin"
print(ogrenciler1)

# ÖNEMLİ BİLGİ: Veriler hafızada nasıl tutulur?:
# list(diziler),class, interface, string(liste gibi çalıştığı için)  -> referans tip heap'e kaydediliyor.Değeri değil referans numarası tutar.o nedenle içine yapılan son müdahele neyse onu tutar 
# int, float, boolean  -> değer tip (sayısal tip) stack'e kaydediliyor.sadece değer olarak kaydeder.string bellekte referans tip gibi tutulur ancak değer tip gibi değer döndürür
sayı1 = 10
sayi2 = 20
sayi1 = sayi2
sayi2 = 60
print(sayi1)  # output 20dir. çünkü değer tiptir sayi1.dizi olsaydı yukarıdaki gibi sayı2'nin sonraki değişiminden etkilenirdi.
print("----------------------------------------------")
# stringin referans olup değer döndürmesine örnek
isim = "canan" # string aslında karakterlerden oluşan bir listedir.o nedenle referans tip olarak kaydedilir
print(isim[0]) 
# az if kullanmak kodun kalitesini gösterir. kod kalitesini gösteren programlar vardır.çok if az nesnel olmuş olur.
#devops(developer operations) = geliştirme operasyonları. bir yazılımın analizi için kullanılan bir program. analiz süreçleri.müşterinin taleplerinin kodla ilişkilendirmek için yapılan ön analizdir.
#test = kodun son versiyonunu aldınız.bunların her biri kendi ortamlarında çalışırken birlikte çalışmıyor olabilirler. o nedenle belli programlarla test edilmeliler. build gibi
print("-----------------------------------------------")


# DÖNGÜLER (LOOPS) -------------------------------------

sehirler = ["Ankara","İstanbul","İzmir"] 
for sehir in sehirler: #iterasyon bazlı döngü
    print(sehir)
for sayi in range(0,10,2): #range bazlı döngü. 2->kaçar kaçar ilerlesin.
    print(sayi)
sayac = 1
while sayac<=10:
    print(sayac)
    sayac = sayac + 1 # sayac++
#isim = input("Adınız: ")
#print("İsminiz: " + isim)

#sayi = int(input("Sayınız: ")) 
#print("sayınız: "+ str(sayi))

sayi = int(input("Hangi sayının faktoriyelini alayım: "))
faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel = faktoriyel * i
print(faktoriyel)
print("-----------------------------------------")

# CLASSES - OOP 

# clas objelere karşılık gelir.
# 1-İçinde özellik barındırır.Müşterinin bilgileri mesela.entity(varlık) olarak kullanırız.
# 2-Operasyon tutucudur.Birbiriyle ilişkili bütün operasyonları içerisinde tutarız ki aklımızda tutmak zorunda kalmayalım.
# fonksiyonları teker teker bulundurmaktansa bir class içinde bulundururuz.
# iş yapan fonsiyonlar var iş yapıp değer döndüren fonksiyonlar var
#fonksiyon tanımlayalım
class Banka: # birbiriyle ilişkili fonksiyonları bir sınıfta toplayarak daha mantıklı bir birleştirme yapmış oluruz.yni ortak operasyonları bir arada tutmak için class kullanırız.
             # classlar referans tiplerdir. yazılımda sürdürelebilirliği sağlamak için çok iyi bir çözümdür. bankaya yeni gelen yazılımcı bu şekilde kodlara adapte olabilecek ya da bozamayacak.zaten hazır yazılmış classlar var
    def krediBasvur(self): # c# ve javada this
        print("kredi başvurusu yapıldı")
    def krediHesapla(self):
        print("kredi hesaplandı")
banka = Banka() 
banka.krediBasvur()
banka.krediHesapla()

class Matematik:
    def topla(self,sayi1,sayi2): # self matematik classının kendisi demek.oraya işaret ediyor.
        return sayi1+sayi2
    def cikar (self,sayi1,sayi2):
        return sayi1-sayi1

matematik=Matematik() #instance almak demektir. yani ondan bellekte referans bir adres oluşturmak demek.
sonuc = matematik.topla(3,5)
print ("Sonuc: "+str(sonuc))

# selfe örnek ---------------------
class Person:
    def __init__(self,name,lastname): # bu şekilde name ve lastname in person clası dışında kullanılabilir olmasını sağlıyoruz.
        self.name = name
        self.lastname = lastname

musteri1 = Person("Canan","Çap")
print(musteri1.name)
#---------------------------------

# INHERİTANCE---------------------------------------------------

# class Istatistik(Matematik):
#     def __init__(self,sayi1,sayi2):
#         super().__init__(sayi1,sayi2)#super üst sınıfın kendisi demektir. yani matematiğin kendisi.burada matematiğin initini kullan diyor.
#     def varyansHesapla(self):
#         return self.s1 * self.s2

#istatistik=Istatistik(2,6)   
# bir üst sınıf olan Matematik clasının toplama çarpma gibi fonksiyonlarını kullanmış oluruz inheritance ile.
# bir sınıf sadece bir sınıftan miras alabilir.



# VERİTABANI PROGRAMLAMA ---------

# sqlitebrowser.org sitesinden sqlite db(mysql ile) yi indirdik. siteden örnek veritabanı indirdik sqlite sample database diyerek.
# db yi aç örnek vertibanını burada aç.

import sqlite3

def listele():
    baglanti = sqlite3.connect("chinook/chinook.db")
    cursor = baglanti.execute("select Lastname from customers")

    for satir in cursor:
        print(satir[0])

    baglanti.close()
print("-------------DB'DEN ÇEKİLEN BİLGİLER------------")
listele()  # db den veri çeken yazdığımız fonksiyonu çağırıyoruz
print("------------------------------------------------")











