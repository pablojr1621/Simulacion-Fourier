# ===========================================================
# PROYECTO: SIMULACION Y ANALISIS DE SEÑALES CON FOURIER
# AUTOR: Eddipablo García
# Descripción: generación y representación de señales básicas
# ===========================================================

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# 1. CONFIGURACIÓN DE LOS PARÁMETROS
# -----------------------------------------------------------

frecuencia_muestreo = 1000  # Muestras por segundo (Hz)
duracion = 1.0              # Duración de la señal (segundos)

# Vector de tiempo
t = np.arange(
    -duracion / 2,
    duracion / 2,
    1 / frecuencia_muestreo
)

# -----------------------------------------------------------
# 2. GENERACIÓN DELAS SEÑALES 
# -----------------------------------------------------------

# A. Pulso rectangular: vale 1 entre -0.1 y 0.1 segundos
pulso = np.where(np.abs(t) <= 0.1, 1.0, 0.0)

# B. Función escalón unitario: vale 0 antes t=0 y 1 después
escalon = np.where(t >= 0, 1.0, 0.0)

# C. Señal senoidal de 5 Hz y amplitud 1
frecuencia = 5
senoidal = np.sin(2 * np.pi * frecuencia * t)

# -------------------------------------------------------------
# 3. REPRESENTACIÓN EN EL DOMINIO DEL TIEMPO
# -------------------------------------------------------------

fig, ejes = plt.subplots(3, 1, figsize=(10, 9))

ejes[0].plot(t, pulso, color="blue")
ejes[0].set_title("Pulso rectangular")
ejes[0].set_ylabel("Amplitud")
ejes[0].grid(True)

ejes[1].plot(t, escalon, color="green")
ejes[1].set_title("Función escalón unitario")
ejes[1].set_ylabel("Amplitud")
ejes[1].grid(True)

ejes[2].plot(t, senoidal, color="red")
ejes[2].set_title("Señal senoidal de 5 Hz")
ejes[2].set_xlabel("Tiempo (segundos)")
ejes[2].set_ylabel("Amplitud")
ejes[2].grid(True)

plt.tight_layout()
plt.show()


# --------------------------------------------------------------
# 4. TRANSFORMADA DE FOURIER Y ESPECTROS
# --------------------------------------------------------------

# Diccionario con las señales que analizaremos
senales = {
    "Pulso rectangular": pulso,
    "Funcion escalon": escalon,
    "Senal senoidal": senoidal
}

# Vector de frecuencias correspondientes a la FFT
N = len(t)
frecuencias = np.fft.fftfreq(
    N, d=1 / frecuencia_muestreo
)

# Analizar cada señal
for nombre, x in senales.items():

    # Calcular la transformada discreta de Fourier
    X = np.fft.fft(x)

    # Central el esprectro al rededor de 0 Hz
    frecuencias_centradas = np.fft.fftshift(frecuencias)
    X_centrada = np.fft.fftshift(X)

    # Magnitud normalizada y fase
    magnitud = np.abs(X_centrada) / N
    fase = np.angle(X_centrada)

    # Eviar mostrar fase donde la magnitud es práctimanete cero
    fase[magnitud < 1e-10] = np.nan

    # Crear las gráficas del espectro
    fig, ejes = plt.subplots(2, 1, figsize=(10, 7))

    # Gráfica de magnitud
    ejes[0].plot(frecuencias_centradas, magnitud)
    ejes[0].set_title(
        f"Espectro de magnitud: {nombre}"
    )
    ejes[0].set_xlabel("Frecuencia (HZ)")
    ejes[0].set_ylabel("Magnitud")
    ejes[0].grid(True)
    ejes[0].set_xlim(-50, 50)

    # Gráfica de fase
    ejes[1].plot(frecuencias_centradas, fase)
    ejes[1].set_title(
        f"Espectro de fase: {nombre}"
    )

    ejes[1].set_xlabel("Frecuecnia (Hz)")
    ejes[1]. set_ylabel("Fase (radianes)")
    ejes[1].grid(True)
    ejes[1].set_xlim(-50, 50)

    plt.tight_layout()
    plt.show()

# -----------------------------------------------------
# 5. VERIFICACION DE LAS PROPIEDADES DE FOURIER
# -----------------------------------------------------

# Utilizaremos el pulso rectagular como señal de prueva
x = pulso.copy()

# A. PROPIEDAD DE LINEALIDAD
# FFT{a*x + b*y} = a*FFT{x} + b*FFT{y}

y = senoidal.copy()
a = 2
b = 3

transformada_combinada = np.fft.fft(a * x + b * y)

transformadas_separadas = (
    a * np.fft.fft(x) + b * np.fft.fft(y)
)

error_linealidad = np.max(
    np.abs(transformada_combinada - transformadas_separadas)
)

print("\n--- Propiedad de linealidad ---")
print("Error máximo:", error_linealidad)
print(
    "¿Se cumple la propiedad?",
    np.allclose(transformada_combinada, transformadas_separadas)
)

# B. DESPLAZAMIENTO TEMPORAL
# Un desplazamiento circular conserva la magnitud de la FFT

desplazamiento = 50
x_desplazada = np.roll(x, desplazamiento)

x_original = np.fft.fft(x)
x_desplazada = np.fft.fft(x_desplazada)

error_magnitud = np.max(
    np.abs(np.abs(x_original) - np.abs(x_desplazada))
)

print("\n--- Desplazamiento temporal ---")
print("Error máximo entre magnitudes:", error_magnitud)
print(
    "¿Se conserva la maginitud?",
      np.allclose(np.abs(x_original),
                  np.abs(x_desplazada)))

# C. ESCLAMIENTO TEMPORAL
# Al comprimir una señal en el tiempo, su espectro 
# se extiende en frecuencia

pulso_comprimido = np.where(
    np.abs(2 * t) <= 0.1, 1.0, 0.0
)

x_original_centrada = np.fft.fftshift(
    np.fft.fft(x)
)

x_comprimido_centrado = np.fft.fftshift(
    np.fft.fft(pulso_comprimido)
)

plt.figure(figsize=(10, 5))

plt.plot(
    np.fft.fftshift(frecuencias),
    np.abs(x_original_centrada) / N,
    label="Pulso original"
)

plt.plot(
    np.fft.fftshift(frecuencias),
    np.abs(x_comprimido_centrado) / N,
    label="Pulso comprimido"
)

plt.title("Efecto del escalamiento temporal en la frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud normalizada")
plt.xlim(-50, 50)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
