# Danis Keysara Saputra (2207275)
# No 1b
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# b. f(x) = e^x - x

#solusi: tidak ditemukan, fungsi tidak memotong sb.x

import numpy as np #Dengan mengimpor modul NumPy, kita dapat menggunakan fungsi dan tipe data NumPy(np) di dalam program

def my_bisection(f, a, b, e): #definisikan fungsi untuk mencari akar dari sebuah fungsi f pada interval [a, b] dengan toleransi e.
    if np.sign(f(a)) == np.sign(f(b)): #Periksa apakah ujung-ujung interval [a, b] memiliki tanda yang sama
        
        raise Exception('Tidak ada akar pada interval a dan b') #) #akan memunculkan exception dengan pesan kesalahan
        
    m = (a + b)/2 #Hitung titik tengah interval [a, b]
  
    if np.abs(f(m)) < e: #Jika nilai absolut dari fungsi f(m) kurang dari toleransi e, maka m adalah akar fungsi
        return m #Kembalikan akar fungsi m
        
    elif np.sign(f(a)) == np.sign(f(m)): #Jika kondisi tersebut terpenuhi, maka akar fungsi terletak di interval [m, b]
        return my_bisection(f,m,b,e) #interval baru = [m,b]
        
    elif np.sign(f(b)) == np.sign(f(m)): #Jika kondisi tersebut terpenuhi, maka akar fungsi terletak di interval [a, m]
        return my_bisection(f,a,m,e) #interval baru = [a,m]
            
            
f = lambda x: np.exp(x) - x #Definisi fungsi f(x), yang akan dicari akarnya
c = my_bisection(f, -2, 2, 0.01) #Panggil fungsi my_bisection() untuk mencari akar fungsi f() di interval [-2, 2] dengan toleransi 0.01
print("c = ", c) #print output
print("f(c) = ", f(c)) #print output
