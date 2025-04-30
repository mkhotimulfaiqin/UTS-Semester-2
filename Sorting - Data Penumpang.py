# Data penumpang per bus
tahunpertama = [30, 30, 30]    # 3 bus masing-masing 30 penumpang
tahunkedua = [25, 25, 25]   # 3 bus masing-masing 25 penumpang

# Gabungkan semua data penumpang
data_penumpang = tahunpertama + tahunkedua

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    kiri  = [x for x in arr[1:] if x <= pivot]
    kanan = [x for x in arr[1:] if x > pivot]
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)

# Urutkan data
data_terurut = quick_sort(data_penumpang)

# Hitung total per bulan
total_pertama = sum(tahunpertama)
total_kedua = sum(tahunkedua)

# Tampilkan hasil
print("Data penumpang sebelum diurutkan:", data_penumpang)
print("Data penumpang setelah diurutkan :", data_terurut)
print(f"Total penumpang tahun pertama : {total_pertama}")
print(f"Total penumpang tahun kedua: {total_kedua}")

# Tentukan bulan dengan penumpang lebih banyak
if total_pertama > total_kedua:
    print("tahun pertama memiliki lebih banyak penumpang.")
elif total_kedua > total_pertama:
    print("tahun kedua memiliki lebih banyak penumpang.")
else:
    print("Kedua nya memiliki jumlah penumpang yang sama.")