#logika dalam operator di boolean
"""
    == (sama dengan)
    != (tidak sama dengan)
    <  (kecil dari)
    >  (besar dari)
    <= (kecil dari atau sama dengan)
    >= (besar dari atau sama dengan)
"""

a = "a" == "a"
b = "12" != "10"
c = "100" > "1000"
d = "100" < "10"
e = "12" >= "12345"
f = "1234" <= "1234"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#Operator perbandingan berantai
"""
    and     (untuk menghasilkan nilai true maka dua kondisi harus benar)
    or      (untuk menghasilkan nilai true maka salah satu kondisi harus benar)
    not     (untuk mengubah kesimpulan antara dua operator)
"""

A = 3 > 2 and 4 < 2
B = 4 < 3 or 10 > 2
C = not (B)
D = not (A)

print(A)    #akan menghasilkan nilai False dikarenakan salah satu kondisi ada yang salah
print(B)    #akan menghasilkan nilai True dikarenakan disalah satu kondisi ada yang benar
print(C)    #akan menghasilkan nilai False dikarenakan nilai sebelumnya yg mulanya menghasilkan nilai True 
            #maka dengan kode "not" nilai tersebut akan berubah
print(D)    #akan menghasilkan nilai True dikarenakan nilai sebelumnya yg mulanya menghasilkan nilai False 
            #maka dengan kode "not" nilai tersebut akan berubah