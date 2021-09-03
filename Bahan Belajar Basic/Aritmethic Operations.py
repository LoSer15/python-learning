a = 17
b = 9

#operasi penjumlahan (+)
result = a + b
print(a, "+" , b, "=",result)

print("=" *100)

#operasi pengurangan (-)
result = a - b
print(a, "-" , b, "=" , result)

print("=" *100)

#operasi perkalian (*)
result = a * b
print(a, "*" , b, "=" , result)


print("=" *100)

#operasi pembagian (/)
result = a / b
print(a, "/" , b, "=" , result)


print("=" *100)

#operasi eksponen -pangkat- (**)
result = a ** b
print(a, "**" , b, "=" , result)


print("=" *100)

#operasi modulus -sisa dari pembagian- (%)
result = a % b
print(a, "%" , b, "=" , result)


print("=" *100)

#operasi floor division -pembulatan kebawah- (//)
result = a // b
print(a, "//" , b , "=" , result)

print("=" *100)

#operasi prioritas (menyesuaikan kaidah kabataku -kali, bagi, tambah, kurang-)
"""
    urutan yang menjadi prioritas dihitung lebih dulu
        - ( ) 
        - eksponen
        - perkalian
        - pembagian
        - modulus
        - floor division
        - penjumlahan
        - pengurangan
"""
a = 10
b = 100
c = 50

result = a+ b - c ** c // a +  b % a * c / a
print("a + b - c ** c // a +  b * c / a = ", result)