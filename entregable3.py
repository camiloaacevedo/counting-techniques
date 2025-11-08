import math, time

class conteo:
    def factorial(self,n):
        """
        Combinatorial idea:
        If we want to know, for example, how many different ways
        n people can be distributed among n seats,
        we can use the factorial to calculate it.
        Example: _n_x_n-1_x...x_1_ this is equal to n!.
        """
        if isinstance(n, float) or n < 0:
            raise ValueError("The factorial is only defined for non-negative integers")

        return int(math.factorial(n)) # Here we opted to calculate the factorial directly to comply with the requirement of using closed formulas.

    def nPr(self,n,r):
        '''
        Combinatorial Idea:
        If we want to know how many n people can be selected for r different positions,
        we can permute n with r since order matters because the positions are different.
        Example:
        In how many ways can 5 people be selected for three positions: Rector, Vice-Rector,
        and Student Representative?
        Answer: Since the positions are different, order matters. Being Rector is not the same as being Student Representative, for example.
        Therefore, the number of ways to choose the 3 positions would be P(5,3)
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("Permutation as a combinatorial concept is only defined for non-negative integers.")

        if r > n:
            raise ValueError(f'You cannot permute {r} elements in {n} spaces')

        if r == 0:
            return 1

        return int(self.factorial(n)//self.factorial(n - r))

    def nCr(self,n,r):
        '''
        Combinatorial Idea:
        n samples were taken from a manufacturing process under the same conditions
        and will be analyzed under the same conditions as well, but due to time constraints,
        only r will be analyzed. In how many ways can I take the r samples?
        Solution:
        Since the samples will be analyzed under the same conditions, the order doesn't matter.
        Therefore, the number of ways to select them is C(n,r)."
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("The concept of combination is only defined for non-negative integers.")

        if r > n:
            raise ValueError(f'You cannot combine {r} elements in {n} spaces')

        if r == 0:
            return 1

        return int(self.nPr(n,r)/self.factorial(r))

    def nPr_rep(sef,n,r):
        '''
        Combinatorial idea:
        If we want to know how many strings of length n and r bits can be formed,
        we can find out using n^r.
        Example: Find the number of 2-bit strings that can be formed with
        length 4.
        Solution: 2^4 = 16.
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("Permutation with repetition as a combinatorial concept is only defined for non-negative integers.")

        if r > n:
            raise ValueError(f'You cannot permute {r} elements in {n} spaces')

        return n**r

    def nCr_rep(self,n,r):
        '''
        Combinatorial Idea:
        Suppose you have 10 balls: 3 yellow, 5 blue, and 2 red. If you want to randomly select 4 balls, 
        the order in which you choose them doesn't matter, since selecting yellow, yellow, blue, and red is 
        the same as selecting yellow, blue, yellow, and red. However, because there are repeated elements, 
        you must perform a combination with repetition. You can think of it as noting the color of each ball 
        you draw and then returning it to the bin. This is known as a combination with repetition, where n is 
        the number of balls and r is the number of balls to be selected, calculated as C(n + r - 1, r).
        '''
        if isinstance(n, float) or isinstance(r, float) or n < 0 or r < 0:
            raise ValueError("The concept of combination with repetition is only defined for non-negative integers.")

        if r + n == 0:
            raise ValueError("You cannot combine with repetition 0 elements in 0 spaces")

        return self.nCr(n + r - 1, r)

    def barras_estrellas(self,m,k):
        '''
        Combinatorial idea:
        We want to know how many ways I can distribute m lentils into
        k containers. To do this, I will separate the lentils into k groups
        and use k - 1 dividers. In the end, the total number of ways I can
        distribute these lentils into the k groups is C(m + k - 1, k - 1)."
        '''
        if isinstance(m, float) or isinstance(k, float) or m < 0 or k < 0:
            raise ValueError("The star and bar technique, as a combinatorial concept, is only defined for non-negative integers.")

        return self.nCr(m + k - 1, k - 1)

# Exploración de límites

T = 4e-05
''' 
A very small T is chosen because the processing times for each test are extremely low, so r and n grow very rapidly, thus truncating the length that Python can store a float.

This means that the size of T is inversely proportional to the processing power available. The more powerful the processor,
the faster it performs calculations, therefore it becomes more difficult to reach T, and
consequently, the calculations grow larger and larger, causing the length with which Python can store a float to be truncated. This length is approximately a maximum of 1.7976931348623157e+308
and a minimum of 2.2250738585072014e-308 (this can be verified by executing `print(sys.float_info)` with the `sys` library).

The maximum T I could reach without truncation with my computer's specifications
is T = 4e-05, and my computer's specifications are as follows:
- CPU: Intel Core i5 12450H, 3.30 GHz (boost up to 4.40 GHz), 8 cores, 12 threads and 45w.
- GPU: Intel® UHD Graphics for 12th Gen Intel® Processor 1.20 GHz
- RAM: 8GB DDR5
- ROM: 512GB M.2 SSD

Feel free to adjust T according to your computer's specifications.
'''

def test_function(function):
    n, r = 1, 1
    while True:
        while r <= n:
            start_time = time.perf_counter()
            function(n,r)
            end_time = time.perf_counter()
            total_time = end_time - start_time

            if total_time > T: # I stop when the enumeration time exceeds T
                # Return larger size tested below T
                if r == 1:
                    return n - 1, n - 1
                return n, r - 1 
            
            r += 1
        n += 1
        r = 1

def main():
    cont = conteo()
    print("Exercise ítem (C):")
    print(f'6! = {cont.factorial(6)}')
    print(f'P(7,3) = {cont.nPr(7,3)}')
    print(f'C(10,4) = {cont.nCr(10,4)}')
    print(f'5^4 = {cont.nPr_rep(5,4)}')
    print(f'C(3 + 5 - 1, 5) = {cont.nCr_rep(3,5)}')
    print(f'barras_y_estrellas(8 + 3 - 1, 8) = {cont.barras_estrellas(8,3)}')

    print("\nLimits exploration:")
    n, r = test_function(cont.nPr)
    print(f'P(n,r) enum OK up to n={n},r={r}; {T}s')
    n, r = test_function(cont.nPr_rep)
    print(f'n^r enum OK up to n={n},r={r}; {T}s')
    n, r = test_function(cont.nCr)
    print(f'C(n,r) enum OK up to n={n},r={r}; {T}s')
    n, r = test_function(cont.nCr_rep)
    print(f'C(n + r - 1, r) enum OK up to n={n},r={r}; {T}s')
    m, k = test_function(cont.barras_estrellas)
    print(f'stars and stripes enum OK up to n={m},r={k}; {T}s')
    
if __name__ == "__main__":
    main()
