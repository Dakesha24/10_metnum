# No 2
# 1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n

import numpy as np #library numpy untuk operasi numerik

def my_bisection(f, a, b, e, n): #definisikan fungsi untuk mencari akar dari sebuah fungsi f pada interval [a, b] dengan toleransi e dan jumlah iterasi `n`
    if np.sign(f(a)) == np.sign(f(b)): #Periksa apakah ujung-ujung interval [a, b] memiliki tanda yang sama
        raise Exception('Tidak ada akar pada interval a dan b') #akan memunculkan exception dengan pesan kesalahan
        
    for i in range(n): # Perulangan untuk melakukan iterasi sebanyak n kali
        m = (a + b)/2 #Hitung titik tengah interval [a, b]
        
           if np.abs(f(m)) < e: #Jika nilai absolut dari fungsi f(m) kurang dari toleransi e, maka m adalah akar fungsi
        return m #Kembalikan akar fungsi m
            
        elif np.sign(f(a)) == np.sign(f(m)): #Jika kondisi tersebut terpenuhi, maka akar fungsi terletak di interval [m, b]
            return my_bisection(f, m, b, e, n) #interval baru = [m,b]
            
        elif np.sign(f(b)) == np.sign(f(m)): #Jika kondisi tersebut terpenuhi, maka akar fungsi terletak di interval [a, m]
            return my_bisection(f, a, m, e, n) #interval baru = [a, m]
        
    #jika mencapai batas iterasi, kembalikan nilai fungsi pada iterasi terakhir
    last_value = (a + b) / 2 
    return last_value
    
            
f = lambda x: x**3 - 2*x + 1 #Definisi fungsi f(x), yang akan dicari akarnya
c = my_bisection(f, -2, 5, 0.001, 0) #Panggil fungsi my_bisection() untuk mencari akar fungsi f() di interval [-2, 2] dengan toleransi 0.01
print("c = ", c) #output
print("f(c) = ", f(c)) #output
