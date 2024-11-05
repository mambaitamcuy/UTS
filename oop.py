class Library:
    def __init__(self):
        self._nama = "library adhlir"
        self._waktu = "07.00-10.00"
        self.__buku = []
        self.__buku_pinjaman = []

    @property
    def _get_buku(self):
        return self.__buku
    
    @_get_buku.setter
    def tambahkan_buku(self,buku):
        self.__buku.append(buku)
    
    @property
    def _get_buku_pinjaman(self):
        return self.__buku_pinjaman
    
    @_get_buku_pinjaman.setter
    def tambahkan_buku_pinjaman(self,buku):
        self.__buku_pinjaman.append(buku)


class System_library(Library):
    def __init__(self):
        super().__init__()

    def isi_buku(self):
        print("\n------ISI BUKU PERPUSTKAAN------\n")
        judul = input("masukkan judul buku : ")
        pengarang = input("masukkan nama pengarang : ")
        hal = int(input("masukkan jumlah halaman : "))
        my_book = {}
        my_book["judul"] = judul
        my_book["pengarang"] = pengarang
        my_book["halaman"] = hal 
        self.tambahkan_buku = my_book
    
    def pinjam_buku(self):
        print(f"\n---- WAKTU BUKA {self._waktu}----\n")
        jam = int(input("masukkan waktu anda ingin mengunjungi perpustakaan : "))
        if (jam < 7 or jam > 10):
            print("maaf perpustakaan sudah tutup/belum buka")
        else:
            for i,n in enumerate(self._get_buku,start=1):
                print(f"{i}. judul : {n["judul"]} -> pengarang : {n["pengarang"]} -> halaman : {n["halaman"]}")

            pilih  =  int(input("masuukkan pilihan buku yang anda ingin pinjam : "))
            if (pilih > len(self._get_buku)):
                print("maaf nomor buku yang anda pinjam tidak tersedia")
            else:
                self._get_buku_pinjaman.append(self._get_buku[pilih - 1])
                self._get_buku.pop(pilih - 1)
                print("selamat buku berhasil dipinjam")
    
    def kembalikan_buku(self):
        for i,n in enumerate(self._get_buku_pinjaman,start=1):
            print(f"{i}. judul : {n["judul"]} -> pengarang : {n["pengarang"]} -> halaman : {n["halaman"]}")

        pilih  =  int(input("masuukkan pilihan buku yang ingin dikembalikan : "))
        if (pilih > len(self._get_buku_pinjaman)):
            print("maaf nomor buku yang anda pinjam tidak tersedia")
        else:
            self._get_buku.append(self._get_buku_pinjaman[pilih - 1])
            self._get_buku_pinjaman.pop(pilih - 1)
            print("selamat buku berhasil dikembalikan")
        
    def info_buku_diperpustakaan(self):
        print("\n----DAFTAR BUKU PERPUSTAKAAN----\n")
        for i,n in enumerate(self._get_buku,start=1):
            print(f"{i}. judul : {n["judul"]} -> pengarang : {n["pengarang"]} -> halaman : {n["halaman"]}")
        print(" ")
    def info_buku_pinjaman(self):
        print("\n----DAFTAR BUKU PINJAMAN----\n")
        for i,n in enumerate(self._get_buku_pinjaman,start=1):
            print(f"{i}. judul : {n["judul"]} -> pengarang : {n["pengarang"]} -> halaman : {n["halaman"]}")
        print(" ")



obj = System_library()


menu = 0

while menu < 6:
    print("1. isi buku di perpustakaan")
    print("2. pinjam buku")
    print("3. kembalikan buku")
    print("4. daftar buku di perpustakaan")
    print("5. daftar buku pinjaman")
    print("6. keluar")
    menu = int(input("masukkan pilihan : "))
    if (menu == 1):
        obj.isi_buku()
    elif (menu == 2):
        obj.pinjam_buku()
    elif (menu == 3):
        obj.kembalikan_buku()
    elif (menu == 4):
        obj.info_buku_diperpustakaan()