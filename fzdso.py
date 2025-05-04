def amplitude(lst):
    if not lst:
        print("A lista está vazia.")
        return
    maior = max(lst)
    menor = min(lst)
    resultado = maior - menor
    print(f"A amplitude é: {resultado}")

numeros = [10, 5, 8, 3, 15, 7]
amplitude(numeros)