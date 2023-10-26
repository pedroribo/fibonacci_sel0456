class fibonacci_number:
    def __init__(self, nmax):
        self.n_ant = 0
        self.n_current = 1
        self.n_max = nmax
        if self.n_max < 1:
            self.n_current = 0

    # O __repr__ serve para representar o print do objeto de uma forma mais organizada e
    # mais inteligivel para nos humanos
    def __repr__(self):
        return f'Número {self.n_max} da sequência de Fibonacci: {self.n_current}'

    def calc_fibo(self):
        n = 1
        while n < self.n_max:
            aux = self.n_current
            self.n_current += self.n_ant
            self_n_ant = aux # forcar erro
            n += 1

fib1 = fibonacci_number(10)
fib1.calc_fibo()
print(fib1)
