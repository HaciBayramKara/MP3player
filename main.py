import random


class MP3Calar():

    def __init__(self, sarkiListesi=[]):
        self.suanCalanSarki = ""
        self.ses = 100
        self.sarkiListesi = sarkiListesi
        self.durum = True

    def sarkiSec(self):

        while True:
            secim = input("{} hangi şarkıyı seçmek istersiniz: ".format(self.sarkiListesi))
            if secim in self.sarkiListesi:

                self.suanCalanSarki = secim
                break
            else:
                print("hatalı şarkı")

    def sesArttir(self):
        self.ses += 5
        if self.ses > 100:
            self.ses = 100
            print("maximum ses seviyesi\n")

    def sesAzalt(self):
        self.ses -= 5
        if self.ses < 0:
            self.ses = 0
            print("minumum ses seviyesi\n")

    def rastgeleSarkiSec(self):
        rastgele = random.choice(self.sarkiListesi)
        self.suanCalanSarki = rastgele

    def sarkiEkle(self):
        self.sarkiListesi.append(input("Eklenecek Şarkı İsmini Giriniz: "))

    def sarkiSil(self):
        print("Silinecek Şarkı Sırasını Giriniz(1-{}): ".format(len(self.sarkiListesi)))
        sil = int(input(""))

        while sil < 1 or sil > len(self.sarkiListesi):
            sil = int(input("Lütfen belirtilen araklıkda giriniz(1-{}): ".format(len(self.sarkiListesi))))
        self.sarkiListesi.pop(sil - 1)

    def kapa(self):
        self.durum = False
        print("Program Sonlandı")

    def menuGoster(self):
        print("Şarkı Listesi:{}\nŞuan Çalan Şarkı:{}\nSes:{}\n\n1-Şarkı Seç\n2-Ses Arttır\n"
              "3-Ses Azalt\n4-Rastgele Şarkı Seç\n5-Şarkı Ekle\n6-Şarkı Sil\n7-Kapat\n".format(self.sarkiListesi,
                                                                                               self.suanCalanSarki,
                                                                                               self.ses))

    def secim(self):
        sec = int(input("Seçiminizi Giriniz: "))
        while sec < 1 or sec > 7:
            sec = int(input("Hatalı seçim yaptınız\nSeçiminizi Giriniz: "))
        return sec

    def calistir(self):
        self.menuGoster()
        sec = self.secim()

        if sec == 1:
            self.sarkiSec()
        if sec == 2:
            self.sesArttir()
        if sec == 3:
            self.sesAzalt()
        if sec == 4:
            self.rastgeleSarkiSec()
        if sec == 5:
            self.sarkiEkle()
        if sec == 6:
            self.sarkiSil()
        if sec == 7:
            self.kapa()


mp3calar = MP3Calar()
while mp3calar.durum:
    mp3calar.calistir()
