# Sahrul Mubarok (2204912)
# No 1b
# Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
# b. f(x) = e^x - x

#solusi: tidak ditemukan, fungsi tidak memotong sb.x

import numpy as np  # Mengimpor library NumPy untuk operasi numerik

def my_bisection(f, a, b, e):  # Mendefinisikan fungsi pencarian akar dengan metode Bagi Dua
    if np.sign(f(a)) == np.sign(f(b)):  # Memeriksa apakah tanda nilai fungsi pada kedua ujung interval sama

        raise Exception('Tidak ada akar pada interval a dan b')  # Jika tanda sama, lemparkan pengecualian

    m = (a + b) / 2  # Membagi interval menjadi dua

    if np.abs(f(m)) < e:  # Jika nilai fungsi pada tengah interval kurang dari epsilon (toleransi), maka m adalah akar hampiran
        return m

    elif np.sign(f(a)) == np.sign(f(m)):  # Jika tanda nilai fungsi pada a dan m sama
        return my_bisection(f, m, b, e)  # Cari akar dalam interval baru [m, b]

    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)  # Cari akar dalam interval baru [a, m]

f = lambda x: np.exp(x) - x  # Definisikan fungsi soal menggunakan lambda
c = my_bisection(f, -2, 2, 0.01) # Memanggil fungsi my_bisection dengan parameter yang diberikan
print("Akar c =", c)  # Menampilkan hasil akar yang ditemukan
print("Nilai f(c) =", f(c))  # Menampilkan nilai fungsi pada akar yang ditemukan
