# import keras
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
#
# #Входные данные
# rng = np.random.default_rng()
# n = 5
# X = 1 - 2*rng.random([n, 10000])
# Y = np.sum(np.sin(X), axis=0)
#
# #Нейронная сеть
# model = keras.Sequential()
# model.add(keras.layers.Input(shape=(n,)))
#
# model.add(keras.layers.Dense(38, activation='tanh'))
# model.add(keras.layers.Dense(1, activation='linear'))
# model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.015), loss='mse')
#
# #Обучение
# fit_history = model.fit(
#     np.transpose(X),
#     np.transpose(Y),
#     epochs=100,
#     batch_size=1,
#     verbose=2
# )
#
# print('Минимальное MSE:', np.min(fit_history.history['loss']))
# plt.plot(fit_history.history['loss'])
# plt.show()
#
# model.summary
#
# import cv2
# import math
#
# def rotate_image(image, angle):
#     (h, w) = image.shape[:2]
#     center = (w / 2, h / 2)
#
#     R = cv2.getRotationMatrix2D(center, angle, 1.0)
#
#     cos = abs(M[0][0])
#     sin = abs(M[0][1])
#
#     new_w = int((h * sin) + (w * cos))
#     new_h = int((h * cos) + (w * sin))
#
#     R[0][2] += (new_w / 2) - center[0]
#     R[1][2] += (new_h / 2) - center[1]
#
#     return cv2.warpAffine(image, R, (new_w, new_h))
#
# ug = int(input('Введите градус угла:'))
# img = cv2.imread("fly64.png")
# rotated = rotate_image(img, ug)
#
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import matplotlib.pyplot as plt

P0 = (0, 0)
P1 = (1, 3)
P2 = (3, 3)
P3 = (4, 0)

def bezie(t, P0, P1, P2, P3):
    x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
    y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]

    return x, y

l_x = []
l_y = []
steps = 100

for i in range(steps + 1):
    t = i / steps
    x, y = bezie(t, P0, P1, P2, P3)
    l_x.append(x)
    l_y.append(y)

plt.plot(l_x, l_y, label="Bezie line")
plt.scatter(*zip(P0, P1, P2, P3), color='red', label="Control points")

plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], linestyle='dashed', color='gray')

plt.legend()
plt.grid()
plt.show()