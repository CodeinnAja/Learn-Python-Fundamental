#memanipulasi data string

#part 1
string1 = "halo"
string2 = " zayn"
print(string1 + string2)

#part 2
stringOne = "Universitas"
print(stringOne*3) #membuat kelipatan pda nilai string

#part 4 mengakses index di string
String1 = "Udin"
print(String1[1])
print(String1[1:3])

#part 5 mencari karakter di string dengan boolean
print("U" in String1)
print("A" not in String1)

#part 5 menghitung panjang karakter dengan len()
karakter = "fakultas"
print(len(karakter))

#part 6 mengganti kata pada suatu kalimat replace()
kalimat = "rangga suka cinta"
ganti = kalimat.replace("cinta", "dian")
print(ganti)
