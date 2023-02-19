import none as none
import requests as requests
from bs4 import BeautifulSoup
"""
method              = fungsi
field / attribute   = variabel
constructor         = method pertama kali yang dipanggil saat object diciptakan . gunakan untuk 
                        mendeklarasiakn semua field pada kelas ini
"""

class Bencana:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url
    def scrapping_data(self):
        pass
    def tampilkan_data(self):
        pass
    def keterangan(self):
        print(self.description)
    def run(self):
        self.scrapping_data()
        self.tampilkan_data()



class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, "to get latest information of earthquake in indonesian from BMKG.go.id ")
    def scrapping_data(self):


        try:
            r = requests.get(self.url)
        except  Exception:
            return None
        if r.status_code == 200 :
            # print(r.text)
            # print(r.status_code)

            soup = BeautifulSoup(r.text,'html.parser')

            result = soup.findChild('ul', {'class':'list-unstyled'})
            result = result.findChildren('li')
            print(f'============ list pencaian : ==============\n')
            j = 0
            mag = None
            dalam = None
            koordinat = None
            lokasi = None
            ket = None

            for i in result:
                # print(j,i)
                if j == 1:
                    mag = i.text
                elif j == 2:
                    dalam = i.text
                elif j ==3:
                    koordinat = i.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif j == 4:
                    lokasi = i.text
                elif j ==5:
                    ket = i.text
                j = j +1

            title = soup.find('title')
            tanggal = soup.find('span',{'class': 'waktu'})
            waktu = tanggal.text.split(', ')[1]
            # mag = soup.find('ul',{'class': 'list-unstyled'})
            print(title.string)
            print("\n===========================================\n")



            hasil = dict()
            hasil['tanggal'] = tanggal.text
            hasil['waktu'] = waktu
            hasil['mag'] = mag
            hasil['kedalaman'] = dalam
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = ket

            self.result = hasil
            print("=================================")
        else:
            return None


    def tampilkan_data(self):
        if self.result is None :
            print("tidak bisa menemukan data apapun")
            return

        print("gempa berdasarkan bmkg")
        print(f'tanggal \t : {self.result["tanggal"]}')
        print(f'waktu \t\t : {self.result["waktu"]}')
        print(f'magnitudo \t : {self.result["mag"]}')
        print(f'kedalaman \t : {self.result["kedalaman"]}')
        print(f'koordinat \t : LS : {self.result["koordinat"]["ls"]}, BT: {self.result["koordinat"]["bt"]}')
        print(f'lokasi \t\t : {self.result["lokasi"]}')
        print(f'ket \t\t : {self.result["dirasakan"]}')

class BanjirTerkini(Bencana):

    def tampilkan_data(self):
        if self.result is None:
            print(f"BANJIR | data banjir terkini di Indonesia")

    def keterangan(self):
        print(f"Info mengenai banjir : {self.description}")
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url, "NOT YET IMPLEMENTED")

if __name__ == '__main__':

    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id/')
    gempa_di_indonesia.keterangan()
    # print(f"\ndeskripsi : {gempa_di_indonesia.description}\n")
    gempa_di_indonesia.run()

    banjir_di_indonesia = BanjirTerkini('NOT YET')
    banjir_di_indonesia.keterangan()
    # print(f"\ndeskripsi : {banjir_di_indonesia.description}")
    banjir_di_indonesia.run()

    daftar_bencana = [gempa_di_indonesia, banjir_di_indonesia]
    print("\nsemua bencana yang ada =================")
    for Bencana in daftar_bencana :
        Bencana.keterangan()



