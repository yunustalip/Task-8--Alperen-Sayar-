import time
import random

class Laboratuvar():
    
    def __init__(self, sinifno=random.randint(1,9999), ogretmen="", kontenjan="", dersgunu=""):

        self.sinifno=sinifno
        self.ogretmen=ogretmen
        self.kontenjan = kontenjan
        self.dersgunu = dersgunu
        self.ogrencisayi = 0
        self.ogrencilistesi = []

    def ogrenci_ekle(self,ogrenciisim):
        if self.kontenjan<=self.ogrencisayi:
            print("Kontenjan doludur")
        else:
            self.ogrencisayi += 1
            self.ogrencilistesi.append(ogrenciisim)
            print("Öğrenci derse eklendi")

    def ogrencilistesinigoster(self):
        print("Derste kayıtlı öğrenciler:", self.ogrencilistesi)
    
    def ogrenci_sil(self,ogrenciisim):
            self.ogrencisayi -= 1
            self.ogrencilistesi.remove(ogrenciisim)
            print("Öğrenci silindi")
    
    def ogretmen_ogren(self):
            print(f"{self.sinifno} nolu sınıfın öğretmeni: {self.ogretmen}")

    def ogretmen_degistir(self,ogretmenisim):
        self.ogretmen = ogretmenisim
        print(f"{self.sinifno} nolu sınıfın yeni öğretmeni: {ogretmenisim}")
    
    def dersgunu_degistir(self,gun):
        self.dersgunu = gun
        print(f"{self.ogretmen} öğretmenin yeni labaratuvar dersi günü: {gun}")
    

print("""
        1. Öğrenci Ekle
        2. Öğrenci Sil
        3. Öğrenci Listesi
        4. Sınıfın Öğretmenini Öğren
        5. Sınıfın Öğretmenini Değiştir
        6. Sınıfın Ders Gününü Değiştir

Çıkmak için q'ya bas.

""")
lab=Laboratuvar(sinifno=1001,ogretmen="Hasan",kontenjan=20,dersgunu="Cuma")

while True:

    islem= input("İslem seçiniz")

    if islem =="q":
        print("Sonlandırılıyor")
     
    elif islem =="1":
        ogrenciisim = input("Öğrenci ismi giriniz")
        lab.ogrenci_ekle(ogrenciisim)
    
    elif islem=="2":
        ogrenciisim = input("Öğrenci ismi giriniz")
        lab.ogrenci_sil(ogrenciisim)

    elif islem=="3":
        lab.ogrencilistesinigoster()
    
    elif islem=="4":
        lab.ogretmen_ogren()
    
    elif islem=="5":
        yeniogretmen = input("Yeni öğretmen ismi giriniz")
        lab.ogretmen_degistir(yeniogretmen)

    elif islem=="6":
        dersgunu_degistir = input("Yeni ders günü giriniz")
        lab.ogretmen_degistir(dersgunu_degistir)
       
    else:
        print("hatalı Tuşlama")



    
