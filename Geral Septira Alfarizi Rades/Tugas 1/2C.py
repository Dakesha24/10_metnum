# No 2
# 3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

import numpy as np #Dengan mengimpor modul NumPy, kita dapat menggunakan fungsi dan tipe data NumPy(np) di dalam program
import matplotlib.pyplot as plt #impor matplotlib ke dalam program untuk grafik

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
#output
print("Akar (c) =", c)

# Membuat grafik fungsi
x = np.linspace(input_a, input_b, 400) #menghasilkan array antara interval untuk mendefinisikan nilai x pada grafik
y = f(x) #mengevaluasi f(x) pada setiap 'x' dalam array yg dihasilkan, untuk mendefinikan nilai y pada grafik 

plt.plot(x, y, label='f(x)') #untuk menghubungkan titik-titik data pada sumbu x dan y, lalu diberi label f(x) untuk memberikan informasi tambahan
plt.axhline(0, color='black', linewidth=0.5) #garis horizontal, 0=posisi; color=warna garis; linewidth=tebalgaris
plt.axvline(0, color='black', linewidth=0.5)  #garis vertikal, 0=posisi; color=warna garis; linewidth=tebalgaris
plt.axvline(c, color='red', linestyle='--', label=f'Akar (x={c:.4f})') #garis vertikal, c=posisigaris(akar hampiran); color:warna_garis; linestyle:gaya_garis; label=untuk memberi informasi akar yang ditemukan, dengan 4 angka belakang koma
plt.legend() #menambahkan legend (keterangan) pada grafik
plt.title('Hasil Grafik, Pencarian Akar') #judul grafik
plt.xlabel('x') #menambahkan label pada sumbu x
plt.ylabel('f(x)') #menambahkan label pada sumbu y

plt.show() #menampilkan grafik
