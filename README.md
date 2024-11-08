# LangChain LLM Chain Tutorial

Este repositorio es una guía completa para implementar y utilizar `llm_chain` con LangChain. La herramienta `llm_chain` de LangChain facilita la construcción de cadenas que interactúan con modelos de lenguaje de manera estructurada, permitiendo encadenar prompts, modelos y parsers para crear flujos de procesamiento de texto complejos.

## Arquitectura

La arquitectura de `llm_chain` sigue un flujo modular que conecta componentes de manera eficiente. Los principales elementos de la arquitectura son:

1. **Prompt Templates**: Son plantillas que generan los prompts para el modelo. Estas plantillas pueden tener variables dinámicas que se rellenan en cada ejecución de la cadena.
   
2. **LLM (Large Language Model)**: El modelo de lenguaje, como OpenAI o cualquier otro compatible con LangChain, que genera respuestas basadas en los prompts. LangChain proporciona una interfaz unificada para diferentes proveedores de LLM.

3. **Parsers**: Se encargan de procesar y transformar las respuestas del modelo en formatos específicos o extraer solo la información requerida, permitiendo un control sobre el formato de salida.

4. **Chains**: Los elementos anteriores se encadenan para construir flujos de trabajo complejos. Los chains permiten unir varias transformaciones y pasos de procesamiento en un solo flujo, donde la salida de un paso sirve como entrada del siguiente.

5. **Integración con FastAPI**: La herramienta también permite desplegar chains como servicios web mediante FastAPI, facilitando la creación de API RESTful para interactuar con el modelo.

## Instalación

Para ejecutar este programa, asegúrate de tener Python 3.7 o superior.

### Paso 1: Clonar el Repositorio

Primero, clona el repositorio de LangChain para tener acceso a los archivos necesarios.

```bash
git clone https://github.com/langchain/langchain.git
cd langchain


### Paso 2: Ejecutar los dos archivos

Ahora hay que abrir el archivo de Jupyter Notebook y ejecutar cada línea de código. Luego hay que abrir el segundo archivo de Server y ejecutarlo.


### Paso 3: Abrir enlace:

A continuación hay que ingresar al enlace http://localhost:8000/chain/playground/, y con esto entramos a la siguiente página web.

![image](https://github.com/user-attachments/assets/8afbf6f0-1263-4b18-9977-67e519714a43)

Con esto podemos hacer uso de la API para traducir, en este ejemplo podemos traducir a italiano algo como "hi", que es lo que configuramos en los archivos anteriores para que suceda.
