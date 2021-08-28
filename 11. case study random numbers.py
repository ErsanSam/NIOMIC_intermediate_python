import numpy as np
print(np.random.rand()) #menghasilkan angka acak
print(np.random.seed(123))
print(np.random.rand())
print("_____")
print(np.random.rand()) #hasilnya beda dengan seed 123
print("+++++")
print(np.random.seed(123))
print(np.random.rand()) #hasilnya akan sama dengan seed 123 pertama
print("???????")
print(np.random.randint(0,2)) #menghasilkan angka random dari 0 sampai 1 #muncul angka 0
print(np.random.randint(0,2)) #0
print(np.random.randint(0,2)) #0
print(np.random.randint(0,2)) #0
print(np.random.randint(0,2)) #0
print(np.random.randint(0,2)) #muncul angka 1
print(np.random.randint(0,2))
print("_________")
print("BERMAIN DADU")
step = 50
dice = np.random.randint(1,7)
if dice <= 2:
    step -= 1
elif dice <= 5:
    step += 1
else :
    step += np.rand.randint(1,7)
print(dice)
print(step)
