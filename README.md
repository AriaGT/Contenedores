> ¡Se espera que ya se tenga instalado Docker y esté activo!

# Comandos básicos para iniciar con los Contenedores

![Docker Image](https://th.bing.com/th/id/R.a2f46e02ea8f7f8af6c6989687bd6b52?rik=WiqhmOrrNVgkCA&pid=ImgRaw&r=0)

___

## 1. Abrir o cerrar entrono de venv:
    cd venv/Scripts && activate.bat && cd ../..

    cd venv/Scripts && deactivate.bat && cd ../..

## 2. Crear nuestra imagen:
    docker build -t {image_name} .
> Ejemplo: `docker build -t flaskapp .`

## 3. Ver nuestras imágenes:
    docker images

## 4. Ver contenedores:
    docker container ls

## 5. Correr nuestra imagen en la consola:
    docker run -it -p {local_port}:{container_port} {image_name}
> Ejemplo: `docker run -it -p 7000:9000 flaskapp`

## 6. Correr nuestra imagen como un proceso:
    docker run -it -p {local_port}:{container_port} -d {image_name}
> Ejemplo: `docker run -it -p 7000:9000 -d {image_name}`

___

## Ruta para verificar el estado de la App

En ambos casos al correr en proyecto podremos acceder a él desde la ruta:

    localhost:{local_port}/api/v1/

El puerto que usarémos será el establecido en local, como en el ejemplo que sería **7000**

    localhost:7000/api/v1/