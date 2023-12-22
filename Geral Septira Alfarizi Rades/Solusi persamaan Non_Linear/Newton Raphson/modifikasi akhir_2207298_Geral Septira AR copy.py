import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Meminta input dari pengguna untuk fungsi
user_input = input("Masukkan fungsi f(x): ")
x = sp.symbols('x')
f = sp.sympify(user_input)

# Menghitung turunan fungsi secara otomatis
f_prime = sp.diff(f, x)

# Meminta input dari pengguna untuk nilai awal aproksimasi
n = float(input("Masukkan Nilai Aproksimasi Awal: "))

# Meminta input dari pengguna untuk toleransi error (galat)
e = float(input("Masukkan Toleransi Error (galat): "))

# Menginisialisasi fungsi Newton-Raphson
def newton_raphson(f, df, xi, e):
    print("Nilai xi: ", xi)
    if abs(f.evalf(subs={x: xi})) < e:
        return xi
    else:
        xi = xi - f.evalf(subs={x: xi})/df.evalf(subs={x: xi})
        return newton_raphson(f, df, xi, e)

# Pemanggilan fungsi Newton-Raphson
estimate = newton_raphson(f, f_prime, n, e)
print ("Akar yang diestimasi = %.6f" % estimate)

# Plot fungsi dan estimasi akar
x_vals = np.linspace(-10, 10, 1000)
f_vals = [f.evalf(subs={x: val}) for val in x_vals]

plt.plot(x_vals, f_vals, label='f(x)')
plt.scatter(estimate, f.evalf(subs={x: estimate}), color='red', label='Estimasi Akar')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5) #garis horizontal, 0=posisi; color=warna garis; linewidth=tebalgaris
plt.axvline(0, color='black', linewidth=0.5)  #garis vertikal, 0=posisi; color=warna garis; linewidth=tebalgaris
plt.legend()
plt.title('Plot Fungsi dan Estimasi Akar')
plt.grid(True)
plt.show()
