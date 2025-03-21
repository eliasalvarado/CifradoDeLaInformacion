<!--
PROJECT NAME
-->

# Laboratorio 3 - Cifrados Simetricos
<a id="readme-top"></a>

<!--
PROJECT DESCRIPTION
-->
## 📜 Descripción

El laboratorio tiene como objetivo implementar distintos cifrados en un entorno real. Cifrados como AES en dos modos de operación, ECB y CBC. También el algoritmo de cifrado Chacha20 y comparar su rendimiento con AES-CBC. Se busca comprender los riesgos que tiene utilizar un modo de operación inadecuado para un escenario, en este caso se analizó como el modo de operación ECB para AES no es adecuado para el cifrado de imágenes. En otra parte se buscó implementar un entorno de mensajería entre computadoras donde un atacante haría el papel del MitM con el fin de capturar paquetes que tendrían los mensajes cifrados y explorar si con la información obtenida se podían romper los cifrados.

El ejercicio se realizó utilizando un Jupyter Notebook, por lo que su ejecución es tan sencilla como un simple clic al botón 'Ejecutar todo' en el entorno que abra el Notebook.

Para esos fines se implementó:
    - Cifrado y descifrado utilizando AES en modo de operación ECB y CBC.
    - Servidor y cliente para mensajería por medio de sockets TCP.
    - Cifrado y descifrado utilizando Chacha20.
    - Encriptación y desencriptación de un conjunto de archivos utilizando AES-CBC.

* https://github.com/eliasalvarado/CifradoDeLaInformacion/tree/main/Laboratorios/Lab3


## 📦 Dependencias

Las principales dependencias del proyecto incluyen:
* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>

## 👥 Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:
1. Realiza un fork del repositorio.
2.	Crea una nueva rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
3.	Haz commit de tus cambios (git commit -m 'Añadir nueva funcionalidad').
4.	Haz push a la rama (git push origin feature/nueva-funcionalidad).
5.	Abre un Pull Request.

### Developer's

<a href="https://github.com/eliasalvarado">
  <img width='75' src="https://avatars.githubusercontent.com/u/16949087?v=4" alt="Elias Alvarado" />
</a>

* [![Linkedin][Linkedin]][Linkedin-lud]
* [![GitHub][GitHub]][GitHub-lud]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>

## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarnos a traves de nuestras redes sociales:

* [![Linkedin][Linkedin]][Linkedin-lud]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Linkedin-lud]: https://www.linkedin.com/in/ealvaradorax/
[Linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Github-lud]: https://github.com/eliasalvarado
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white