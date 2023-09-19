# Danis Keysara Saputra
# No 2
# 2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya

import numpy as np

def my_bisection(f, a, b, e, n): #definisikan fungsi untuk mencari akar, n untuk jumlah iterasi
    if np.sign(f(a)) == np.sign(f(b)):  #meriksa apakah tanda nilai fungsi sam
        raise Exception('Tidak ada akar pada interval a dan b')  #eksekusi jika tanda sama
    
    for i in range(n): #looping program hingga iterasi maksimal
        m = (a + b) / 2 #eksekusi jika syarat terpenuhi, membagi interval jadi 2
        
        if np.abs(f(m)) < e:  #jika terepenuhi, m akar hampiran
            return m
            
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m #interval baru = [m, b]
            
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m #interval baru = [a, m]

    #jika mencapai batas iterasi, kembalikan nilai fungsi pada iterasi terakhir
    last_value = (a + b) / 2
    return last_value

# Meminta user untuk memasukkan fungsi, interval, galat, dan iterasi
input_f = input("Masukkan fungsi f(x): ")
input_a = float(input("Masukkan interval bawah (a): "))
input_b = float(input("Masukkan interval atas (b): "))
input_e = float(input("Masukkan toleransi galat (e): "))
input_n = int(input("Masukkan jumlah iterasi (n): "))

# Membuat fungsi dari input pengguna
f = lambda x: eval(input_f) #mengevaluasi ekspresi atau kode Python yang diberikan sebagai string

# Mencari akar dengan argumen yang diinput oleh pengguna
c = my_bisection(f, input_a, input_b, input_e, input_n) #memanggil fungsi, dengan argumen yang diinput
print("c =", c)
print("f(c) =", f(c))
