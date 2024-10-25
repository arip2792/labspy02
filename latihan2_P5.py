import random

# Meminta input n dari pengguna
n = int(input("Masukkan jumlah n: "))

# Inisialisasi penghitung
count = 0

# Loop while untuk memastikan menghasilkan n bilangan acak
while count < n:
    # Generate bilangan acak antara 0 dan 1
    random_number = random.random()
    
    # Jika bilangan acak lebih kecil dari 0.5, cetak dan tambahkan count
    if random_number < 0.5:
        print(random_number)
        count += 1
