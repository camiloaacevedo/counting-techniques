from entregable3 import conteo # Para validar el tamaño de las listas
import os, time # Para limpiar la consola y calcular los tiempos de ejecución

def perm(A, actual=[]):
    permutaciones = []
    
    if not A:
        return [actual]

    for i in range(len(A)):
        elemento = A[i]
        elementos_restantes = A[:i] + A[i+1:]
        nueva = actual + [elemento]
        results = perm(elementos_restantes, nueva)
        permutaciones.extend(results)
            
    return permutaciones


def nPr(A, r, actual=[]):
    resultados = []
    
    if len(actual) == r:
        return [actual]

    if not A:
        return []

    for i in range(len(A)):
        elemento = A[i]
        restantes = A[:i] + A[i+1:]
        nueva = actual + [elemento]
        resultados.extend(nPr(restantes, r, nueva))
            
    return resultados

def nCr(A, r, actual=[], index=0):
    if len(actual) == r:
        return [actual]

    combinaciones = []
    
    for i in range(index, len(A)):
        nueva = actual + [A[i]]
        results = nCr(A,r,nueva,i + 1)
        combinaciones.extend(results)
            
    return combinaciones

def nPr_rep(A, r, actual=[]):
    if len(actual) == r:
        return [actual]

    results = []
    
    for elemento in A:
        nuevo = actual + [elemento]
        resultados_recursivos = nPr_rep(A,r,nuevo) 
        results.extend(resultados_recursivos)
            
    return results

def nCr_rep(A, r, actual=[], index=0):
    todas_las_combinaciones = []
    
    if len(actual) == r:
        return [actual]

    for i in range(index, len(A)):
        elemento = A[i]
        nueva = actual + [elemento]
        resultados_recursivos = nCr_rep(A,r,nueva,i)
        todas_las_combinaciones.extend(resultados_recursivos)
            
    return todas_las_combinaciones

def barras(A, m, actual=[], index=0):
    todas = []

    if len(actual) == m:
        return [actual]

    for i in range(index, len(A)):
        contenedor_seleccionado = A[i]
        nueva = actual + [contenedor_seleccionado]
        resultados_recursivos = barras(A,m,nueva,i)
        todas.extend(resultados_recursivos)
            
    return todas

# Mostrar ayuda
def show_help():
    print("\nLista de comandos:\n" \
        "--op : realizar una operación\n" \
        "--n : Fijar valor de n para la operación\n"
        "--r : Fijar valor de r para la operación\n"
        "--m : Fijar valor de m para la operación\n"
        "--k : Fijar valor de k para la operación\n"
        "-verificar : Comparar longitud de reultado obtenido con el valor real\n" \
        "-forzar : Forzar al programa a hacer operaciones con valores mayores a los establecidos\n" \
        "-limites : Testear los límites de tiempo de las operaciones\n" \
        "set_limits : Cambiar valores de los límites\n" \
        "exit: Finalizar la ejecución\n" \
        "clear : Limpiar la terminal\n" \
        "\n" \
        "Operaciones:\n" \
        "perm : Factorial (necesita de un n)\n" \
        "nPr : Factorial (necesita de un n y r)\n" \
        "nCr : Factorial (necesita de un n y r)\n" \
        "nPr_rep : Factorial (necesita de un n y r)\n" \
        "nCr_rep : Factorial (necesita de un n y r)\n" \
        "barras : Factorial (necesita de un m y un k)\n" \
        
    )

# Testear límites de tiempo de operaciones
def test_op(function, T):
    n, r = 1, 1
    while True:
        while r <= n:
            A = [i + 1 for i in range(n)]
            start_time = time.perf_counter()
            function(A,r)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            if total_time > T: # Detengo cuando el tiempo de enumerar supera T
                # Retorno mayor tamaño probado por debajo de T
                if r == 1:
                    return n - 1, n - 1, last_time, total_time
                return n, r - 1, last_time, total_time,
            last_time = total_time
            r += 1
        n +=1
        r = 1

def show_results(n, r, last_time, total_time, function):
    if n == r:
        if total_time >= 3:
            print(f'{function}: n<={n},r<={r} ({last_time}s) ; n={n + 1},r=1 ({total_time}s) demsiado lento')
        else:
            print(f'{function}: n<={n},r<={r} ({last_time}s) ; n={n + 1},r=1 ({total_time}s) lento')
    else:
        if total_time >= 3:
            print(f'{function}: n<={n},r<={r} ({last_time}s) ; r={r + 1} ({total_time}s) demasiado lento')
        else:
            print(f'{function}: n<={n},r<={r} ({last_time}s) ; r={r + 1} ({total_time}s) lento')

def main():
    cont = conteo()
    ops = ['perm', 'nPr', 'nCr', 'nPr_rep', 'nCr_rep', 'barras']
    n_lim,r_lim,m_lim,k_lim = 7,6,10,6
    T = 2

    while True:
        try:
            opt = input().strip() 
        except EOFError:
            break
        
        if not opt:
            continue
            
        if opt == 'exit':
            break

        # Probando los límites
        if opt == '-limites':
            # Test de nPr
            n, r, last_time, total_time = test_op(nPr,T)
            show_results(n, r, last_time, total_time, "nPr")

            # Test de nCr (tener en cuenta que este test puede tardar varios segundo en completarse)
            n, r, last_time, total_time = test_op(nCr,T)
            show_results(n, r, last_time, total_time, "nCr")

            # Test de nPr_rep
            n, r, last_time, total_time = test_op(nPr_rep,T)
            show_results(n, r, last_time, total_time, "nPr_rep")

            # Test de nCr_rep
            n, r, last_time, total_time = test_op(nCr_rep,T)
            show_results(n, r, last_time, total_time, "nCr_rep")

            # Test de barras
            n, r, last_time, total_time = test_op(nCr_rep,T)
            show_results(n, r, last_time, total_time, "barras")

        if opt == 'set_limits': # Cambiar los límites predeterminados
            desicion = input('\nHacer operaciones con límites altos puede detener el programa repentinamente. ¿Está seguro que desea continuar? Y/n ')
            if desicion == 'Y' or desicion == 'y':
                print(f'n={n_lim}, r={r_lim}, m={m_lim}, k={k_lim}')
                n_lim = int(input('n='))
                while n_lim < 0:
                    print('n debe ser un entero positivo')
                    n_lim = int(input('n='))
                r_lim = int(input('r='))
                while r_lim < 0:
                    print('r debe ser un entero positivo')
                    r_lim = int(input('r='))
                m_lim = int(input('m='))
                while m_lim < 0:
                    print('m debe ser un entero positivo')
                    m_lim = int(input('m='))
                k_lim = int(input('k='))
                while k_lim < 0:
                    print('k debe ser un entero positivo')
                    k_lim = int(input('k='))



        if opt == 'help': # Mostrar lista de comandos y operaciones
            show_help()


        if opt == 'clear': # Limpiar consola
            os.system('cls') # Para Windows
            os.system('clear') # Para Linux / macOS


        args = opt.split() # Extraer y agrupar las subcadenas del comando


        if 'set_limits' not in args and 'help' not in args and 'clear' not in args and '-limites' not in args:
            if len(args) < 2 or args[0] != '--op':
                print(f"'{opt}' command not found. Enter 'help' for more options")
                continue


            # Verificar la operación selecionada
            op = args[1] 


            if op not in ops:
                print(f"'{op}' command not found. Enter 'help' for more options")
                continue
            
            # Operación factorial
            if op == 'perm':
                if '--n' not in args or len(args) > 6:
                     print(f"'{opt}' command not found. Enter 'help' for more options")
                     continue
                
                try:
                    n_index = args.index('--n') + 1
                    n_val = int(args[n_index])
                    if n_val <= n_lim or '-forzar' in args:
                        A = [i + 1 for i in range(n_val)]
                        A = perm(A)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.factorial(n_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')
                        
                    if n_val > n_lim and '-forzar' not in args:
                        print("n mayor al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print(f"Error: '{args[-1]}' is not valid for '--n'.")


            # Operación permutación sin repetición
            if op == 'nPr':
                if '--n' not in args or '--r' not in args:
                    print("Error: El comando 'nPr' requiere '--n <valor> y --r <valor>'.")
                    continue
                
                try:
                    n_index = args.index('--n') + 1
                    n_val = int(args[n_index])

                    r_index = args.index('--r') + 1
                    r_val = int(args[r_index])

                    if (n_val <= n_lim and r_val <= r_lim) or '-forzar' in args:
                        A = [i + 1 for i in range(n_val)]
                        A = nPr(A, r_val)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.nPr(n_val,r_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')

                    if (n_val > n_lim or r_val > r_lim) and '-forzar' not in args:
                        print("n o r mayor/es al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print("Error: Los valores de '--n' o '--r' no son números válidos.")


            # Operación combinación sin repetición
            if op == 'nCr':
                if '--n' not in args or '--r' not in args:
                    print("Error: El comando 'nCr' requiere '--n <valor> y --r <valor>'.")
                    continue
                
                try:
                    n_index = args.index('--n') + 1
                    n_val = int(args[n_index])

                    r_index = args.index('--r') + 1
                    r_val = int(args[r_index])

                    if (n_val <= n_lim and r_val <= r_lim) or '-forzar' in args:
                        A = [i + 1 for i in range(n_val)]
                        A = nCr(A, r_val)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.nCr(n_val,r_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')

                    if (n_val > n_lim or r_val > r_lim) and '-forzar' not in args:
                        print("n o r mayor/es al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print("Error: Los valores de '--n' o '--r' no son números válidos.")


            # Operación permutación con repetición
            if op == 'nPr_rep':
                if '--n' not in args or '--r' not in args:
                    print("Error: El comando 'nPr_rep' requiere '--n <valor> y --r <valor>'.")
                    continue
                
                try:
                    n_index = args.index('--n') + 1
                    n_val = int(args[n_index])

                    r_index = args.index('--r') + 1
                    r_val = int(args[r_index])

                    if (n_val <= n_lim and r_val <= r_lim) or '-forzar' in args:
                        A = [i + 1 for i in range(n_val)]
                        A = nPr_rep(A, r_val)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.nPr_rep(n_val,r_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')

                    if (n_val > n_lim or r_val > r_lim) and '-forzar' not in args:
                        print("n o r mayor/es al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print("Error: Los valores de '--n' o '--r' no son números válidos.")


            # Operación combinación con repetición
            if op == 'nCr_rep':
                if '--n' not in args or '--r' not in args:
                    print("Error: El comando 'nCr_rep' requiere '--n <valor> y --r <valor>'.")
                    continue
                
                try:
                    n_index = args.index('--n') + 1
                    n_val = int(args[n_index])

                    r_index = args.index('--r') + 1
                    r_val = int(args[r_index])

                    if (n_val <= n_lim and r_val <= r_lim) or '-forzar' in args:
                        A = [i + 1 for i in range(n_val)]
                        A = nCr_rep(A, r_val)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.nCr_rep(n_val,r_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')

                    if (n_val > n_lim or r_val > r_lim) and '-forzar' not in args:
                        print("n o r mayor/es al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print("Error: Values for '--n' or '--r' are not valid.")


            # Operación de barras y estrellas
            if op == 'barras':
                if '--m' not in args or '--k' not in args:
                    print("Error: El comando 'barras' requiere '--m <valor> y --k <valor>'.")
                    continue
                
                try:
                    m_index = args.index('--m') + 1
                    m_val = int(args[m_index])

                    k_index = args.index('--k') + 1
                    k_val = int(args[k_index])

                    if (m_val <= m_lim and k_val <= k_lim) or '-forzar' in args:
                        A = [i + 1 for i in range(k_val)]
                        A = barras(A, m_val)
                        print(A)
                        if '-verificar' in args:
                            if len(A) == cont.barras_estrellas(m_val,k_val): # Validar el tamaño del arreglo vs. la fórmula
                                print('OK')
                                continue
                            print('FAIL')

                    if (m_val > m_lim or k_val > k_lim) and '-forzar' not in args:
                        print("m o k mayor/es al límite asignado. Escriba 'set_limits' para modificar los límites")
                        continue

                except (ValueError, IndexError):
                    print("Error: Los valores de '--m' o '--k' no son números válidos.")


if __name__ == "__main__":
    main()
