# Usamos una imagen base Python 3 en Alpine
FROM python:3-alpine

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el contenido de nuestro proyecto local al directorio de trabajo en el contenedor
COPY . /app

# Instalamos las dependencias de nuestro proyecto desde el archivo requirements.txt
RUN pip install -r requirements.txt

# Actualizamos la lista de paquetes disponibles en Alpine Linux
RUN apk update

# Instalamos la herramienta Git en el contenedor
RUN apk add git

# Clonamos el repositorio de Git con el código fuente de nuestro proyecto
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-AManatrizio.git

# Ejecutamos las pruebas unitarias y generamos un informe de cobertura
RUN coverage run -m unittest && coverage report -m

# Iniciamos nuestra aplicación principal (reemplazar "main.py" con el nombre de tu archivo de inicio)
CMD ["python3", "main.py"]
