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
    return pd.read_sql('SELECT * FROM health_data', con=engine)

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

        # Gráfico de nivel de obesidad en función del consumo de alcohol
        st.subheader('Nivel de obesidad en función de consumo de alcohol')
        fig3 = px.histogram(df, x='CALC', color='NObeyesdad', barmode='group',
                             title='Nivel de obesidad en función de consumo de alcohol')
        st.plotly_chart(fig3)

        # Gráfico de nivel de obesidad en función de actividad física
        st.subheader('Nivel de obesidad en función de actividad física')
        fig4 = px.box(df, x='NObeyesdad', y='FAF', title='Nivel de obesidad en función de actividad física')
        st.plotly_chart(fig4)
        
        # Gráfico de nivel de obesidad en función del Peso
        st.subheader('Nivel de obesidad en función del Peso')
        fig5 = px.box(df, x='NObeyesdad', y='Weight', title='Nivel de obesidad en función del Peso')
        st.plotly_chart(fig5)

        # Gráfico de nivel de obesidad en función del número de comidas principales
        st.subheader('Nivel de obesidad en función del número de comidas principales')
        fig6 = px.box(df, x='NObeyesdad', y='NCP', title='Nivel de obesidad en función del número de comidas principales')
        st.plotly_chart(fig6)

        # Gráfico de nivel de obesidad en función del consumo de verduras
        st.subheader('Nivel de obesidad en función del consumo de verduras')
        fig7 = px.box(df, x='NObeyesdad', y='FCVC', title='Nivel de obesidad en función del consumo de verduras')
        st.plotly_chart(fig7)

        # Gráfico de nivel de obesidad en función del medio de transporte 
        st.subheader('Nivel de obesidad en función del medio de transporte')
        fig8 = px.histogram(df, x='NObeyesdad', color='MTRANS', barmode='group',
                             title='Nivel de obesidad en función del medio de transporte')
        st.plotly_chart(fig8)

        # Gráfico de nivel de obesidad en función del histórico familiar con sobrepeso
        st.subheader('Nivel de obesidad en función del histórico familiar con sobrepeso')
        fig9 = px.histogram(df, x='family_history_with_overweight', color='NObeyesdad', barmode='group',
                             title='Nivel de obesidad en función del histórico familiar con sobrepeso')
        st.plotly_chart(fig9)


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






