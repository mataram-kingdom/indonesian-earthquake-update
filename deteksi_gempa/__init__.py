import none as none
import requests as requests
from bs4 import BeautifulSoup


class GempaTerkini:
    def __init__(self):
        self.description = "to get latest information of earthquake in indonesian from BMKG.go.id "
        self.result = None

    def ekstraksi_data(self):


        try:
            r = requests.get('https://www.bmkg.go.id/')
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

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()

if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini()
    print(f"\ndeskripsi : {gempa_di_indonesia.description}\n")
    gempa_di_indonesia.run()

    # gempa_di_indonesia.tampilkan_data()
    # gempa_di_indonesia.ekstraksi_data()
