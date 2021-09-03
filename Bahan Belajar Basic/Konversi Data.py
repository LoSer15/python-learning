born_year = input("Masukkan tahun lahir kamu ")     #kode ini akan meminta kamu utk memasukkan nilai
print(type(born_year))                              #kode ini akan menampilkan tipe data pada kode sebelumnya

born_year = int(born_year)              #kode ini akan mengubah tipe data pada variabel menjadi integer
print(type(born_year))                  #kode ini akan menampilkan tipe data pada kode sebelumnya

age = 2021 - born_year       #kode ini akan melakukan operasi pengurangan
print(type(age))             #kode ini akan menampilkan tipe data pada kode sebelumnya

print("umur kamu sekarang adalah ", age) #akan menampilkan "umur kamu sekarang adalah (umur)"

"""
catatan : konversi data pada kode baris 4 berfungsi untuk mengubah data pada kode baris 1 menjadi tipe data
          integer. Jika tidak, maka kodenya akan error dikarenakan kode yg di baris 1 menyimpan input data
          dengan tipe data string sedangkan pada kode baris 7 terjadi operasi matematika yg mengharuskan
          tipe datanya integer
"""