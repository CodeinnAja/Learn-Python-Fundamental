#membuat percabangan bersarang pada python

print("Jenis-Jenis Bangun Datar : \n")
print("1.Segitiga")
print("2.Persegi")
print("3.Persegi Panjang\n")

banganDatar = input("Masukan PIlihan Bangun Datar : ")
if(banganDatar == "1"):
    print("1.Keliling Setitiga")
    print("2.Luas Segitiga \n")
    rumus = input("Masukan Pilihan Untuk Melihat Rumus : ")
    if(rumus == "1"):
        print("sisi + sisi + sisi")
    else:
        print("1/2 X alas X tinggi")
elif(banganDatar == "2"):
    print("1.Keliling Persegi")
    print("2.Luas Persegi \n")
    rumus = input("Masukan Pilihan Untuk Melihat Rumus : ")
    if (rumus == "1"):
        print("4 X sisi")
    else:
        print("sisi X sisi")
else:
    print("1.Keliling Persegi Panjang")
    print("2.Luas Persegi Panjang  \n")
    rumus = input("Masukan Pilihan Untuk Melihat Rumus : ")
    if (rumus == "1"):
        print("2 X (panjang + lebar)")
    else:
        print("panjang X lebar")