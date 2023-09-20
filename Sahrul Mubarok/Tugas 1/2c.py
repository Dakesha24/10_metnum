# Sahrul Mubarok (2204912)
# No 2
# 3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

#library numpy untuk operasi numerik
import numpy as np
#menambah matplotlib ke dalam program untuk grafik
import matplotlib.pyplot as plt 

def my_bisection(f, a, b, e, n):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    for i in range(n):
        m = (a + b) / 2
        
        if np.abs(f(m)) < e:
            return m
            
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
            
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m
    
    last_value = (a + b) / 2
    return last_value

# Meminta user untuk memasukkan fungsi, interval, galat, dan iterasi
input_f = input("Masukkan fungsi f(x): ")
input_a = float(input("Masukkan interval bawah (a): "))
input_b = float(input("Masukkan interval atas (b): "))
input_e = float(input("Masukkan toleransi galat (e): "))
input_n = int(input("Masukkan jumlah iterasi (n): "))

# Membuat fungsi dari input pengguna
f = lambda x: eval(input_f)

# Mencari akar dengan argumen yang diinput oleh pengguna
c = my_bisection(f, input_a, input_b, input_e, input_n)
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
