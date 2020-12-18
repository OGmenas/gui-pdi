### Instalación 

Para poder entrenar y usar esta red deberemos instalar varios paquetes de Python, todos incluidos en requeriments.txt

Dentro del directorio deberemos ejecutar.

```
pip install -r requirements.txt
```
### Prueba con imágenes

* Introduce las imágenes que desees en el directorio ./prueba/input_imgs/1
* En el script podrás seleccionar distintos pesos generados. Cada número corresponde a la epoch en la que se generaron.
* Ejecuta el script process_img.py con python

```
python3 process_img.py
```

* Las imágenes generadas se guardarán en ./samples/

### Entrenamiento

Para realizar el entrenamiento recomiendo tener CUDA instalado.

Puedes obtener resultados con pocas etapas de entrenamiento, los primeros resultados son muy
exagerados. Conforme avanzan las etapas los resultados se suavizan más. (En este repositorio no se adjunta dataset)

```
python3 train.py
```
