import numpy as np

bilangan = [2,4,6,8,10,12]
for angka in bilangan:
    print(angka)
print("____")
for index, angka in enumerate(bilangan):
    print("index" + str(index) + " = " + str(angka))

profil = {"ersan":"Data Analyst",
          "fernando":"Data Scientist",
          "samjaya":"Data Engineer"}
for k,v in profil.items(): #jika menggunakan dictionary, menggunakan method .items()
    print(str(k) + " sebagai "+ str(v))
print("__________")
np_tinggi = np.array([170,171,172,173,174,176])
np_berat = np.array([60,61,60,61,69,70])
massa = (np_tinggi/np_berat) **3
for val in massa:
    print(val)
print("_________")
massa2 = np.array([np_tinggi, np_berat])
for val in massa2:
    print(val)
print("++++++++")
for val in np.nditer(massa2): #jika menggunakan array 2d, menggunakan fungsi np.nditer
    print(val)