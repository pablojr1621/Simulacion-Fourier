Simulación y análisis de señales con la Transfromada de Fourier

Descripción

Este proyecto tiene como obejtivo simular y analizar señales elementales en el dominio del tiempo y de la frecuencia mediante la transformada Rápida de Fourier (FFT), utilizando Python y las bibliotecas Numpy y Matplotlib.

Se estudian tres señales: un pulso rectangular, una función escalón unitario y una señal senoidal de 5 Hz. Se generan gráficas temporales y se calculan los espectros de magnitud y fase de cada señal.

Además, se verifican propiedades de la Transformada de Fourier, como la linealidad, el desplazammiento temporal y el escalamiento temporal.

Objetivos

Representar señales elementales en el dominio del timepo.
Calcular la FFT de las señales generadas.
Visualizar ye interpretar los espectros de magnitud y fase.
Comprobar propiedades elementales de la transformada de Fourier.
Comparar el compartamiento de las señales en los dominios del tiempo y la frecuencia.

Herramientas utilizadas

Python
NumPy
Matplotlib

Instalación

Instalar las bibliotecas necesarias mediante el siguiente comando:

python -m pip install numpy matplotlib

Ejecución

1. Abrir una terminal en la carpeta del proyecto.
2. ejecutar el programa con el comando:

python simulacio_fourier.py

3. Observar las gráficas generadas y revisar los resultados numéricos en la consola.
Los mensajes de las pruebas pueden aparecer después de cerrar las ventanas de las gráficas.

Rsultados

El programa genera cinco ventanas de gráficas:

1. Representación temporal del puslo rectangular, el esaclaón unitario y la señla senoidal.
2. Espectros de magnitud y fase del pulso rectangular.
3. Espectros de magnitud y fase del escalón unitario.
4. espectros de magnitud y fase de las señal senoidal.
5. comparación del espectro del pulso original y del pulso comprimido.

Las preubas numéricas permiten comprobar la linealidad y la conservación de la magnitudante un desplazamiento circular. La última gráfica ilustra que la compresión temporal de un pulso produce un espectro más extendido en la frecuencia.

Autor
Eddipablo Gacía

Licencia
Proyecto académico desarrollado con fines educativos.