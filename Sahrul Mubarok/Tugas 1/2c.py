# Sahrul Mubarok (2204912)
# No 2
# 3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

# Import library NumPy untuk operasi numerik
import numpy as np
# Import library Matplotlib untuk membuat grafik
import matplotlib.pyplot as plt 

# Definisikan fungsi my_bisection untuk mencari akar fungsi
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

# Meminta input dari pengguna: fungsi, interval, galat, dan iterasi
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
x = np.linspace(input_a, input_b, 400) # Menghasilkan array yang berisi nilai x dalam interval
y = f(x) # Menghitung nilai y untuk setiap x dalam array

plt.plot(x, y, label='f(x)') # Menampilkan grafik fungsi f(x)
plt.axhline(0, color='black', linewidth=0.5) # Garis horizontal pada y=0
plt.axvline(0, color='black', linewidth=0.5) # Garis vertikal pada x=0
plt.axvline(c, color='red', linestyle='--', label=f'Akar (x={c:.4f})') # Garis vertikal pada x=c (akar) dengan label
plt.legend() # Menampilkan legenda pada grafik
plt.title('Grafik Fungsi dan Pencarian Akar') # Judul grafik
plt.xlabel('x') # Label sumbu x
plt.ylabel('f(x)') # Label sumbu y

plt.show() # Menampilkan grafik

