# Sahrul Mubarok (2204912)
# No 2
# 2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya

import numpy as np

def my_bisection(f, a, b, e, n):  # Mendefinisikan fungsi pencarian akar dengan metode Bagi Dua, n untuk jumlah iterasi
    if np.sign(f(a)) == np.sign(f(b)):  # Memeriksa apakah tanda nilai fungsi pada kedua ujung interval sama
        raise Exception('Tidak ada akar pada interval a dan b')  # Jika tanda sama, lemparkan pengecualian
    
    for i in range(n):  # Looping program hingga iterasi maksimal
        m = (a + b) / 2  # Membagi interval menjadi dua
        
        if np.abs(f(m)) < e:  # Jika nilai fungsi pada tengah interval kurang dari epsilon (toleransi), maka m adalah akar hampiran
            return m
            
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m  # Interval baru = [m, b]
            
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m  # Interval baru = [a, m]

    # Jika mencapai batas iterasi, kembalikan nilai fungsi pada iterasi terakhir
    last_value = (a + b) / 2
    return last_value

# Meminta user untuk memasukkan fungsi, interval, galat, dan iterasi
input_f = input("Masukkan fungsi f(x): ")
input_a = float(input("Masukkan interval bawah (a): "))
input_b = float(input("Masukkan interval atas (b): "))
input_e = float(input("Masukkan toleransi galat (e): "))
input_n = int(input("Masukkan jumlah iterasi (n): "))

# Membuat fungsi dari input pengguna
f = lambda x: eval(input_f)  # Mengevaluasi ekspresi atau kode Python yang diberikan sebagai string

# Mencari akar dengan argumen yang diinput oleh pengguna
c = my_bisection(f, input_a, input_b, input_e, input_n)  # Memanggil fungsi, dengan argumen yang diinput
print("Akar c =", c)
print("Nilai f(c) =", f(c))

