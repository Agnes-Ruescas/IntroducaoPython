conjunto = {1, 2, 3, 4, 5}
conjuto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjuto2)
print('União {} '.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjuto2)
print('Intercecção {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjuto2)
conjunto_diferenca2 = conjuto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjuto_diff_simetrica = conjunto.symmetric_difference(conjuto2)
print('Diferença simétrica {}'.format(conjuto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato',  'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# print(conjunto)