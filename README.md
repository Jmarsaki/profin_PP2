# Una medición de impacto de políticas de innovación energética 
Este es un proyecto de software para medir posible impacto en políticas de innovación energética. 
Se realizará un analisis de datos para detectar el impacto producido en el mercado en las fluctuaciones de los incrementos de energías renovables en Nueva Zelanda tomando datasets publicados por el mismo gobierno. Seguidamente se aplicarán los datos resultantes a una matriz DAFO para medir y sacar conclusiones sobre dicho impacto.
Estructura del repositorio:
Carpeta "documentos": Contendrá archivos referentes al control y al manejo de la aplicación.
Carpeta "data": Contendrá los conjuntos de datos utilizados para el entrenamiento y evaluación en la realización del modelo.
Carpeta "testing": Contendrá los script de testing del modelo.
Carpeta "medimpapp_train": Contendrá el código fuente para entrenamiento del modelo.
Archivo "main": Contiene al código fuente de la aplicación en lenguaje Python y los recursos necesarios para montarlo como aplicación desde Flask.
README.md: Es el texto con las especificaciones del modelo.
 # Indicaciones para poner en marcha la aplicación
 Para activar desde Flask, esta aplicación que se encuentra en un repositorio de GitHub, por ejemplo, desde Visual Studio Code, se pueden seguir los pasos:
    1. Clonar el repositorio: Abrir Visual Studio Code y clonar el repositorio de GitHub que contiene la aplicación (Flask). Esto se puede hacer  desde la barra lateral de Visual Studio Code haciendo clic en el icono de Git (tercer icono de la izquierda) y luego en "Clonar Repositorio". Se ingresa la URL del repositorio y se selecciona una ubicación local para clonarlo.
    2. Configurar el entorno virtual (opcional): Es recomendable la utilización de un entorno virtual para la aplicación Flask. Particularmente el autor de la aplicación, usa una máquina virtual Ubuntu de Linux. Si se elige la terminal de Visual Studio Code, se debe navegar hasta la carpeta del proyecto y crear un entorno virtual con el siguiente comando (reemplaza "venv" con el nombre que desees para el entorno virtual):
       Copy code
       python -m venv venv
       Luego, dependiendo del sistema operativo, activar el entorno virtual con:
        ◦ En Windows:
        
          venv\Scripts\activate
          
        ◦ En macOS o Linux:
        
          bash
          
          source venv/bin/activate
          
    3. Instalar las dependencias: Asegúrarse de que todas las dependencias requeridas para la aplicación con Flask estén instaladas en el entorno virtual. Se pueden instalar desde el archivo "requirements.txt" con el siguiente comando:
       pip install -r requirements.txt
    4. Definir el archivo de entrada: Asegurarse de que  aplicación tenga un archivo de entrada principal. Por convención, se llamará "app.py", pero puede tener otro nombre. Este archivo debe contener la instancia de la aplicación y todas las rutas y lógica de la aplicación.
    5. Ejecutar la aplicación: Desde la terminal de Visual Studio Code, navegar hasta el directorio que contiene el archivo de entrada de la aplicación y ejecutar el siguiente comando:
       arduino
       flask run
       Esto iniciará el servidor de desarrollo de Flask y la aplicación ya estará activa en http://127.0.0.1:5000/. Se puede acceder a la aplicación desde el navegador web visitando esa dirección.
Si la aplicación requiere configuraciones adicionales, como la conexión a una base de datos o la configuración de variables de entorno, se deben realizar los pasos adicionales antes de ejecutar la aplicación.
       Si se elige la terminal de Ubuntu para activar la aplicación con Flask desde la terminal de Ubuntu, sigue estos pasos:

Abrir la terminal:
Puedes abrir la terminal presionando Ctrl + Alt + T o buscando "Terminal" en el menú de aplicaciones.

Navega al directorio de tu aplicación:
Utiliza el comando cd para navegar al directorio donde tienes almacenados los archivos de tu aplicación Flask. Por ejemplo, si tu aplicación está en el directorio mi_app, ejecuta:

bash
cd /ruta/a/tu/directorio/mi_app

Verificar que el entorno virtual esté activado (opcional pero recomendado):
Si se está utilizando un entorno virtual (virtualenv) para gestionar las dependencias de tu aplicación Flask, asegúrarse de activarlo antes de continuar. Si no se elige un entorno virtual, se puede saltear este paso. Para activar el entorno virtual, se ejecuta el siguiente comando:

bash
source nombre_entorno_virtual/bin/activate
Donde nombre_entorno_virtual es el nombre del directorio de tu entorno virtual.

Ejecutar la aplicación:
Utilizar el comando flask run para ejecutar tu aplicación Flask:

arduino
flask run
Si todo está configurado correctamente, se verá un mensaje indicando que el servidor se está ejecutando y en qué dirección IP y puerto está escuchando. Flask se ejecuta en http://127.0.0.1:5000/ por defecto.

Acceder a la aplicación desde un navegador:
Abrir el navegador web elegido y navegar a la dirección proporcionada por Flask (por lo general, http://127.0.0.1:5000/). Allí se debería poder ver la aplicación Flask en funcionamiento.

Detener el servidor Flask:
Para detener el servidor Flask, se presiona Ctrl + C en la terminal donde se está ejecutando. Esto detendrá el servidor y dejará de servir la aplicación.


A partir de aquí, se deben preparar los datos de entrada si se hacen predicciones sobre nuevos datos de forma adecuada para que sean compatibles con el modelo entrenado. La interfaz web tiene un displey para cargar el archivo CSV y luego posee uno para mostrar los resultados presionando el botón de cálculo. Se deben proveer los valores numéricos enteros de las FORTALEZAS, OPORTUNIDADES, DEBILIDADES y AMENAZAS. Luego, la aplicación devuelve la predicción sobre el incremento de producción del año a anticipar y su incremento de producción porcentual junto a los impactos sobre las FORTALEZAS, OPORTUNIDADES, DEBILIDADES y AMENAZAS sobre el mismo año.
 
Este es un proyecto realizado por Julio Mariano Sachi de TCDIA en el ISPC.
