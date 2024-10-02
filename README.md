Problemática

La obesidad es un problema de salud que afecta a personas de todo el mundo, causando problemas físicos y emocionales, y aumentando el riesgo de enfermedades graves como la diabetes, problemas del corazón, y otras condiciones crónicas. A medida que el número de personas con obesidad sigue creciendo, es crucial entender qué factores, como los hábitos alimentarios, la actividad física y otros aspectos del estilo de vida, influyen en su desarrollo. Con esta información, se pueden mejorar las estrategias de prevención y tratamiento para abordar este problema de manera más efectiva.
Información del conjunto de datos - Nivel de obesidad

integrantes: Jhonier Gallego / Ivan cepeda

https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels/data

Este conjunto de datos se centra en la estimación de los niveles de obesidad de individuos en México, Perú y Colombia, utilizando información sobre hábitos alimentarios y condición física. Se compone de 2111 registros y 17 atributos que describen diversas características relacionadas con la salud, como la ingesta de alimentos, la actividad física, el tiempo dedicado a actividades sedentarias, entre otros.

Los datos están etiquetados con una variable de clase llamada "NObesity" que clasifica a los individuos en diferentes categorías de peso: Peso Insuficiente, Peso Normal, Sobrepeso Nivel I, Sobrepeso Nivel II, Obesidad Tipo I, Obesidad Tipo II y Obesidad Tipo III. Esta clasificación permite realizar análisis detallados sobre las tendencias de obesidad y sobrepeso en los países mencionados.

- Genero: Categórico, "Género"
- Edad: Continua, "Edad"
- Altura: Continua, "Altura"
- Peso: Continua, "Peso"
- Historico_familiar_con_sobrepeso: Binario, "¿Algún miembro de su familia ha sufrido o sufre de sobrepeso?"
- FAVC: Binario, "¿Consume alimentos altos en calorías frecuentemente?"
- FCVC: Entero, "¿Suele comer verduras en sus comidas?"
- NCP: Continua, "¿Cuántas comidas principales tiene al día?"
- CAEC: Categórico, "¿Consume algún alimento entre comidas?"
- FUMA: Binario, "¿Fuma?"
- CH2O: Continua, "¿Cuánta agua bebe diariamente?"
- SCC: Binario, "¿Monitorea las calorías que consume diariamente?"
- FAF: Continua, "¿Con qué frecuencia realiza actividad física?"
- TUE: Entero, "¿Cuánto tiempo usa dispositivos tecnológicos como teléfono celular, videojuegos, televisión, computadora y otros?"
- CALC: Categórico, "¿Con qué frecuencia consume alcohol?"
- MTRANS: Categórico, "¿Qué medio de transporte utiliza normalmente?"
- NObeyesdad: Categórico, "Nivel de obesidad"

¿Qué contiene los datos?
este repositorio contiene los siguientes archivos

1) ObesityDataSet_raw_and_data_sinthetic: base de datos
![image](https://github.com/user-attachments/assets/e17c8a1f-f1c7-44c1-879d-ae397657a7d2)


2) Proyecto_V2: Analisis exploratorio del dataset
![image](https://github.com/user-attachments/assets/587ab723-595e-43f6-bf36-97dc95ede409)

![image](https://github.com/user-attachments/assets/1af96f86-d423-4b5a-b5f4-449ad950dc4b)




3) SQL_GALLEGO_CEPEDA: Creacion de base de datos y tablas en SQL
inicialmente se ejecuta codigo para añadir un nuevo usuario, inicialmente hay 2111 y se adiciona el usuario 2112
![image](https://github.com/user-attachments/assets/501c7403-4512-48c8-9c48-cd378a3d7753)

codigo para crear nuevo usuario

![image](https://github.com/user-attachments/assets/037f0345-a13d-4082-bd7a-c796be61d17e)

vista SQL conla creacion del nuevo usuario

posteriormente se realiza una funcion para crear multiples usuarios, en este paso se adicionan 3 nuevos usuarios

![image](https://github.com/user-attachments/assets/0442e832-0534-486d-882b-2f9dfd05e1d2)

codigo para crear los multiples usuarios

![image](https://github.com/user-attachments/assets/175abe6c-6589-4114-94f5-76d46eef07c0)

vista SQL con la creacion de multiples usuarios

una vez se crean los multiples usuarios, se realiza la modificacion de uno de los registros creados, en este caso se modifica la edad del ultimo usuario registrado, pasando de 18 a 35 años

![image](https://github.com/user-attachments/assets/83ca79ec-186c-4a43-931c-0a23c57e9724)

codigo para cmodificar registro

![image](https://github.com/user-attachments/assets/463e301b-e550-44b9-b6a6-c985c0b3d70f)

vista SQL con la modificacion

finalmente se realiza eliminacion de un registro, en este caso se elimina el usuario 2114

![image](https://github.com/user-attachments/assets/018aa511-11a2-46f7-b3a0-603113b4b405)

codigo para eliminar registro

![image](https://github.com/user-attachments/assets/b98d381b-6c17-45c3-ab90-08b9ec1bb0a7)

vista SQL sin el usuario 2114


4) app: despliegue de la informacion relevante del dataset de manera grafica (localhost)

![image](https://github.com/user-attachments/assets/548c7a11-a648-44d3-8bf7-25c0e98ea587)


Valor Generado

Este conjunto de datos proporciona información útil para investigadores, médicos, y responsables de políticas públicas que buscan enfrentar la obesidad de manera más efectiva. Al analizar los datos, se pueden identificar patrones y factores que contribuyen al aumento de peso en las personas. Esto puede ayudar a diseñar programas de prevención, campañas de concientización y políticas de salud más eficaces, con el objetivo de prevenir y tratar la obesidad. Además, este análisis puede ser la base para desarrollar herramientas de predicción que permitan una intervención temprana y más personalizada en personas con riesgo de desarrollar obesidad.
