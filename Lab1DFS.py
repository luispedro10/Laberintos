from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import numpy as np
import queue
#Volver imagen original a un tamaño 20x20 en pixeles
imagen = Image.open('C:/Users/LUISPEDRO/Desktop/Universidad Del Valle/Semestre 7/InteligenciaArtificial/maze3.bmp')
imagenPeque = imagen.resize((20,20), Image.BILINEAR)
images=[]
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
            start_i=x

for i in range(len(matriz)):
        for x, pos in enumerate(maze[i]):
            if pos == "O":
                start_j = x

start= start_i, start_j


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
end_i, end_j= ilist[0],jlist[0]
end2_i, end2_j= ilist[1],jlist[1]


#Crear matriz binaria sin especificar fin ni comienzo, por eso se tomaron los indices en el bloque pasado. (0= Espacio) (1=Pared)
a = [
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
            a[i][j]= 1
            


#DFS
pathFinal=[]

def depth(i, j):    
    global pathFinal, end_i, end_j, a
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1:
        return 
    if (i, j) in pathFinal or a[i][j] > 0:
        return 
    pathFinal.append((i, j))
    a[i][j] = 2
    if (i, j) == (end_i, end_j):
        print("Found!",pathFinal)
        for x in pathFinal:
            i,j=x
            matriz[i][j]=[198,60,219]
        pathFinal=pathFinal
        pathFinal.pop()
        return
    #Se busca entre los vecinos.
    else:
        depth(i - 1, j)  
        depth(i + 1, j)  
        depth(i, j + 1)  
        depth(i, j - 1)  
    pathFinal.pop()
    return pathFinal

a= depth(start_i, start_j)

plt.imshow(matriz, interpolation='nearest')
plt.grid()
plt.show()



