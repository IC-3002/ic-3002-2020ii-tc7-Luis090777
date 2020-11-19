
def encontrar_ruta(C): 
      
    R = [ [ 0 for j in range(len(C[0])) ] for i in range(len(C)) ] 
      
    if encontrar_ruta_aux(maze, 0, 0, R) == False:
        return []
    return R
      

def encontrar_ruta_aux(C, x, y, R): 
      

    if x == len(C) - 1 and y == len(C[0])-1 and C[x][y]== 1: 
        R[x][y] = 1
        return True
          
    if esSeguro(C, x, y) == True:  
        R[x][y] = 1

        if encontrar_ruta_aux(C, x + 1, y, R) == True: 
            return True
              

        if encontrar_ruta_aux(C, x, y + 1, R) == True: 
            return True

        R[x][y] = 0
        return False
    
def esSeguro( C, x, y ):
    if x >= 0 and x < len(C) and y >= 0 and y < len(C[0]) and C[x][y] == 1:
        return True
      
    return False
