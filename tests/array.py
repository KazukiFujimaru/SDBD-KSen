class ArrayADT:
    def __init__(self, ukuran, tipe_data):
        # Membuat array dengan ukuran tetap dan tipe data tertentu.
        self.isi = [None] * ukuran  # Array dengan ukuran tetap
        self.panjang = ukuran
        self.tipe_data = tipe_data  # Menyimpan tipe data yang diperbolehkan

    def set(self, index, value):
        # Menetapkan nilai pada indeks tertentu, dengan validasi tipe data.
        if 0 <= index < self.panjang:
            if isinstance(value, self.tipe_data):
                self.isi[index] = value
                print(f"Set isi[{index}] = {value}")
            else:
                print(f"Error: Nilai harus bertipe {self.tipe_data.__name__}!")
        else:
            print("Error: Indeks di luar batas!")

    def get(self, index):
        # Mengambil nilai dari indeks tertentu, jika indeks valid.
        if 0 <= index < self.panjang:
            return self.isi[index]
        else:
            print("Error: Indeks di luar batas!")
            return None

    def ukuran(self):
        # Mengembalikan ukuran array.
        return self.panjang
    
    def display(self):
        """Menampilkan isi array."""
        print(self.isi)

# Contoh penggunaan
# Membuat array integer dengan ukuran 5
arr = ArrayADT(5, int)  

# Berhasil karena sesuai tipe data
arr.set(0, 10)
arr.set(3, 20)  
arr.display()

# Gagal karena tidak sesuai tipe data
arr.set(3, "Ini String")  

# Gagal karena indeks di luar batas
arr.set(5, 50)  

# Menampilkan satu data
print("Nilai di indeks 3:", arr.get(3))

# Menampilkan panjang array
print("Ukuran array:", arr.ukuran())
