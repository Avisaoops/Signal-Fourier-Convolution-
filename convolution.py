import matplotlib.pyplot as plt

# دریافت سیگنال ها
x = list(map(float, input("Enter first signal (space separated): ").split()))
h = list(map(float, input("Enter second signal (space separated): ").split()))

N = len(x)
M = len(h)

# محاسبه کانولوشن
y = [0] * (N + M - 1)

for n in range(N + M - 1):
    for k in range(N):
        if 0 <= n - k < M:
            y[n] += x[k] * h[n - k]

print("Convolution Result:")
print(y)

# رسم نمودارها
plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.stem(range(N), x)
plt.title("Signal x[n]")

plt.subplot(3,1,2)
plt.stem(range(M), h)
plt.title("Signal h[n]")

plt.subplot(3,1,3)
plt.stem(range(len(y)), y)
plt.title("Convolution y[n]")

plt.tight_layout()
plt.show()