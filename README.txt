Rogelio Alberto Félix Gamboa - A01634386
Juan Carlos Quirino Carrasco - A01632369

---
Masa resorte utilizando factorización LU
---

La aplicación se divide en dos partes, el servidor que resuelve
un sistema de ecuaciones dado utilizando factorizacion LU y 
una pagina web que corre la interfaz, este primero escrito en
python3.7.2 y la pagina corre en codigo de Javascript con JQuery,
aunque no se necesitan conocimiento en ninguno de estos lenguajes 
para utilizar el producto.

Solo se necesita ejecutar un archivo y este es:
    - index.html
Este funciona con los principales navegadores web disponibles

Este contiene todo el codigo necesario para correr y hacer las
llamadas al servidor, de ahi se utiliza la interfaz para elaborar
un sistema y resolverlo.

Si se desea correr de forma local el servidor de python se siguen
los siguientes pasos

1.

    pip3 install -r requirements.txt
    python server.py

2. Modificar index.html para que la variable URL sea igual a:
    "localhost:5000"

3. Ejecutar index.html