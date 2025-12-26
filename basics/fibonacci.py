import math

def fibonacci(n):
 
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    fib_n = round((phi**n - psi**n) / math.sqrt(5))
    return fib_n

if __name__ == "__main__":
    n = int(input("Digite a posicao (n): "))
    result = fibonacci(n)
    print(f"O {n} numero da sequencia de fibonacci eh:  {result}")