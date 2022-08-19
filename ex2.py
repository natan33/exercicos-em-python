frase = str(input('Digite um frase: ')).upper().strip()

print(f'\033[1mA letra A aparece {frase.count("A")} vezes nessa frase\033[m')
print(f'\033[2;32mA primeira letra A apareceu na posição {frase.find("A")+1}\033[m')
print(f'\033[7;35;31mA ultima letra A apareceu na posição {frase.rfind("A")+1}\033[m')
