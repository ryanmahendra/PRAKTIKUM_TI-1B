
import random

# matriks dengan angka random 1-10
A = [[random.randint(1, 10) for j in range(2)] for i in range(2)]
B = [[random.randint(1, 10) for j in range(2)] for i in range(2)]

# Pengurangan matriks
hasil = []

for i in range(2):
    baris = []
    for j in range(2):
        baris.append(A[i][j] - B[i][j])
    hasil.append(baris)

# Menampilkan hasil
print("Matriks A:")
for baris in A:
    print(baris)

print("\nMatriks B:")
for baris in B:
    print(baris)

print("\nHasil Pengurangan:")
for baris in hasil:
    print(baris)
