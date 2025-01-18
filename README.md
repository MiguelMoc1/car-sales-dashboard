# Car sales dashboard
# Panel de Control de Anuncios de Venta de Coches

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva para visualizar y analizar datos de anuncios de venta de coches. La aplicación permite a los usuarios explorar el conjunto de datos a través de diversos gráficos y realizar análisis exploratorios de manera interactiva utilizando Streamlit.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│ └── EDA.ipynb
└── .streamlit
└── config.toml

## Archivos Principales

- **README.md**: Este archivo, que proporciona una descripción del proyecto, instrucciones de instalación y uso.
- **app.py**: Contiene el código de la aplicación web desarrollada con Streamlit.
- **vehicles_us.csv**: Conjunto de datos de anuncios de venta de coches utilizado para el análisis.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar la aplicación.
- **notebooks/EDA.ipynb**: Jupyter Notebook con el análisis exploratorio de datos (EDA).
- **.streamlit/config.toml**: Archivo de configuración de Streamlit para el despliegue.

## Requisitos

Para ejecutar este proyecto, necesitarás instalar las siguientes dependencias:

- pandas
- plotly-express
- streamlit

Puedes instalarlas ejecutando el siguiente comando:

```sh
pip install -r requirements.txt
Análisis Exploratorio de Datos (EDA)
El análisis exploratorio de datos se encuentra en el archivo notebooks/EDA.ipynb. Este notebook incluye visualizaciones como:

Histogramas del odómetro
Gráficos de dispersión del odómetro vs precio y año vs precio
Gráficos de barras del número de coches por tipo
Gráficos de caja del precio por tipo de coche
Aplicación Web
La aplicación web desarrollada con Streamlit permite a los usuarios interactuar con los datos y generar gráficos en tiempo real. La aplicación incluye las siguientes funcionalidades:

Construcción de histogramas del odómetro
Construcción de gráficos de dispersión del odómetro vs precio y año vs precio
Construcción de gráficos de barras del número de coches por tipo
Construcción de gráficos de caja del precio por tipo de coche
Ejecución de la Aplicación
Para ejecutar la aplicación, sigue estos pasos:

Clona el repositorio en tu máquina local:
git clone https://github.com/MiguelMoc1/newproject.git
cd newproject
Crea y activa un entorno virtual:
python -m venv vehicles_env
.\vehicles_env\Scripts\activate
Instala las dependencias:
pip install -r requirements.txt
Ejecuta la aplicación de Streamlit:
streamlit run app.py
Despliegue
La aplicación está configurada para ser desplegada en Render. El archivo .streamlit/config.toml contiene la configuración necesaria para el despliegue.

Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor, abre un issue o envía un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
Con esta descripción en el archivo `README.md`, los usuarios tendrán una comprensión clara del propósito y estructura del proyecto, así como instrucciones detalladas para la instalación, ejecución y despliegue de la aplicación. Si necesitas más detalles o ajustes específicos, no dudes en preguntar. ¡Estoy aquí para ayudarte!


