# Sahrul Mubarok (2204912)
# No 2
# 1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n

import numpy as np  # Mengimpor library NumPy untuk operasi numerik

def my_bisection(f, a, b, e, n):  # Mendefinisikan fungsi pencarian akar dengan metode Bagi Dua, dengan batas iterasi ke-n
    if np.sign(f(a)) == np.sign(f(b)):  # Memeriksa apakah tanda nilai fungsi pada kedua ujung interval sama
        raise Exception('Tidak ada akar pada interval a dan b')  # Jika tanda sama, lemparkan pengecualian

    for i in range(n):
        m = (a + b) / 2  # Membagi interval menjadi dua

        if np.abs(f(m)) < e:  # Jika nilai fungsi pada tengah interval kurang dari epsilon (toleransi), maka m adalah akar hampiran
            return m

        elif np.sign(f(a)) == np.sign(f(m)):  # Jika tanda nilai fungsi pada a dan m sama
            return my_bisection(f, m, b, e, n)  # Cari akar dalam interval baru [m, b]

        elif np.sign(f(b)) == np.sign(f(m)):
            return my_bisection(f, a, m, e, n)  # Cari akar dalam interval baru [a, m]

    # Jika mencapai batas iterasi, kembalikan nilai fungsi pada iterasi terakhir
    last_value = (a + b) / 2
    return last_value


f = lambda x: x**3 - 2*x + 1  # Definisikan fungsi soal menggunakan lambda
c = my_bisection(f, -2, 5, 0.001, 100)  # Memanggil fungsi my_bisection dengan parameter yang diberikan, dengan batas iterasi ke-100
print("Akar c =", c)  # Menampilkan hasil akar yang ditemukan
print("Nilai f(c) =", f(c))  # Menampilkan nilai fungsi pada akar yang ditemukan
