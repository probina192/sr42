from random import randint
arrA=[]
arrB=[]
arrSize=int(input("Введите размерность массива A: "))
f=input("Хотите ввести элемента массива? y/n ")
if (f=="y"):
    for i in range (arrSize):
        arrA.append (int(input()))
elif (f=="n"):
    for i in range (arrSize):
        arrA.append (randint(0,100))
else:
    print ("Ошибка")
    exit ()
arrSize=int(input("Введите размерность массива B: "))
f=input("Хотите ввести элемента массива? y/n ")
if (f=="y"):
    for i in range (arrSize):
        arrB.append (int(input()))
elif (f=="n"):
    for i in range (arrSize):
        arrB.append (randint(0,100))
else:
    print ("Ошибка")
    exit ()
print ("Массив А")
print (arrA)
print ("Массив B")
print (arrB)
massive=[]
for i in range (len(arrA)):
    for g in range (len(arrB)):
        if (arrA[i]==arrB[g]):
            massive.append (arrA[i])
print ("Результат")
print (massive)
            