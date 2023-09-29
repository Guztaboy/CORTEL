import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib as mpl





valores1 = [
'Desligamentos Totais',
'Pedidos de Demissão', 
'Homologações Realizadas', 
'Homologações não Realizadas', 
'Feedbacks Positivos',
'Feedbacks Negativos'
]
#Motivos

img = mpimg.imread("logo-grupo-cortel.png")
x_min, y_min = 22.5, 15 
x_max, y_max = 35.5, 20

valores3 = (23, 3, 7, 16, 4, 3)

cores = ['#252B48', 'green', 'red', 'purple', 'yellow', 'orange']

legendas = ['Total', 'Pedidos de Demissão', 'Homologações Realizadas', 'Homologações não Realizadas', 'Feedbacks Positivos', 'Negativos']

x = np.array (valores1)
y1 = np.array(valores3)

for i, label in enumerate(legendas):
    plt.bar(x, y1, width=0.7, align='edge', label = label, color= cores, edgecolor='black')
    for i, valor in enumerate(valores3):
      plt.annotate((valor), xy=(i, valor), xytext=(i+0.1, valor+0.1))
'''
plt.plot (x, y2, marker='o', label = "Faltas")
for i, valor in enumerate(valores2):
      plt.annotate((valor), xy=(i, valor), xytext=(i+0.1, valor+0.1))
'''

plt.imshow(img, extent=[x_min, x_max, y_min, y_max])
plt.xlabel("Motivos") 
plt.ylabel("Quantidade") 
plt.title("Quadro de Desligamentos Cortel SP 09/2023") 
plt.ylim(0, 25, 1,) 
plt.xlim(0, 60, 35) 
plt.xticks(rotation=90)
plt.yticks(range(0, 30, 10))
plt.grid(False)
plt.legend(legendas, labelcolor = cores)
plt.show()

