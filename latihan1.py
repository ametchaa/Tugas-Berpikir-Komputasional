# Program menghitung jarak (s)
# Latihan menerapkan operator aritmatika

# KAMUS
# s : jarak : float             satuan dalam (m)
# v : kecepatan : float         satuan dalam (m/s)
# t : waktu : float             satuan dalam (s)

# Algoritma
v = float(input('Masukkan nilai kecepatan '))
t = float(input('Masukkan nilai waktu '))

s = v * t
print("Maka jaraknya adalah " + str(s) + " meter")