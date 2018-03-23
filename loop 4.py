#Segitiga

a = ""
bar = 1
x = 5
# Looping Baris
while bar <= x:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 1:
        a= a+ "   "
        kol = kol - 1
    # Looping Kolom Bintang
    kanan = 0
    while kanan <= (x - bar):
        a = a + " * "
        kanan = kanan + 1
    a= a + "\n"
    bar = bar + 1
print(a)