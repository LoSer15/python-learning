celcius = float(input("Masukkan Suhu Celcius "))

#konversi celcius ke reamur
reamur = (4/5) * celcius

#konversi celcius ke kelvin
kelvin = celcius + 273

#konversi celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32

print("Suhu dalam Reamur adalah ", reamur , "R")
print("Suhu dalam Kelvin adalah ", kelvin , "K")
print("Suhu dalam Fahrenheit adalah ", fahrenheit , "F")

print("=" * 100)

reamur = float(input("Masukkan Suhu Reamur "))

#konversi reamur ke celcius
celcius = (5/4) * reamur

#konversi reamur ke kelvin
kelvin = ((5/4) * reamur) + 273

#konversi reamur ke fahrenheit
fahrenheit = ((9/4) * reamur) +32

print("Suhu dalam Celcius adalah ", celcius , "C")
print("Suhu dalam Kelvin adalah ", kelvin , "K")
print("Suhu dalam Fahrenheit adalah ", fahrenheit , "F")

print("=" *100)

fahrenheit = float(input("Masukkan Suhu Fahrenheit "))

#konversi fahrenheit ke celcius
celcius = 5/9 * (fahrenheit - 32) 

#konversi fahrenheit ke reamur
reamur = 4/9 * (fahrenheit - 32)

#konversi fahrenheit ke kelvin
kelvin = (5/9 * (fahrenheit - 32)) + 273

print("Suhu dalam Celcius adalah ", celcius , "C")
print("Suhu dalam Reamur adalah ", reamur , "R")
print("Suhu dalam Kelvin adalah ", kelvin , "K")

print("=" *100)

kelvin = float(input("Masukkan Suhu Kelvin "))

#konversi kelvin ke celcius
celcius = kelvin + 273

#konversi kelvin ke reamur
reamur = 4/5 * (kelvin - 273)

#konversi kelvin ke fahrenheit
fahrenheit = (9/5 * (kelvin - 273)) + 32

print("Suhu dalam Celcius adalah ", celcius , "C")
print("Suhu dalam Reamur adalah ", reamur , "R")
print("Suhu dalam Fahrenheit adalah ", fahrenheit , "F")