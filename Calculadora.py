class Calculadora:

    def soma(self, valores):
        if not valores:
            return 0
        soma = 0
        for valor in valores:
            soma += valor
        return soma

    def subtracao(self, valores):
        if not valores:
            return 0

        subtracao = valores[0]
        for valor in valores[1:]:
            subtracao -= valor
        return subtracao

    def multiplicacao(self, valores):
        if not valores:
            return 0
        multiplicacao = 1
        for valor in valores:
            multiplicacao *= valor
        return multiplicacao

    def divisao(self, numerador, denominador):
        return numerador / denominador

    def fatorial(self, valor):
        if valor < 0:
            raise ValueError("Não existe fatorial de número negativo")
        if valor == 0 or valor == 1:
            return 1
        fatorial = 1
        for i in range(1, valor + 1):
            fatorial *= i
        return fatorial

    def raiz_quadrada(self, valor):
        if valor < 0:
            raise ValueError("Não existe raiz de número negativo")
        if valor == 0:
            return 0
        raiz = 0
        while raiz * raiz <= valor:
            raiz += 1
        return raiz - 1
