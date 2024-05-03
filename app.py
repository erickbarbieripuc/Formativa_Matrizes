#Atividade 1
#B

#Atividaade 2
#C

#Atividade 3
#D

#Atividade  4 
#A

# #Atividade 5 
# import numpy as np

# A = np.array([[1,2],
#               [3,4]])

# B = np.array([[0,1],
#               [-1,0]])

# C = np.dot(A,B)
# print(C)

# #Atividade prática 1
# import numpy as np
# A = np.eye(3)
# print(A)

#Atividade prática 2
# import numpy as np
# A = []
# B = []

# for i in range(2):
#     linha = []
#     for j in range(2):
#         elemento = -i + j
#         linha.append(elemento)
#     A.append(linha)
# A_np = np.array(A)

# for i in range(2):
#     linha = []
#     for j in range(2):
#         elemento = -i - j
#         linha.append(elemento)
#     B.append(linha)
# B_np = np.array(B)

# C = np.dot(A_np,B_np)
#print(C)

# #Atividade prática 3
# import numpy as np
# A = []

# for i in range (3):
#     linha = []
#     for j in range(2):
#         elemento = i * j
#         linha.append(elemento)
#     A.append(linha)
# A_np = np.array(A)

# At = np.transpose(A_np)
# print(At)

#Atividade pratica 4
# import numpy as np
# A = []
# B = []

# for i in range(2):
#     linha = []
#     for j in range(3):
#         elemento = -i - j
#         linha.append(elemento)
#     A.append(linha)
# A_np = np.array(A)

# for i in range(2):
#     linha = []
#     for j in range(3):
#         elemento = -i + j
#         linha.append(elemento)
#     B.append(linha)
# B_np = np.array(B)

# C = A_np - B_np
# print(C)

#Atividade prática 5 
import numpy as np
matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        elemento = i*i
        linha.append(elemento)
    matriz.append(linha)
matriz_np = np.array(matriz)
print("Resultado da matriz:")
print(matriz_np)


        





        


