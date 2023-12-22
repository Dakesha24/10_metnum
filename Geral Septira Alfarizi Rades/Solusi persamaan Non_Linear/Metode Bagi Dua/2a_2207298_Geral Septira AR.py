# No 2
# 1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n

import numpy as np #library numpy untuk operasi numerik

def my_bisection(f, a, b, e, n): #definisikan fungsi untuk mencari akar, n untuk jumlah iterasi
    if np.sign(f(a)) == np.sign(f(b)): #meriksa apakah tanda nilai fungsi sam
        raise Exception('Tidak ada akar pada interval a dan b') #eksekusi jika tanda sama
        
    for i in range(n):
        m = (a + b)/2 #eksekusi jika syarat terpenuhi, membagi interval jadi 2
        
        if np.abs(f(m)) < e: #jika terepenuhi, m akar hampiran
            return m
            
        elif np.sign(f(a)) == np.sign(f(m)): #jika tanda nilai sama
            return my_bisection(f, m, b, e, n) #interval baru = [m,b]
            
        elif np.sign(f(b)) == np.sign(f(m)): 
            return my_bisection(f, a, m, e, n)
        
    #jika mencapai batas iterasi, kembalikan nilai fungsi pada iterasi terakhir
    last_value = (a + b) / 2 
    return last_value
    
            
f = lambda x: x**3 - 2*x + 1 #definisikan fungsi soal menggunakan lambda
c = my_bisection(f, -2, 5, 0.001, 0) #memanggil fungsi, dengan argumen yang diberikan
print("c = ", c)
print("f(c) = ", f(c))
