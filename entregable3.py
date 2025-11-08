import math, time

class conteo:
    def factorial(self,n):
        '''
        Idea combinatoria:
        Si queremos por ejemplo saber de cuantas formas diferentes
        se pueden distribuir n personas en una cantidad n de asientos, 
        podemos usar el factorial para calcularlo. 
        Ejemplo: _n_x_n-1_x...x_1_ esto es igual a n!.
        '''
        if isinstance(n, float) or n < 0:
            raise ValueError("El factorial solo está definido para enteros no negativos")

        return int(math.factorial(n)) # Aquí optamos por calcular el factorial directamente para cumplir con el requerimiento de usar fórmulas cerradas.

    def nPr(self,n,r):
        '''
        Idea combinatoria:
        Si queremos saber se pueden seleccionar n personas para r distintas posiciones,
        podemos permutar n con r ya que el orden si importa al ser posiciones diferentes.
        Ejemplo:
        ¿De cuantas maneras se pueden seleccionar 5 personas para tres cargos: Rector, Vicerector
        y personero?
        Respuesta: Ya que los cargos son diferentes, el orden importa. No es lo mismo ser rector
        que personero por ejemplo. Por tanto, la cantidad de formas de escoger los 3 cargos sería P(5,3)
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("La permutación como concepto de combinatoria solo esta definido para enteros no negativos")

        if r > n:
            raise ValueError(f'No se puede permutar {r} elementos en {n} espacios')

        if r == 0:
            return 1

        return int(self.factorial(n)//self.factorial(n - r))

    def nCr(self,n,r):
        '''
        Idea combinatoria:
        Se tomaron n muestra de un proceso de fabricación bajo las mismas condiciones
        y seran analizadas bajo las mismas condiciones también pero por cuestiones de 
        tiempo solo se van a analizar r, ¿De cuántas formas puedo tomar las r muestras?
        Solución:
        Ya que las muestras seran analizadas bajo las mismas condiciones, no nos importa
        el orden. Por tanto la cantidad de formas de seleccionarlas es C(n,r).
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("La combinación como concepto, solo esta definido para enteros no negativos")

        if r > n:
            raise ValueError(f'No se puede combinar {r} elementos en {n} espacios')

        if r == 0:
            return 1

        return int(self.nPr(n,r)/self.factorial(r))

    def nPr_rep(sef,n,r):
        '''
        Idea combinatoria:
        Si queremos saber cuantas cadenas de longitud n y r bits se pueden formar,
        podemos averiguarlo con n^r.
        Ejemplo: Halle la cantidad de cadenas de 2 bits que se pueden formar con
        longitud 4.
        Solución: 2^4 = 16.
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("La permutación con repetición como concepto de combinatoria solo esta definido para enteros no negativos")

        if r > n:
            raise ValueError(f'No se puede permutar {r} elementos en {n} espacios')

        return n**r

    def nCr_rep(self,n,r):
        '''
        Idea combinatoria:
        Suponga tener 10 bolas, 3 amarillas, 5 azules y dos rojas. Si desea tomar 4
        bolas de manera aleatoria no es importante el orden en que se escogen ya que
        tomar amarillo, amarrillo, azul y rojo es lo mismo que tomar amarillo, azul,
        amarilo y rojo. Sin embargo, al haber elementos repetidos, debe realizar una
        combinación con repetición. Puede verlo como que cada vez que sace una bola,
        anotará su color y la devolvera fuera. Esto se conoce como combinación con
        repetición, donde n es la cantidad de bolas y r es la cantidad de bolas que
        se van a tomar y se calcula como C(n + r - 1, r).
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("La combinación con repetición como concepto, solo esta definido para enteros no negativos")

        if r + n == 0:
            raise ValueError("No se puede combinar con repetición 0 elementos en 0 espacios")

        return self.nCr(n + r - 1, r)

    def barras_estrellas(self,m,k):
        '''
        Idea combinatoria:
        Queremos saber de cuantas formas puedo distribuir m lentejas en
        k contenedores, para eso voy a separar las lentejas en k grupos
        y k - 1 separadores. Al final, la cantidad total en que puedo
        distribuir esas lentejas en los k grupos es C(m + k - 1, k - 1).
        '''
        if isinstance(m, float) or isinstance(k, float) or m < 0 or k < 0:
            raise ValueError("La técnica de barras y estrellas como concepto de combinatoria, solo esta definido para enteros no negativos")

        return self.nCr(m + k - 1, k - 1)

# Exploración de límites

T = 4e-05
'''
Se escoge un T muy pequeño ya que los tiempos de procesamiento de cada 
prueba son extremadamente bajos por lo que r y n crecen muy rapidamente 
truncando así, la longitud con la que Python puede guardar un float.

Esto quiere decir que el tamaño de T es inversamente proporcional a la
potencia del procesador con el que se disponga. Entre más potente el procesador,
más rapido realiza los cálculos por lo tanto se le hace más dificil alcanzar T y
por tanto, los cálculos crecen cada vez más haciendo que se trunque la longitud con
la que Python puede guardar un float que es aproximadamente máximo 1.7976931348623157e+308
y mínimo 2.2250738585072014e-308 (esto se puede comprobar ejecutando print(sys.float_info
con la librería sys).

El T máximo que pude tomar sin que haya truncamiento con las especificaciones de mi computador 
es T = 4e-05 y las especificaciones de mi computador son las siguientes:
- CPU: Intel Core i5 12450H, 3.30 GHz (boost up to 4.40 GHz), 8 cores, 12 threads and 45w.
- GPU: Intel® UHD Graphics for 12th Gen Intel® Processors  1.20 GHz 
- RAM: 8GB DDR5
- ROM: M.2 DE 512 GB

Sientase libre de ajustar T en función de las características de su computador.
'''

def test_function(function):
    n, r = 1, 1
    while True:
        while r <= n:
            start_time = time.perf_counter()
            function(n,r)
            end_time = time.perf_counter()
            total_time = end_time - start_time

            if total_time > T: # Detengo cuando el tiempo de enumerar supera T
                # Retorno mayor tamaño probado por debajo de T
                if r == 1:
                    return n - 1, n - 1
                return n, r - 1 
            
            r += 1
        n += 1
        r = 1

def main():
    cont = conteo()
    print("Ejercicios ítem (C):")
    print(f'6! = {cont.factorial(6)}')
    print(f'P(7,3) = {cont.nPr(7,3)}')
    print(f'C(10,4) = {cont.nCr(10,4)}')
    print(f'5^4 = {cont.nPr_rep(5,4)}')
    print(f'C(3 + 5 - 1, 5) = {cont.nCr_rep(3,5)}')
    print(f'barras_y_estrellas(8 + 3 - 1, 8) = {cont.barras_estrellas(8,3)}')

    print("\nExploración de límites:")
    n, r = test_function(cont.nPr)
    print(f'P(n,r) enum OK hasta n={n},r={r}; {T}s')
    n, r = test_function(cont.nPr_rep)
    print(f'n^r enum OK hasta n={n},r={r}; {T}s')
    n, r = test_function(cont.nCr)
    print(f'C(n,r) enum OK hasta n={n},r={r}; {T}s')
    n, r = test_function(cont.nCr_rep)
    print(f'C(n + r - 1, r) enum OK hasta n={n},r={r}; {T}s')
    m, k = test_function(cont.barras_estrellas)
    print(f'barras y estrellas enum OK hasta n={m},r={k}; {T}s')
    
if __name__ == "__main__":
    main()