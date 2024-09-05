# Proyecto de Automatización con Playwright

Este proyecto está diseñado para automatizar la creación de un nuevo empleado en OrangeHRM utilizando Playwright.

## Requisitos

- Python instalado en tu sistema.
- Playwright y otras dependencias especificadas en el archivo `requirements.txt`.

## Pasos para configurar y ejecutar el proyecto

1. **Crear un entorno virtual**

   Primero, crea un entorno virtual para gestionar las dependencias del proyecto. Ejecuta el siguiente comando:

   ```bash
    `py -m venv venv`
   ```

2. **Acceder al entorno virtual**

   Activa el entorno virtual creado anteriormente:

   ```bash
    `venv\Scripts\activate`
   ```

3. **Instalar los módulos**

   Instala las dependencias necesarias que están listadas en el archivo `requirements.txt`:

   ```bash
   `pip install -r requirements.txt`
   ```

4. **Instalar Playwright**

   Es necesario instalar Playwright y sus navegadores para poder ejecutar las automatizaciones:

   ```bash
   `playwright install`
   ```

5. **Ejecutar el archivo de prueba**

   Finalmente, ejecuta el archivo `main_test.py` para correr las pruebas automatizadas:

   ```bash
   `py main_test.py`
   ```

## Notas adicionales

- Asegúrate de que el entorno virtual esté activado antes de ejecutar los comandos de instalación y pruebas.
- Si encuentras algún problema con las dependencias, revisa que todos los módulos necesarios estén correctamente listados en `requirements.txt`.
