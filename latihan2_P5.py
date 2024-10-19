import random

n = int(input("Masukkan jumlah n: "))

count = 0

while count < n:
    random_number = random.random()
    
    if random_number < 0.5:
        print(random_number)
        count += 1
