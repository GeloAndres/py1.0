import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahren = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss ='mean_squared_error'
)
print("comenzando entrenamiento......")
historia = modelo.fit(celsius, fahren, epochs=1000000, verbose=False)
print("Modelo Entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historia.history["loss"])

