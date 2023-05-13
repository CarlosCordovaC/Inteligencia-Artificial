# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:43:02 2023

@author: carlo

k-NN (k-Nearest Neighbors): Es un algoritmo de aprendizaje supervisado que se utiliza 
para la clasificación y regresión. Se basa en encontrar los k puntos de datos más 
cercanos en función de la distancia y asignar una etiqueta o valor en función de las 
etiquetas de los vecinos más cercanos.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generar datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.randn(20, 2) + [2, 2],
                    np.random.randn(20, 2) + [-2, -2],
                    np.random.randn(20, 2) + [2, -2]])

# Aplicar k-Medias
k = 3  # Número de clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Obtener las etiquetas de los clusters y los centroides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')
plt.title('k-Medias Clustering')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()


"""
En este ejemplo, generamos un conjunto de datos de ejemplo con tres grupos distintos. 
Luego, aplicamos el algoritmo k-Medias para agrupar los datos en k=3 clusters. Finalmente, 
visualizamos los datos y los centroides de cada cluster utilizando un gráfico de dispersión.

El resultado será un gráfico que muestra los puntos de datos coloreados según su asignación
 a un cluster y los centroides marcados con una 'x' roja.
"""