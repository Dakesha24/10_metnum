# Danis Keysara Saputra (2207275)
# No 1
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# a. f(x) = x^3 - 2x + 1

import numpy as np #library numpy untuk operasi numerik

def my_bisection(f, a, b, e): #definisikan fungsi untuk mencari akar, beri parameternya
    if np.sign(f(a)) == np.sign(f(b)): #meriksa apakah tanda nilai fungsi sama
        
        raise Exception('Tidak ada akar pada interval a dan b') #eksekusi jika tanda sama
        
    m = (a + b)/2 #eksekusi jika syarat terpenuhi, membagi interval jadi 2
        
    if np.abs(f(m)) < e: #jika terepenuhi, m akar hampiran
        return m
        
    elif np.sign(f(a)) == np.sign(f(m)): #jika tanda nilai sama
        return my_bisection(f,m,b,e) #interval baru = [m,b]
        
    elif np.sign(f(b)) == np.sign(f(m)): 
        return my_bisection(f,a,m,e) #interval baru = [a,m]
            
            
f = lambda x: x**3 - 2*x + 1 #definisikan fungsi soal menggunakan lambda
c = my_bisection(f, -2, 2, 0.01) #memanggil fungsi, dengan argumen yang diberikan
print("c = ", c)
print("f(c) = ", f(c))
