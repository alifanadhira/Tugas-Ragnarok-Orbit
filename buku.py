# POLYMORPHISM

class buku(object):
    def __init__(self, judul, genre, tahun):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
    
    def baca(self, durasi):
        for i in range(durasi):
            print("sedang membaca..")
            
    def info(self):
        print(f"Judul Buku: {self.judul}\nGenre: {self.genre}\nTahun terbit: {self.tahun}")

        
class hardcover(buku):
    def __init__(self, judul, genre, tahun, warna, bahasa):
        super().__init__(judul, genre, tahun)
        self.warna = warna
        self.bahasa = bahasa
        
    def doing(self, durasi):
        for i in range(durasi):
            print("membaca..membuka halaman..")
            
        
class softcover(buku):
    def __init__(self, judul, genre, tahun, harga, kondisi):
        super().__init__(judul, genre, tahun)
        self.harga = harga
        self.kondisi = kondisi
        
    def fisik(self, kondisi_buku):
        if kondisi_buku == True:
            print("Buku Baru")
        else:
            print("Buku Second")