# No 2
# 2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya

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


# Meminta user untuk memasukkan fungsi, interval, galat, dan iterasi
# Input fungsi
input_f = input("Masukkan fungsi f(x): ")
# Input interval
input_a = float(input("Masukkan interval bawah (a): "))
input_b = float(input("Masukkan interval atas (b): "))
# Input toleransi galat
input_e = float(input("Masukkan toleransi galat (e): "))
# Input jumlah iterasi
input_n = int(input("Masukkan jumlah iterasi (n): "))

# Membuat fungsi dari input pengguna
# Menggunakan fungsi lambda untuk membuat fungsi sederhana
f = lambda x: eval(input_f)

# Mencari akar dengan argumen yang diinput oleh pengguna
c = my_bisection(f, input_a, input_b, input_e, input_n)

# Output
print("c =", c)
print("f(c) =", f(c))

