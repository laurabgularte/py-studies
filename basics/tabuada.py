# tabuada.py

def multiplication_table(number):
    print(f"Tabuada do numero {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    user_input = int(input("Digite o numero para ver a tabuada: "))
    multiplication_table(user_input)