fruits = ["Jeruk",                              #pemberian variabel dan pengisian apa aja di dalam variabel tersebut
            "Nanas" ,
            "Mangga" ,
            "Anggur" ,
            "Pepaya" ,]

health = ["Healthy" , 
            "Healthier" ,
            "Health" ,
            "Health" ,
            "Healthy" ,]
    
for index,buah in enumerate(fruits) :           #enumerate digunakan untuk memberikan nomor pada saat looping
    print(index, "" ,buah)

print("=" * 100)

#menggabungkan 2 variabel atau lebih pada saat looping (zip)
for buah,healths in zip(fruits , health) :
    print(buah , "very " ,healths)

print("=" * 100)

#menyusun loopingan biar rapi
list = {"jeruk" , "mangga" , "apel" , "buah naga" , "anggur" , "salak" , "durian"} #tanda kurung kurawal membuat index jadi diacak

for buah in sorted(list) :
    print(buah)

print("-" * 100)

#mengambil data
data = { "Jeruk" : "Healthy" ,
            "Nanas" : "Healthier" ,
            "Mangga" : "Health" ,
            "Anggur" : "Health" ,
            "Pepaya" :  "Healthy",  
        }

for database in data.keys() :           #mengambil data bagian kiri
    print(database) 

print("-" *100)

for database in data.values() :         #mengambil data bagian kanan
    print(database)

print("-" *100)

for database in data.items() :          #mengambil semua data
    print(database)

print("==" *50)

for database,x in data.items() :        #hampir mirip dengan perintah zip
    print(database, "manfaat bagi tubuh " ,x)

print("=" *100)

#looping di dalam looping
fruits = ["Jeruk",
            "Nanas" ,
            "Mangga" ,
            "Anggur" ,
            "Pepaya" ,]

health = ["Healthy" , 
            "Healthier" ,
            "Health" ,
            "Health" ,
            "Healthy" ,]

vegetab = ["Bayam" , "Wortel" , "Kangkung" , "Daun Singkong" , "Daun Pepaya", "Tomat"]

typeOf_Food = [fruits , health , vegetab] 

for JenisMakan in typeOf_Food:
    print(JenisMakan)
    for subJenisMakan in JenisMakan:
        print(subJenisMakan)