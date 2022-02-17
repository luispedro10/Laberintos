from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import queue
#Volver imagen original a un tamaño 20x20 en pixeles
imagen = Image.open('C:/Users/LUISPEDRO/Desktop/Universidad Del Valle/Semestre 7/InteligenciaArtificial/maze3.bmp')
imagenPeque = imagen.resize((20,20), Image.BILINEAR)

#--COMIENZA DISCRETIZACION DE IMAGEN--"

#Mostrar imagen original  
imagen.show()

#Imagen a Matriz
#Mostrar imagen 20x20
matriz = np.array(imagenPeque)
plt.imshow(matriz, interpolation='nearest')
plt.grid()
plt.show()


#Volver los cuadros negras totalmente negros
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][0]<99:
            matriz[i][j]=[0,0,0]
                       
#Volver los cuadros grises a cuadros blancos
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][0] == matriz[i][j][1] and not matriz[i][j][0] == 0:
            matriz[i][j]=[255,255,255]
            
#Volver cuadros verdes totalmente verdes
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][1] >= 221 and not matriz[i][j][2] > 209:
            matriz[i][j]=[0,255,0]
#Eliminar cuadros verdes repetidos sin son vecinos
            if matriz[i][j-1][1] and not matriz[i][j-1][2] > 209:
                matriz[i][j-1]=[255,255,255]
            if matriz[i][j+1][1] and not matriz[i-1][j][2] > 209:
                matriz[i][j+1]=[255,255,255]
            if matriz[i-1][j][1] and not matriz[i-1][j][2] > 209:
                matriz[i-1][j]=[255,255,255]
            if matriz[i+1][j][1] and not matriz[i+1][j][2] > 209:
                matriz[i+1][j]=[255,255,255]
                


            
#Volver cuadros rojos totalmente rojos
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][0] > 224 and not matriz[i][j][2] >= 202 and not matriz[i][j][1] > 208:
            matriz[i][j]=[255,0,0]            
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][0] > 254 and not matriz[i][j][2] >= 163: 
            matriz[i][j]=[255,0,0]            
    
#Limpiar Sonido Alrededor de cuadros rojos y verdes
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j][2] > 10 and not matriz[i][j][2] > 252:
            matriz[i][j]=[255,255,255]

#Mostrar imagen limpia
plt.imshow(matriz, interpolation='nearest')
plt.grid()
plt.show()
#--TERMINA DISCRETIZACION DE IMAGEN--"


#--COMIENZA BREADTH FIRST SEARCH--"
#Crear una lista, para ver índices de donde se empieza y donde termina
maze = []
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
maze.append([" "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "])
#Poner un "O" donde se empieza (color rojo) y una "X" donde se debe llegar
for i in range(len(maze)):
    for j in range(len(maze)):
        if matriz[i][j][0] == 255 and matriz[i][j][1] == 0:
            maze[i][j]= "O"
        if matriz[i][j][1] == 255 and matriz[i][j][0] == 0:
            maze[i][j]= "X"

#Encontrar índice de inicio
for x, pos in enumerate(maze):
        if "O" in pos:
            istart=x

for i in range(len(matriz)):
        for x, pos in enumerate(maze[i]):
            if pos == "O":
                jstart = x

start= istart, jstart


#Encontrar indice de final
ilist=[]
for x, pos in enumerate(maze):
    if "X" in pos:     
        ilist.append(x)
        
jlist=[]
for i in range(len(matriz)):
    for x, pos in enumerate(maze[i]):
         if pos == "X":
            jlist.append(x)

#Ambos finales
end1= ilist[0],jlist[0]
end2= ilist[1],jlist[1]

#Crear matriz binaria sin especificar fin ni comienzo, por eso se tomaron los indices en el bloque pasado. (0= Espacio) (1=Pared)
lab = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#Poner "1" donde hay paredes
for i in range(len(maze)):
    for j in range(len(maze)):
        if matriz[i][j][0] == 0 and matriz[i][j][1] == 0:
            lab[i][j]= 1
        




#Crear matriz para resolver laberinto
m = []
for i in range(len(lab)):
    m.append([])
    for j in range(len(lab[i])):
        m[-1].append(0)
i,j = start
m[i][j] = 1


#Se hacen los pasos validos (Referencia: https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1)
def paso(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and lab[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and lab[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and lab[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and lab[i][j+1] == 0:
           m[i][j+1] = k + 1

#Encontrando final Número 1.     
k1 = 0
while m[end1[0]][end1[1]] == 0: 
    k1 += 1
    paso(k1)
    
i, j = end1
k1 = m[i][j]
pathEnd1 = [(i,j)]
while k1 > 1:
    if i > 0 and m[i - 1][j] == k1-1:
        i, j = i-1, j
        pathEnd1.append((i, j))
        k-=1
    elif j > 0 and m[i][j - 1] == k1-1:
        i, j = i, j-1
        pathEnd1.append((i, j))
        k1-=1
    elif i < len(m) - 1 and m[i + 1][j] == k1-1:
        i, j = i+1, j
        pathEnd1.append((i, j))
        k1-=1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k1-1:
        i, j = i, j+1
        pathEnd1.append((i, j))
        k1 -= 1
#Encontrando final 2        
k2 = 0
while m[end2[0]][end2[1]] == 0: 
    k2 += 1
    paso(k2)
    
i, j = end2
k2 = m[i][j]
pathEnd2 = [(i,j)]
while k2 > 1:
    if i > 0 and m[i - 1][j] == k2-1:
        i, j = i-1, j
        pathEnd2.append((i, j))
        k2-=1
    elif j > 0 and m[i][j - 1] == k2-1:
        i, j = i, j-1
        pathEnd2.append((i, j))
        k2-=1
    elif i < len(m) - 1 and m[i + 1][j] == k2-1:
        i, j = i+1, j
        pathEnd2.append((i, j))
        k2-=1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k2-1:
        i, j = i, j+1
        pathEnd2.append((i, j))
        k2 -= 1
#Escogiendo el final mas corto        
    if len(pathEnd1)<len(pathEnd2):
        pathFinal=pathEnd1
    elif len(pathEnd2)<len(pathEnd1):
        pathFinal=pathEnd2
    elif len(pathEnd2)==len(pathEnd1):
        pathFinal=pathEnd2

#Cambiando el color del camino a rosado
for x in pathFinal:
    i,j=x
    matriz[i][j]=[198,60,219]    
   
   




    
    
    

#Imprimir resultado final
plt.imshow(matriz, interpolation='nearest')
plt.grid()
plt.show()
#--TERMINA BREADTH FIRST SEARCH-"



 
 
 

           



