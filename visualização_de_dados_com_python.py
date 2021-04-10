# -*- coding: utf-8 -*-
"""Visualização de dados com python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NqRAgLIabOEruSuE1hYOrpqK9WQdK42T
"""

import matplotlib.pyplot as plt

x1 = [0, 1, 3, 5, 7, 9]
y1 = [0, 2, 8, 2, 4, 13]

x2 = [0, 2, 4, 6, 8, 10]
y2 = [0, 4, 4, 4, 7, 5]

titulo = "Gráfico de linhas by Glédison"
eixox= "Eixo X"
eixoy= "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.plot(x1, y1, label = "Grupo 1")
plt.plot(x2, y2, label = "Grupo 2")
plt.legend()

plt.show()

x1 = [1, 3, 5, 7, 9]
y1 = [2, 8, 2, 4, 13]

x2 = [2, 4, 6, 8, 10]
y2 = [4, 4, 4, 7, 5]

titulo = "Gráfico de barras by  Glédison"
eixox= "Eixo X"
eixoy= "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()

plt.show()

x1 = [0, 1, 3, 5, 7, 9]
y1 = [0, 2, 8, 2, 4, 13]

x2 = [0, 2, 4, 6, 8, 10]
y2 = [0, 4, 4, 4, 7, 5]

titulo = "Scartterplot: Gráfico de dispersão by  Glédison"
eixox= "Eixo X"
eixoy= "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x1, y1, label = "Grupo 1")
plt.scatter(x2, y2, label = "Grupo 2")

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.legend()

plt.show()

#Mudança de cores

x1 = [0, 1, 3, 5, 7, 9]
y1 = [0, 2, 8, 2, 4, 13]

x2 = [0, 2, 4, 6, 8, 10]
y2 = [0, 4, 4, 4, 7, 5]

titulo = "Scartterplot: Gráfico de dispersão by  Glédison"
eixox= "Eixo X"
eixoy= "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x1, y1, label = "Grupo 1", color="k", marker=".", s=100)
plt.scatter(x2, y2, label = "Grupo 2")

plt.plot(x1, y1, color="K", linestyle="--")
plt.plot(x2, y2)

plt.legend()
#Salvando a imagem em um arquivo
plt.savefig("figura1.pdf")

