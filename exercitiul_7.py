S=str(input("Introduceti sirul de caractere: "))
A=0
for j in range(0,len(S)):
    x=ord(S[j])
    if x==65:
        A+=1
print("a) Numarul de aparitii ale caracterului A: ",A)
B=''
for j in S:
        B=S.replace("A","*")
print('b) Sirul obtinut prin substituirea caracterului A prin caracterul  * :' ,B )
C=''
for j in S:
    if ord(j)==66:
        C+=''
    if ord(j)!=66:
        C+=chr(ord(j))
print('c) Sirul obtinut prin radierea din sirul S a tuturor apariTiilor caracterului B: ' , C)
D=''
for j in S:
    D=S.count('MA')
print('d) Numarul de aparitii ale silabei MA in sirul S:' , D) 
E=''
for j in S:
    E=S.replace('MA','TA')
    print("e) Sirul obtinut prin substituirea silabei MA cu TA: ",E)
F=''
for j in S:
    F=S.replace('TO', '')
print('f) Sirul obtinut prin radierea din sirul S a tuturor aparitiilor silabei TO:' , F)
G=''
G=S[::-1]
print('g) Scrierea inversa a sirului S' , G)