import numpy as np
from kaleidoscope import qsphere
import matplotlib.pyplot as plt

# Определяем квантовое состояние пятикубитной системы с пятью компонентами
state = np.zeros(2**5, dtype=complex)

# Амплитуды вероятностей для компонент 0, 7, 15, 27 и 30
state[0] = 1/(4*np.sqrt(2))     # амплитуда для состояния |00000⟩ (десятичное 0)
state[7] = 1/(2*np.sqrt(2))     # амплитуда для состояния |00111⟩ (десятичное 7)
state[15] = 3/(4*np.sqrt(2))    # амплитуда для состояния |01111⟩ (десятичное 15)
state[27] = np.sqrt(2)          # амплитуда для состояния |11011⟩ (десятичное 27)
state[30] = 1/4                # амплитуда для состояния |11110⟩ (десятичное 30)

# Визуализация на Q-сфере с нотацией Дирака в десятичной системе счисления
qsphere(state, state_labels_kind='ints').show()