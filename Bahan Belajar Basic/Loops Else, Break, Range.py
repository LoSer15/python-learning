for i in range(0,10,3):                 #fungsi range untuk nge-loop banyaknya angka 
    print(i)                            #di sini akan nge-loop mulai dari 0 sampai 9 

print("++" *50)

angks = 10                                   #program akan meminta tolong untuk mencari nilai

for i in range(1,101):                      #banyaknya angka yang akan di loop
    print(i)

    if i is angks:                          
        print("lah dapat jok",i)
        break                               #ketika udah dapat angkanya maka program langsung berhenti nge-loop
else:                                       
    print("tak dapat jok haye")             #kalau tidak dapat maka program akan ke 'else' 