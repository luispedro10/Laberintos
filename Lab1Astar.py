from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from queue import PriorityQueue
#Volver imagen original a un tamaño 20x20 en pixeles
imagen = Image.open('C:/Users/LUISPEDRO/Desktop/Universidad Del Valle/Semestre 7/InteligenciaArtificial/maze5.jpg')
imagenPeque = imagen.resize((20,20), Image.BILINEAR)

#--COMIENZA DISCRETIZACION DE IMAGEN--"

#Mostrar imagen original  
#imagen.show()

#Imagen a Matriz
#Mostrar imagen 20x20
matriz = np.array(imagenPeque)
#plt.imshow(matriz, interpolation='nearest')
#plt.grid()
#plt.show()


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
plt.imshow(matriz, interpolation='nearest')

plt.show()

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
            


           
#Haciendo nested dictionary y grid para el laberinto
nested={}
grid=[]
for i in range (1,21):
    for j in range(1,21):
        grid.append((j,i))

for i in grid:
    nested[i]= {'E':0,'W': 0, 'N': 0, 'S': 0}

#Especificando Esquinas y Bordes 
for x in grid:
    i,j=x
    if lab[i-1][j-1]==0:
        if i==1 and j==1:
            if lab[i-1][j]==0:
                nested[(i,j)]['W']=1
            if lab[i][j-1]==0:
                nested[(i,j)]['S']=1
        elif i==20 and j==20:
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1
            if lab[i-1][j-2]==0:
                nested[(i,j)]['E']=1
        elif i==1 and j==20:
            if lab[i][j-1]==0:
                nested[(i,j)]['W']=1
            if lab[i-1][j-2]==0:
                nested[(i,j)]['S']=1
        elif i==20 and j==1:
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1
            if lab[i-1][j]==0:
                nested[(i,j)]['E']=1
        elif j==1:
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1
            if lab[i][j-1]==0:
                nested[(i,j)]['S']=1
            if lab[i-1][j]==0:
                nested[(i,j)]['E']=1
        elif j==20:
            if lab[i][j-1]==0:
                nested[(i,j)]['S']=1
            if lab[i-1][j-2]==0:
                nested[(i,j)]['W']=1
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1
        elif i==1:
            if lab[i-1][j-2]==0:
                nested[(i,j)]['W']=1
            if lab[i-1][j]==0:
                nested[(i,j)]['E']=1
            if lab[i][j-1]==0:
                nested[(i,j)]['S']=1
        elif i==20:
            if lab[i-1][j-2]==0:
                nested[(i,j)]['W']=1
            if lab[i-1][j]==0:
                nested[(i,j)]['E']=1
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1
        else:
            if lab[i-1][j-2]==0:
                nested[(i,j)]['W']=1
            if lab[i-1][j]==0:
                nested[(i,j)]['E']=1
            if lab[i][j-1]==0:
                nested[(i,j)]['S']=1
            if lab[i-2][j-1]==0:
                nested[(i,j)]['N']=1


    


def heuristica(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)


#A STAR #Referencia: https://levelup.gitconnected.com/a-star-a-search-for-solving-a-maze-using-python-with-visualization-b0cae1c3ba92
startMaze=(start)
g_score={cell:float('inf') for cell in grid}
g_score[start]=0
f_score={cell:float('inf') for cell in grid}
f_score[start]=heuristica(start,(1,1))

open=PriorityQueue()
open.put((heuristica(start,(1,1)),heuristica(start,(1,1)),start))
aPath={}
    
while not open.empty():
        currCell=open.get()[2]
        if currCell==(end1):
            break
        for d in 'ESNW':
            if nested[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+heuristica(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,heuristica(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
fwdPath={}
cell=(end1)

#Mientras no lleguemos a la meta...
while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]



#Pintar el camino de Rosado
for x in fwdPath:
    i,j=x
    matriz[i][j]=[198,60,219]

#Mostrar imagen limpia
plt.imshow(matriz, interpolation='nearest')
plt.grid()
plt.show()







