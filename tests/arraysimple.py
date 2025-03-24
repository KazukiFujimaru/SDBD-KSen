array = []
tipe_data = str

def ukuran_array(ukuran):
    global array 
    array = [None] * ukuran

def tambah_data(index, isi):
    global array
    if isinstance(isi, tipe_data) :
        if index >= 0 and  index < len(array):
            array[index] = isi
        else:
            print(f"Index {index} diluar batas ukuran array")
    else:
        print(f"Data {isi} bukan {tipe_data.__name__}")

def ambil_data(index):
    global array
    if index >= 0 and  index < len(array):
        print(array[index])
    else:
        print(f"Index {index} diluar batas ukuran array")

def cek_ukuran():
    global array
    print(f"Ukuran array : {len(array)}")

# Penggunaan
ukuran_array(5)  # Ukuran Array = 5
tambah_data(2, "Alina")  # Data berhasil
tambah_data(7, "Yuuka")  # Data Gagal, diluar index
tambah_data(1, 12) # Data gagal, tipe data berbeda
print(array)  # Mengeluarkan output 
print(ambil_data(2))  # Output: Alina
cek_ukuran()  # Output: 5
