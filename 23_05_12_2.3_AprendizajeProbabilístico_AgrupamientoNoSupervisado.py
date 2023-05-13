# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:34:40 2023

@author: carlo

En resumen, el agrupamiento no supervisado es una técnica que permite descubrir
 automáticamente la estructura subyacente de un conjunto de datos sin la necesidad de 
 conocer las etiquetas de las muestras. Utiliza métodos estadísticos y probabilísticos 
 para agrupar los datos en clústeres basados en su similitud, lo que facilita la 
 identificación de patrones, segmentación de datos y análisis exploratorio. Es una 
 herramienta útil en diversas aplicaciones, como la segmentación de clientes, análisis
 de redes sociales, reconocimiento de patrones, entre otros.
"""

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Crear el modelo de agrupamiento con k-medias
k = 2
modelo = KMeans(n_clusters=k)
modelo.fit(datos)

# Obtener las etiquetas de los grupos y los centroides
etiquetas = modelo.labels_
centroides = modelo.cluster_centers_

# Visualizar los datos y los grupos
colores = ['r', 'b']  # Colores para los puntos de cada grupo
for i in range(len(datos)):
    plt.scatter(datos[i][0], datos[i][1], color=colores[etiquetas[i]], s=100)

# Visualizar los centroides
for centroide in centroides:
    plt.scatter(centroide[0], centroide[1], color='k', marker='x', s=200)

plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Agrupamiento de datos utilizando k-medias')
plt.show()


"""
En este ejemplo, tenemos un conjunto de datos de muestra con dos características. 
Utilizamos la biblioteca scikit-learn para crear un modelo de agrupamiento utilizando 
el algoritmo de k-medias. Luego ajustamos el modelo a los datos y obtenemos las etiquetas 
de los grupos asignados a cada punto de datos y los centroides de cada grupo.

Finalmente, visualizamos los puntos de datos en un gráfico, donde cada grupo se muestra 
con un color diferente y los centroides se marcan con una 'x'. Esto nos permite ver cómo 
se agrupan los datos en función de las características y cómo se distribuyen los centroides.

Este ejemplo ilustra cómo puedes aplicar el algoritmo de k-medias en Python para realizar 
agrupamiento no supervisado y obtener información sobre la estructura subyacente de tus 
datos.
"""