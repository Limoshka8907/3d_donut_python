import numpy as np
import os
import time
A = 0.0
B = 0.0
z = np.zeros(1760)
b = [' '] * 1760
symbols = ".,-~:;=!*#$@"

# Очистка экрана
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Сброс массивов
    b = [' '] * 1760
    z.fill(0)

    for j in np.arange(0, 6.28, 0.07):
        for i in np.arange(0, 6.28, 0.02):
            sini = np.sin(i)
            cosj = np.cos(j)
            sinA = np.sin(A)
            sinj = np.sin(j)
            cosA = np.cos(A)
            cosj2 = cosj + 2
            mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
            cosi = np.cos(i)
            cosB = np.cos(B)
            sinB = np.sin(B)
            t = sini * cosj2 * cosA - sinj * sinA
            x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
            y = int(12 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
            o = x + 80 * y
            N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))

            if 22 > y > 0 and 0 < x < 80 and mess > z[o]:
                z[o] = mess
                b[o] = symbols[N] if N > 0 else symbols[0]

    # Очистка предыдущего вывода в терминале
    print("\x1b[d", end='')

    # Вывод результата
    for k in range(1760):
        print(b[k], end='\n' if k % 80 == 79 else '')

    A += 0.04
    B += 0.02

    # Задержка для визуализации кадров
    time.sleep(0.001)