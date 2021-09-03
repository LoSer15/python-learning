#Di Python dalam penulisan program string dapat menggunakan tanda kutip ('...') dan kutip dua ("...")
name = "Dwi Suhariadi"                  #memasukkan tipe data string ke variabel
       #012345678910,11,12              #jumlah index pada string
print(name[12])                         #akan menampilkan huruf "i" saja            (arrays)
print(name[0:3])                        #akan menampilkan kata "Dwi" saja           (arrays) (slicing)
print(name[4:13])                       #akan menampilkan kata "Suhariadi" saja     (arrays) (slicing)
print(name[:])                          #akan menampilkan kata "Dwi Suhariadi"      (arrays) (slicing)

surname = 'Suhariadi'                   #string dengan tanda kutip satu ('...')
print(surname)


#Membuat string banyak baris dengan tanda kutip dua sebanyak tiga kali 
Paragraph = """
halo nama saya Dwi Suhariadi
saya tinggal di jakarta
saya sekarang kuliah
saya bosan
"""
print(Paragraph)


#Membuat string banyak baris dengan tanda kutip satu sebanyak tiga kali
Paragraph = '''
halo nama saya Dwi Suhariadi
saya tinggal di jakarta
saya sekarang kuliah
saya bosan
'''
print(Paragraph)


#Menghitung jumlah karakter pada string
Paragraph ="test tes tes tes test test tes test tes test tes test test"
print(len(Paragraph))


#Mengedit karakter/huruf pada string
yourName = "Dwi Suhariadi"
print(yourName.lower())     #mengubah kata di string menjadi huruf kecil semua
print(yourName.upper())     #mengubah kata di string menjadi huruf besar semua
print(yourName.replace("Dwi" , "Jason"))        #mengganti kata di string menjadi kata baru


#Menggabungkan string dengan tipe data angka
usia = 13
paraf = "Nama saya Dwi Suhariadi umurku {}"  #dalam string wajib menambahkan kurung kurawal "{}" untuk memasukkan tipe data angka
print(paraf.format(usia))

age = 22                                     #dihitung mulai dari angka nol
height = 177                                 #dihitung angka satu
weight = 60                                  #dihitung angka dua
text = "Halo Namaku Adi, umurku {0} berat badanku {2} dan tinggiku {1}"
print(text.format(age , height , weight))