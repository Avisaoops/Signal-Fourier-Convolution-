import math
import cmath
import matplotlib.pyplot as plt

# دریافت یک دوره از سیگنال
x = list(map(float, input("Enter one period of signal: ").split()))

N = len(x)

# محاسبه ضرایب DFS
C = []

for k in range(N):
    ck = 0

    for n in range(N):
        angle = -2 * math.pi * k * n / N
        ck += x[n] * complex(math.cos(angle), math.sin(angle))

    ck /= N
    C.append(ck)

# اندازه و فاز
magnitude = [abs(c) for c in C]
phase = [cmath.phase(c) for c in C]

print("Fourier Series Coefficients:")

for k in range(N):
    print(f"C[{k}] = {C[k]}")

# رسم اندازه
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.stem(range(N), magnitude)
plt.title("Magnitude Spectrum")
plt.xlabel("k")
plt.ylabel("|Ck|")

# رسم فاز
plt.subplot(2,1,2)
plt.stem(range(N), phase)
plt.title("Phase Spectrum")
plt.xlabel("k")
plt.ylabel("Phase (rad)")

plt.tight_layout()
plt.show()