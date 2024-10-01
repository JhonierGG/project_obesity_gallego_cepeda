import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Configuración de la conexión
user = 'root'
password = '9904'
host = 'localhost'
database = 'obesity_dataset'
connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)


# Función para cargar datos
def load_data():
    return pd.read_sql('SELECT * FROM `health_data`', con=engine)

# Título de la aplicación
st.title('Análisis de Datos del health_data')

# Contenedor para la tabla y gráficos
table_placeholder = st.empty()
chart_placeholder = st.empty()

# Función para dibujar gráficos
def draw_charts(df):
    chart_placeholder.empty()  # Limpiar el contenedor de gráficos
    
    # Gráfico de distribución de edades
    with chart_placeholder.container():
        st.subheader('Distribución de Edades')
        fig1, ax1 = plt.subplots()
        ax1.hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
        ax1.set_title('Distribución de Edades')
        ax1.set_xlabel('Edad')
        ax1.set_ylabel('Frecuencia')
        st.pyplot(fig1)

        # Gráfico de niveles de obesidad
        st.subheader('Nivel de obesidad')
        fig2 = px.histogram(df, x='NObeyesdad', color='Gender', barmode='group',
                             title='Nivel de obesidad por Género')
        st.plotly_chart(fig2)

        # Gráfico de nivel de obesidad en funcion del consumo de alcohol
        st.subheader('Nivel de obesidad en funcion de consumo de alcohol')
        fig3 = px.histogram(df, x='CALC', color='NObeyesdad', barmode='group',
                             title='Nivel de obesidad en funcion de consumo de alcohol')
        st.plotly_chart(fig3)

        # Gráfico de nivel de obesidad en funcion de actividad fisica
        st.subheader('nivel de obesidad en funcion de actividad fisica')
        fig4 = px.box(df, x='NObeyesdad', y='FAF', title='nivel de obesidad en funcion de actividad fisica')
        st.plotly_chart(fig4)

# Función para mostrar la tabla
def show_table(df):
    table_placeholder.empty()  # Limpiar el contenedor de la tabla
    with table_placeholder.container():
        st.subheader('Datos de la Tabla')
        st.write(f'Cantidad de registros: {len(df)}')  # Mostrar cantidad de datos
        st.write(df.head())  # Mostrar los primeros registros

# Botón para actualizar los datos
if st.button('Actualizar gráficos y tabla'):
    df = load_data()  # Cargar los datos actualizados
    show_table(df)  # Mostrar la tabla actualizada
    draw_charts(df)  # Dibujar gráficos actualizados

# Refresco automático
while True:
    df = load_data()
    show_table(df)  # Mostrar la tabla actualizada
    draw_charts(df)  # Dibujar gráficos actualizados
    time.sleep(10)  # Esperar 10 segundos antes de actualizar