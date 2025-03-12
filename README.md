# Proyecto: Sistema de Gestión de Exámenes

## Descripción
Este proyecto consiste en un servidor HTTP que permite a los profesores gestionar exámenes, definir preguntas, asignar alumnos y calcular puntuaciones.

El sistema está compuesto por:
- **Servidor**: Implementado en **Python** utilizando **Flask-RESTful** para exponer servicios REST.
- **Clientes**: Desarrollados en **Java**, permiten a los profesores y alumnos interactuar con el servidor.
- **Base de Datos**: Implementada en **MySQL** para almacenar información sobre exámenes, preguntas, alumnos y resultados.
- **Formato de Comunicación**: Todas las peticiones y respuestas se manejan en formato **JSON**.

## Características principales
- Creación y gestión de exámenes.
- Añadir o eliminar preguntas en los exámenes.
- Asignación de alumnos a exámenes.
- Registro de respuestas de los alumnos.
- Cálculo y almacenamiento de puntuaciones.
- API REST basada en **Flask-RESTful** para la comunicación entre clientes y servidor.
- Almacenamiento de datos en **MySQL**.

## Tecnologías utilizadas
- **Servidor**: Python, Flask-RESTful  
- **Cliente**: Java (con HTTP requests y JSON parsing)  
- **Base de Datos**: MySQL  
- **Formato de Datos**: JSON  
