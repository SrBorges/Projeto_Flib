from random import randint

def gerar():

    gerador = randint(1, 1000)
    return gerador


aleatorio = gerar()

# print(aleatorio) <- Ver valor. 

valor = int(input("Digite seu Chute: "))
digito = 1

while valor != aleatorio:
    digito += 1
    valor = int(input("Digite seu Chute: "))
    print(f"Tentativa: {digito}")

    if 0 < valor <= 150:
        print("Muito baixo.")
    elif 151 < valor <= 400:
        print("Muito baixo. ")
    elif 401 < valor <= 600:
        print("Muito alto. ")
    elif 401 < valor <= 500:
        print("Muito alto. ")
    elif 600 < valor <= 1000:
        print("Muito alto. ")
print("Você acertou. :) \n")


if 0 < digito <= 5:
    print("Excelente. ")
elif 6 <= digito <= 7:
    print("Bom. ")
elif 8 <= digito <= 12:
    print("Normal. ")
elif 13 <= digito <= 14:
    print("Ruim. ")
elif digito >= 15:
    print("Trágico. ")

### Sr. Borges ###
