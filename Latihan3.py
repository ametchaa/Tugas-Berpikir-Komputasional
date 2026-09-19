# Program Menghitung Harga Total Pembelian Kelereng
# Banyak kelereng yang dibeli beragam

# KAMUS
# m : jumlah kelereng merah : int           m>0
# h : jumlah kelereng hijau : int           m>0
# k : jumlah kelereng kuning : int          m>0
# Harga 1 kelereng merah  : 1000
# Harga 1 kelereng hijau  : 1500
# Harga 1 kelereng kuning : 2000
# Harga : int

# Algoritma
m = int(input('Banyak kelereng merah adalah '))
h = int(input('Banyak kelereng hijau adalah '))
k = int(input('Banyak kelereng kuning adalah '))

Harga = (1000 * m) + (1500 * h) + (2000 * k)

print("Maka harga yang harus dibayarkan adalah " + "Rp" + str(Harga))