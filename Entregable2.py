def recorrido_especial(A1, A2, M, m = 0, n = 0, direccion_vertical=1):

    if n >= len(M[0]):
        return
        
    num_filas = len(M)
    
    A1.append(M[m][n])
    A2.append([m, n])
    
    siguiente_fila = m + direccion_vertical
    siguiente_columna = n
    
    if 0 <= siguiente_fila < num_filas:
        recorrido_especial(A1, A2, M, siguiente_fila, n, direccion_vertical)
    
    else:
        nueva_direccion = -direccion_vertical
        
        siguiente_columna = n + 1
        
        if direccion_vertical == 1:
            fila_inicio = num_filas - 1
        else:
            fila_inicio = 0
            
        if siguiente_columna < len(M[0]):
             recorrido_especial(A1, A2, M, fila_inicio, siguiente_columna, nueva_direccion)
    
    return A1, A2


M = [
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]

A1, A2 = [], []

A1, A2 = recorrido_especial(A1, A2, M)

print(A1, A2)