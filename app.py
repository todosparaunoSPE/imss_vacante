# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 11:06:10 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime  # <-- AGREGAR ESTA LÍNEA

# Configuración de la página
st.set_page_config(
    page_title="Simulador de Funciones - Política Fiscal IMSS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🏛️ Simulador de Funciones - Subdivisión de Política Fiscal")
st.markdown("**Herramienta interactiva para demostrar las capacidades requeridas en la vacante**")

# Sidebar con información de la vacante
with st.sidebar:
    # AGREGADO: Nombre y fecha
    st.header("👤 Información del Candidato")
    st.markdown("**Nombre:** Javier Horacio Pérez Ricárdez")
    st.markdown(f"**Fecha:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    st.divider()
    
    st.header("📋 Información de la Vacante")
    st.markdown("""
    **Puesto:** Subjefe de División de Política Fiscal  
    **Nivel:** N31  
    **Salario:** $53,000 MXN brutos mensuales  
    **Área:** Coordinación de Planeación y Evaluación
    """)
    
    st.divider()
    st.markdown("### 🎯 Funciones Disponibles")
    st.markdown("Selecciona una función para explorar en los botones:")

# Lista de funciones del puesto
funciones = {
    "Presupuesto": "Integrar información para el anteproyecto de presupuesto",
    "Análisis Reformas": "Evaluar impacto recaudatorio de reformas",
    "Estudios Investigación": "Elaborar estudios de seguridad social y mercado laboral",
    "Reportes Avances": "Generar reportes de acciones y logros",
    "Metas Desempeño": "Definir metas para unidades administrativas",
    "Detección Anomalías": "Identificar esquemas de comportamiento atípicos"
}

# Usar session_state para mantener la función seleccionada
if 'selected_funcion' not in st.session_state:
    st.session_state.selected_funcion = None

# Crear botones para cada función
cols = st.columns(3)
for i, (funcion, descripcion) in enumerate(funciones.items()):
    with cols[i % 3]:
        if st.button(f"**{funcion}**", use_container_width=True, key=f"btn_{funcion}"):
            st.session_state.selected_funcion = funcion
            st.rerun()

# Si no se ha seleccionado ninguna función, mostrar pantalla de inicio
if not st.session_state.selected_funcion:
    st.markdown("---")
    st.subheader("🚀 Bienvenido/a al Simulador de Funciones")
    st.markdown("""
    Esta herramienta demuestra las capacidades técnicas y analíticas requeridas para el puesto de 
    **Subjefe de División de Política Fiscal** en el IMSS.
    
    ### 📊 Características:
    - Análisis de datos con Python y Pandas
    - Visualizaciones interactivas con Plotly
    - Simulación de escenarios presupuestales
    - Detección de anomalías en datos
    - Reportes ejecutivos automatizados
    
    ### 👆 **Selecciona una función en los botones superiores para comenzar**
    """)
    
    # Mostrar datos de ejemplo
    st.markdown("### 📈 Vista Previa de Datos de Ejemplo")
    
    # Generar datos sintéticos de afiliación
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    afiliados = np.random.randint(18000000, 22000000, size=12)
    recaudacion = np.random.randint(45000, 65000, size=12) * 1000
    
    df_ejemplo = pd.DataFrame({
        'Mes': meses,
        'Afiliados': afiliados,
        'Recaudación (MXN)': recaudacion
    })
    
    st.dataframe(df_ejemplo, use_container_width=True)
    
    # Gráfico de ejemplo
    fig = px.line(df_ejemplo, x='Mes', y='Afiliados', 
                  title='Tendencia de Afiliados Mensual (Ejemplo)',
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

# FUNCIÓN 1: PRESUPUESTO
elif st.session_state.selected_funcion == "Presupuesto":
    st.header("💰 Integración de Información para Presupuesto")
    
    st.markdown("""
    **Objetivo:** Elaborar diferentes escenarios del anteproyecto de presupuesto de ingresos y egresos
    """)
    
    # Simulación de escenarios presupuestales
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("⚙️ Parámetros del Escenario")
        crecimiento = st.slider("Crecimiento esperado (%)", -5.0, 15.0, 3.5, 0.5, key="presupuesto_crecimiento")
        inflacion = st.slider("Inflación esperada (%)", 2.0, 8.0, 4.0, 0.1, key="presupuesto_inflacion")
        año_base = st.number_input("Presupuesto base (millones MXN)", 50000, 200000, 120000, key="presupuesto_base")
        
        if st.button("Generar Escenarios Presupuestales", key="btn_generar_presupuesto"):
            st.success("✅ Escenarios generados exitosamente")
    
    with col1:
        # Generar datos para escenarios presupuestales
        años = [2024, 2025, 2026, 2027]
        escenario_conservador = [año_base, 
                               año_base * (1 + (crecimiento-1)/100),
                               año_base * (1 + (crecimiento-1)/100)**2,
                               año_base * (1 + (crecimiento-1)/100)**3]
        
        escenario_moderado = [año_base,
                            año_base * (1 + crecimiento/100),
                            año_base * (1 + crecimiento/100)**2,
                            año_base * (1 + crecimiento/100)**3]
        
        escenario_optimista = [año_base,
                             año_base * (1 + (crecimiento+2)/100),
                             año_base * (1 + (crecimiento+2)/100)**2,
                             año_base * (1 + (crecimiento+2)/100)**3]
        
        df_presupuesto = pd.DataFrame({
            'Año': años,
            'Conservador': [f"${x/1000:,.1f}M" for x in escenario_conservador],
            'Moderado': [f"${x/1000:,.1f}M" for x in escenario_moderado],
            'Optimista': [f"${x/1000:,.1f}M" for x in escenario_optimista]
        })
        
        st.subheader("📊 Escenarios Presupuestales Proyectados")
        st.dataframe(df_presupuesto, use_container_width=True)
        
        # Gráfico de escenarios
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=años, y=escenario_conservador, 
                               mode='lines+markers', name='Conservador',
                               line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=años, y=escenario_moderado, 
                               mode='lines+markers', name='Moderado'))
        fig.add_trace(go.Scatter(x=años, y=escenario_optimista, 
                               mode='lines+markers', name='Optimista',
                               line=dict(dash='dot')))
        
        fig.update_layout(title='Proyección de Escenarios Presupuestales',
                         xaxis_title='Año',
                         yaxis_title='Presupuesto (Millones MXN)')
        st.plotly_chart(fig, use_container_width=True)

# FUNCIÓN 2: ANÁLISIS DE REFORMAS

# FUNCIÓN 2: ANÁLISIS DE REFORMAS
elif st.session_state.selected_funcion == "Análisis Reformas":
    st.header("📊 Evaluación de Impacto Recaudatorio de Reformas")
    
    st.markdown("""
    **Objetivo:** Analizar el impacto recaudatorio de reformas propuestas a la Ley del Seguro Social
    """)
    
    # Simulación de impacto de reformas
    reformas = [
        "Incremento cuota patronal 1%",
        "Reducción cuota trabajador 0.5%", 
        "Nuevo esquema para PyMEs",
        "Ampliación base de cotización",
        "Incorporación sector informal"
    ]
    
    # Datos base que pueden cambiar con la sensibilidad
    impacto_base = [15.5, -8.2, 3.7, 12.8, 22.3]
    confianza = [85, 78, 65, 82, 60]
    
    col1, col2 = st.columns([3, 2])
    
    with col2:
        st.subheader("📋 Configuración del Análisis")
        
        # Selector de reforma específica
        reforma_seleccionada = st.selectbox("Selecciona una reforma para análisis detallado:", reformas, key="reforma_select")
        
        if reforma_seleccionada:
            idx = reformas.index(reforma_seleccionada)
            
            # Análisis de sensibilidad
            st.subheader("🔍 Análisis de Sensibilidad")
            sensibilidad = st.slider("Variación en supuestos clave (%)", -20, 20, 0, key="sensibilidad_slider")
            
            # Calcular impacto ajustado
            impacto_ajustado = impacto_base[idx] * (1 + sensibilidad/100)
            
            # Mostrar métricas
            col_metric1, col_metric2 = st.columns(2)
            with col_metric1:
                st.metric("Impacto Base", f"{impacto_base[idx]}%")
                st.metric("Impacto Ajustado", f"{impacto_ajustado:.1f}%", 
                         delta=f"{impacto_ajustado - impacto_base[idx]:+.1f}%")
            with col_metric2:
                st.metric("Nivel de Confianza", f"{confianza[idx]}%")
                
                # Calcular confianza ajustada (inversamente proporcional a la variación)
                confianza_ajustada = max(0, min(100, confianza[idx] - abs(sensibilidad)))
                st.metric("Confianza Ajustada", f"{confianza_ajustada:.0f}%")
    
    with col1:
        st.subheader("📈 Impacto de Reformas Propuestas")
        
        # Crear DataFrame actualizado con los impactos ajustados
        if reforma_seleccionada:
            idx = reformas.index(reforma_seleccionada)
            impacto_actualizado = impacto_base.copy()
            impacto_actualizado[idx] = impacto_base[idx] * (1 + sensibilidad/100)
        else:
            impacto_actualizado = impacto_base
        
        df_reformas = pd.DataFrame({
            'Reforma': reformas,
            'Impacto Esperado (%)': impacto_actualizado,
            'Nivel de Confianza (%)': confianza,
            'Tamaño Visual': [abs(x) + 10 for x in impacto_actualizado]  # CORREGIDO: Valores positivos para tamaño
        })
        
        # Gráfico de barras interactivo
        fig = px.bar(df_reformas, x='Reforma', y='Impacto Esperado (%)',
                    color='Impacto Esperado (%)',
                    title='Impacto Recaudatorio Esperado por Reforma',
                    color_continuous_scale='RdYlGn',
                    hover_data=['Nivel de Confianza (%)'])
        
        # Destacar la reforma seleccionada
        if reforma_seleccionada:
            idx_seleccionado = reformas.index(reforma_seleccionada)
            fig.add_annotation(
                x=idx_seleccionado,
                y=impacto_actualizado[idx_seleccionado],
                text="🔍 Seleccionada",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="red",
                bgcolor="white",
                bordercolor="red",
                borderwidth=1
            )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Gráfico adicional: Comparación de confianza vs impacto
        st.subheader("📊 Relación Impacto-Confianza")
        
        # CORREGIDO: Usar valores absolutos para el tamaño y añadir colores por tipo de impacto
        df_reformas['Tipo Impacto'] = ['Positivo' if x > 0 else 'Negativo' for x in df_reformas['Impacto Esperado (%)']]
        
        fig2 = px.scatter(df_reformas, 
                         x='Impacto Esperado (%)', 
                         y='Nivel de Confianza (%)',
                         size='Tamaño Visual',  # CORREGIDO: Usar valores positivos
                         text='Reforma',
                         title='Relación entre Impacto Esperado y Nivel de Confianza',
                         size_max=25,
                         color='Tipo Impacto',  # Color por tipo de impacto
                         color_discrete_map={'Positivo': 'green', 'Negativo': 'red'},
                         hover_data=['Impacto Esperado (%)', 'Nivel de Confianza (%)'])
        
        # Destacar punto seleccionado
        if reforma_seleccionada:
            fig2.add_annotation(
                x=impacto_actualizado[idx],
                y=confianza[idx],
                text="● Seleccionada",
                showarrow=True,
                arrowhead=2,
                font=dict(color="blue", size=12, weight="bold")
            )
        
        fig2.update_traces(
            textposition='top center',
            marker=dict(sizemode='diameter', sizeref=2.0)
        )
        fig2.update_layout(
            xaxis_title="Impacto Esperado (%)",
            yaxis_title="Nivel de Confianza (%)",
            showlegend=True
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Análisis de escenarios
    st.subheader("🎯 Simulación de Escenarios")
    
    if reforma_seleccionada:
        idx = reformas.index(reforma_seleccionada)
        
        col_scenario1, col_scenario2, col_scenario3 = st.columns(3)
        
        with col_scenario1:
            st.markdown("**🔻 Escenario Conservador**")
            impacto_conservador = impacto_base[idx] * 0.7
            recaudacion_base = 100000  # Base de 100,000 millones
            recaudacion_conservador = recaudacion_base * (impacto_conservador / 100)
            st.metric("Impacto Estimado", f"{impacto_conservador:.1f}%")
            st.metric("Recaudación Anual", f"${recaudacion_conservador:,.0f} M")
        
        with col_scenario2:
            st.markdown("**📊 Escenario Base**")
            impacto_base_val = impacto_base[idx]
            recaudacion_base_val = recaudacion_base * (impacto_base_val / 100)
            st.metric("Impacto Estimado", f"{impacto_base_val:.1f}%")
            st.metric("Recaudación Anual", f"${recaudacion_base_val:,.0f} M")
        
        with col_scenario3:
            st.markdown("**🔺 Escenario Optimista**")
            impacto_optimista = impacto_base[idx] * 1.3
            recaudacion_optimista = recaudacion_base * (impacto_optimista / 100)
            st.metric("Impacto Estimado", f"{impacto_optimista:.1f}%")
            st.metric("Recaudación Anual", f"${recaudacion_optimista:,.0f} M")
        
        # Gráfico de comparación de escenarios
        st.subheader("📈 Comparativa de Escenarios")
        
        escenarios = ['Conservador', 'Base', 'Optimista']
        impactos_escenarios = [impacto_conservador, impacto_base_val, impacto_optimista]
        recaudaciones = [recaudacion_conservador, recaudacion_base_val, recaudacion_optimista]
        
        fig_escenarios = go.Figure()
        
        fig_escenarios.add_trace(go.Bar(
            name='Impacto (%)',
            x=escenarios,
            y=impactos_escenarios,
            yaxis='y',
            offsetgroup=1,
            marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1']
        ))
        
        fig_escenarios.add_trace(go.Scatter(
            name='Recaudación (M$)',
            x=escenarios,
            y=recaudaciones,
            yaxis='y2',
            mode='lines+markers',
            line=dict(color='#FFE66D', width=3),
            marker=dict(size=8)
        ))
        
        fig_escenarios.update_layout(
            title=f'Comparación de Escenarios - {reforma_seleccionada}',
            xaxis=dict(title='Escenarios'),
            yaxis=dict(title='Impacto (%)', side='left'),
            yaxis2=dict(title='Recaudación Anual (Millones MXN)', side='right', overlaying='y'),
            showlegend=True
        )
        
        st.plotly_chart(fig_escenarios, use_container_width=True)
    
    # Timeline de implementación
    if reforma_seleccionada:
        st.subheader("📅 Cronograma de Implementación Estimado")
        
        fases = ['Análisis', 'Discusión', 'Aprobación', 'Implementación', 'Evaluación']
        meses = [3, 6, 9, 12, 18]
        
        df_timeline = pd.DataFrame({
            'Fase': fases,
            'Meses': meses,
            'Progreso': [25, 50, 75, 90, 100]
        })
        
        fig_timeline = px.line(df_timeline, x='Meses', y='Progreso', 
                              markers=True, 
                              title=f'Cronograma para: {reforma_seleccionada}',
                              line_shape='linear')
        
        # Añadir anotaciones para cada fase
        for i, fase in enumerate(fases):
            fig_timeline.add_annotation(
                x=meses[i],
                y=df_timeline['Progreso'][i],
                text=fase,
                showarrow=True,
                arrowhead=2,
                yshift=10,
                bgcolor='lightblue'
            )
        
        fig_timeline.update_layout(
            xaxis_title="Meses desde inicio",
            yaxis_title="% de Progreso",
            yaxis_range=[0, 100],
            xaxis_range=[0, 20]
        )
        st.plotly_chart(fig_timeline, use_container_width=True)





# FUNCIÓN 3: ESTUDIOS E INVESTIGACIÓN  
elif st.session_state.selected_funcion == "Estudios Investigación":
    st.header("🔬 Estudios e Investigación en Seguridad Social")
    
    st.markdown("""
    **Objetivo:** Elaborar estudios en materia de seguridad social, salud, economía y mercado laboral
    """)
    
    # Datos sintéticos de mercado laboral
    sectores = ['Manufactura', 'Servicios', 'Comercio', 'Construcción', 'Agricultura', 'Salud', 'Educación']
    afiliados_por_sector = np.random.randint(500000, 3500000, size=len(sectores))
    crecimiento_sector = np.random.uniform(-2.0, 8.0, size=len(sectores))
    informalidad = np.random.uniform(15.0, 65.0, size=len(sectores))
    
    df_sectores = pd.DataFrame({
        'Sector': sectores,
        'Afiliados': afiliados_por_sector,
        'Crecimiento Anual (%)': crecimiento_sector,
        'Tasa Informalidad (%)': informalidad
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Afiliados por Sector Económico")
        
        # Gráfico de torta
        fig = px.pie(df_sectores, values='Afiliados', names='Sector',
                    title='Distribución de Afiliados por Sector Económico')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Crecimiento vs Informalidad")
        
        # Gráfico de dispersión
        fig = px.scatter(df_sectores, x='Crecimiento Anual (%)', y='Tasa Informalidad (%)',
                        size='Afiliados', text='Sector',
                        title='Relación entre Crecimiento e Informalidad por Sector',
                        size_max=60)
        fig.update_traces(textposition='top center')
        st.plotly_chart(fig, use_container_width=True)
    
    # Análisis correlacional
    st.subheader("📊 Análisis de Correlaciones")
    
    correlacion = np.corrcoef(df_sectores['Crecimiento Anual (%)'], 
                             df_sectores['Tasa Informalidad (%)'])[0,1]
    
    # CORREGIDO: st.metric sin parámetro key
    st.metric("Correlación Crecimiento-Informalidad", f"{correlacion:.3f}")
    
    if correlacion < -0.3:
        st.info("🔍 **Hallazgo:** Existe correlación negativa significativa entre crecimiento e informalidad")
    elif correlacion > 0.3:
        st.info("🔍 **Hallazgo:** Existe correlación positiva significativa entre crecimiento e informalidad")
    else:
        st.info("🔍 **Hallazgo:** No existe correlación significativa entre las variables")

# FUNCIÓN 4: REPORTES DE AVANCES
elif st.session_state.selected_funcion == "Reportes Avances":
    st.header("📋 Generación de Reportes de Avances y Logros")
    
    st.markdown("""
    **Objetivo:** Elaborar propuestas de reportes que muestren acciones, avances y logros en afiliación y recaudación
    """)
    
    # Datos sintéticos para reportes
    estados = ['CDMX', 'Jalisco', 'Nuevo León', 'Puebla', 'Veracruz', 'Chiapas', 'Baja California']
    meta_afiliacion = np.random.randint(80000, 300000, size=len(estados))
    avance_afiliacion = [int(x * np.random.uniform(0.6, 1.2)) for x in meta_afiliacion]
    meta_recaudacion = np.random.randint(2000, 8000, size=len(estados)) * 1000
    avance_recaudacion = [int(x * np.random.uniform(0.7, 1.3)) for x in meta_recaudacion]
    
    df_reportes = pd.DataFrame({
        'Estado': estados,
        'Meta Afiliación': meta_afiliacion,
        'Avance Afiliación': avance_afiliacion,
        '% Avance Afiliación': [f"{(a/m)*100:.1f}%" for a, m in zip(avance_afiliacion, meta_afiliacion)],
        'Meta Recaudación (MXN)': [f"${m:,.0f}" for m in meta_recaudacion],
        'Avance Recaudación (MXN)': [f"${a:,.0f}" for a in avance_recaudacion],
        '% Avance Recaudación': [f"{(a/m)*100:.1f}%" for a, m in zip(avance_recaudacion, meta_recaudacion)]
    })
    
    st.subheader("📈 Dashboard de Avances por Estado")
    st.dataframe(df_reportes, use_container_width=True)
    
    # Selector de estado para detalle
    estado_seleccionado = st.selectbox("Selecciona un estado para reporte detallado:", estados, key="estado_select")
    
    if estado_seleccionado:
        idx = estados.index(estado_seleccionado)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            # CORREGIDO: st.metric sin parámetro key
            st.metric("Meta Afiliación", f"{meta_afiliacion[idx]:,}")
            st.metric("Avance Afiliación", f"{avance_afiliacion[idx]:,}")
        
        with col2:
            porcentaje_afiliacion = (avance_afiliacion[idx] / meta_afiliacion[idx]) * 100
            st.metric("% Avance Afiliación", f"{porcentaje_afiliacion:.1f}%")
        
        with col3:
            st.metric("Meta Recaudación", f"${meta_recaudacion[idx]:,}")
            st.metric("Avance Recaudación", f"${avance_recaudacion[idx]:,}")
        
        with col4:
            porcentaje_recaudacion = (avance_recaudacion[idx] / meta_recaudacion[idx]) * 100
            st.metric("% Avance Recaudación", f"{porcentaje_recaudacion:.1f}%")
        
        # Gráfico de progreso
        fig = go.Figure()
        
        fig.add_trace(go.Indicator(
            mode = "gauge+number+delta",
            value = porcentaje_afiliacion,
            domain = {'x': [0, 0.5], 'y': [0, 1]},
            title = {'text': "Avance Afiliación"},
            delta = {'reference': 100},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 70], 'color': "lightgray"},
                    {'range': [70, 90], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        fig.add_trace(go.Indicator(
            mode = "gauge+number+delta",
            value = porcentaje_recaudacion,
            domain = {'x': [0.5, 1], 'y': [0, 1]},
            title = {'text': "Avance Recaudación"},
            delta = {'reference': 100},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 70], 'color': "lightgray"},
                    {'range': [70, 90], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        fig.update_layout(title=f'Avance de Metas - {estado_seleccionado}')
        st.plotly_chart(fig, use_container_width=True)

# FUNCIÓN 5: METAS DE DESEMPEÑO
elif st.session_state.selected_funcion == "Metas Desempeño":
    st.header("🎯 Definición de Metas de Resultados y Desempeño")
    
    st.markdown("""
    **Objetivo:** Colaborar en la definición de metas para unidades administrativas de Órganos Desconcentrados
    """)
    
    # Simulador de establecimiento de metas
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("📐 Configuración de Metas")
        
        tipo_meta = st.radio("Tipo de Meta:", ["Afiliación", "Recaudación", "Eficiencia Operativa"], key="tipo_meta_radio")
        
        if tipo_meta == "Afiliación":
            meta_base = st.number_input("Meta base de afiliación:", 1000, 1000000, 50000, key="meta_afiliacion_input")
            crecimiento_meta = st.slider("Crecimiento esperado (%)", 0, 50, 15, key="crecimiento_afiliacion_slider")
            meta_final = meta_base * (1 + crecimiento_meta/100)
            
        elif tipo_meta == "Recaudación":
            meta_base = st.number_input("Meta base de recaudación (MXN):", 1000000, 100000000, 5000000, key="meta_recaudacion_input")
            crecimiento_meta = st.slider("Crecimiento esperado (%)", 0, 50, 12, key="crecimiento_recaudacion_slider")
            meta_final = meta_base * (1 + crecimiento_meta/100)
            
        else:  # Eficiencia Operativa
            meta_base = st.number_input("Tiempo promedio actual (días):", 1, 30, 10, key="meta_eficiencia_input")
            mejora_meta = st.slider("Reducción esperada (%)", 0, 50, 20, key="mejora_eficiencia_slider")
            meta_final = meta_base * (1 - mejora_meta/100)
        
        # CORREGIDO: st.metric sin parámetro key
        st.metric("Meta Propuesta", f"{meta_final:,.0f}" if tipo_meta != "Eficiencia Operativa" else f"{meta_final:.1f} días")
        
        if st.button("💾 Guardar Configuración de Meta", key="btn_guardar_meta"):
            st.success("✅ Configuración de meta guardada exitosamente")
    
    with col1:
        st.subheader("📊 Simulación de Cumplimiento de Metas")
        
        # Generar datos de simulación
        trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
        cumplimiento = np.random.uniform(0.7, 1.3, size=4) * 100
        
        df_simulacion = pd.DataFrame({
            'Trimestre': trimestres,
            'Cumplimiento (%)': cumplimiento
        })
        
        fig = px.bar(df_simulacion, x='Trimestre', y='Cumplimiento (%)',
                    title='Simulación de Cumplimiento Trimestral',
                    color='Cumplimiento (%)',
                    color_continuous_scale='RdYlGn')
        fig.add_hline(y=100, line_dash="dash", line_color="red", 
                     annotation_text="Meta 100%", annotation_position="bottom right")
        st.plotly_chart(fig, use_container_width=True)
        
        # Análisis de riesgo
        riesgo_bajo_meta = len([x for x in cumplimiento if x < 90])
        # CORREGIDO: st.metric sin parámetro key
        st.metric("Trimestres con riesgo de incumplimiento", riesgo_bajo_meta)

# FUNCIÓN 6: DETECCIÓN DE ANOMALÍAS

# FUNCIÓN 6: DETECCIÓN DE ANOMALÍAS
elif st.session_state.selected_funcion == "Detección Anomalías":
    st.header("🔍 Detección de Esquemas de Comportamiento Atípicos")
    
    st.markdown("""
    **Objetivo:** Identificar esquemas de comportamiento atípicos que impacten al Instituto en materia de afiliación y recaudación
    """)
    
    # Configuración inicial en session_state
    if 'datos_anomalias' not in st.session_state:
        st.session_state.datos_anomalias = None
    if 'metodo_seleccionado' not in st.session_state:
        st.session_state.metodo_seleccionado = "IQR (Recomendado)"
    if 'sensibilidad_actual' not in st.session_state:
        st.session_state.sensibilidad_actual = 3
    
    # Sidebar para configuración
    with st.sidebar:
        st.header("⚙️ Configuración de Detección")
        
        # Selector de método de detección
        metodo = st.selectbox(
            "Método de detección:",
            ["IQR (Recomendado)", "Desviación Estándar", "Percentiles"],
            key="metodo_deteccion_select"
        )
        
        # Ajustar sensibilidad según el método
        if metodo == "Desviación Estándar":
            sensibilidad = st.slider(
                "Número de desviaciones estándar:",
                min_value=1.0,
                max_value=5.0,
                value=3.0,
                step=0.5,
                key="sensibilidad_std"
            )
        elif metodo == "Percentiles":
            col_perc1, col_perc2 = st.columns(2)
            with col_perc1:
                percentil_inf = st.slider("Percentil inferior:", 1, 25, 5, key="percentil_inf")
            with col_perc2:
                percentil_sup = st.slider("Percentil superior:", 75, 99, 95, key="percentil_sup")
        else:  # IQR
            sensibilidad = st.slider(
                "Multiplicador IQR:",
                min_value=1.0,
                max_value=3.0,
                value=1.5,
                step=0.1,
                key="sensibilidad_iqr"
            )
        
        # Selector de tipo de datos
        tipo_datos = st.selectbox(
            "Tipo de datos a analizar:",
            ["Afiliaciones Diarias", "Recaudación Diaria", "Tasa de Crecimiento", "Eficiencia Operativa"],
            key="tipo_datos_select"
        )
        
        # Rango de días a analizar
        num_dias = st.slider(
            "Número de días a analizar:",
            min_value=7,
            max_value=90,
            value=30,
            key="num_dias_slider"
        )
        
        # Botón para generar nuevos datos
        if st.button("🔄 Generar Nuevos Datos Aleatorios", key="btn_nuevos_datos"):
            st.session_state.datos_anomalias = None
            st.rerun()
    
    # Generar o recuperar datos
    if st.session_state.datos_anomalias is None:
        # Generar datos sintéticos con anomalías
        np.random.seed(np.random.randint(1, 1000))  # Semilla aleatoria cada vez
        dias = list(range(1, num_dias + 1))
        
        # Datos base según el tipo seleccionado
        if tipo_datos == "Afiliaciones Diarias":
            base_value = 5000
            std_dev = 500
            anomalia_alta = 15000
            anomalia_baja = 800
        elif tipo_datos == "Recaudación Diaria":
            base_value = 1000000
            std_dev = 100000
            anomalia_alta = 3000000
            anomalia_baja = 200000
        elif tipo_datos == "Tasa de Crecimiento":
            base_value = 2.0
            std_dev = 0.5
            anomalia_alta = 8.0
            anomalia_baja = -3.0
        else:  # Eficiencia Operativa
            base_value = 85.0
            std_dev = 5.0
            anomalia_alta = 98.0
            anomalia_baja = 45.0
        
        # Generar datos normales
        datos = np.random.normal(base_value, std_dev, num_dias)
        
        # Insertar anomalías aleatorias
        num_anomalias = np.random.randint(2, 5)  # Entre 2 y 4 anomalías
        posiciones_anomalias = np.random.choice(range(num_dias), num_anomalias, replace=False)
        
        for i, pos in enumerate(posiciones_anomalias):
            if i % 2 == 0:
                datos[pos] = anomalia_alta * np.random.uniform(0.8, 1.2)  # Anomalía alta
            else:
                datos[pos] = anomalia_baja * np.random.uniform(0.8, 1.2)  # Anomalía baja
        
        st.session_state.datos_anomalias = {
            'dias': dias,
            'datos': datos,
            'tipo_datos': tipo_datos,
            'base_value': base_value
        }
    
    # Recuperar datos
    datos_actuales = st.session_state.datos_anomalias
    dias = datos_actuales['dias']
    datos = datos_actuales['datos']
    tipo_datos = datos_actuales['tipo_datos']
    base_value = datos_actuales['base_value']
    
    df_deteccion = pd.DataFrame({
        'Día': dias,
        'Valor': datos
    })
    
    # Calcular límites según el método seleccionado
    if metodo == "Desviación Estándar":
        media = np.mean(datos)
        std = np.std(datos)
        limite_superior = media + sensibilidad * std
        limite_inferior = media - sensibilidad * std
    elif metodo == "Percentiles":
        limite_inferior = np.percentile(datos, percentil_inf)
        limite_superior = np.percentile(datos, percentil_sup)
    else:  # IQR
        Q1 = np.percentile(datos, 25)
        Q3 = np.percentile(datos, 75)
        IQR = Q3 - Q1
        limite_superior = Q3 + sensibilidad * IQR
        limite_inferior = Q1 - sensibilidad * IQR
    
    # Identificar anomalías
    anomalias = df_deteccion[
        (df_deteccion['Valor'] > limite_superior) | 
        (df_deteccion['Valor'] < limite_inferior)
    ]
    
    # Layout principal
    col_estadisticas, col_visualizacion = st.columns([1, 2])
    
    with col_estadisticas:
        st.subheader("📊 Estadísticas de Detección")
        
        # Métricas clave
        st.metric("Total de Días Analizados", len(df_deteccion))
        st.metric("Anomalías Detectadas", len(anomalias))
        
        tasa_anomalias = (len(anomalias) / len(df_deteccion)) * 100
        st.metric("Tasa de Anomalías", f"{tasa_anomalias:.1f}%")
        
        st.metric("Límite Superior", f"{limite_superior:,.1f}")
        st.metric("Límite Inferior", f"{limite_inferior:,.1f}")
        
        # Análisis de impacto
        if not anomalias.empty:
            impacto_total = anomalias['Valor'].sum() - (base_value * len(anomalias))
            st.metric(
                "Impacto Total", 
                f"{impacto_total:,.0f}",
                delta=f"{impacto_total:+,.0f}"
            )
        
        # Recomendación automática
        st.subheader("💡 Recomendación")
        if len(anomalias) > 4:
            st.error("🚨 **Investigación Urgente**: Múltiples anomalías detectadas")
        elif len(anomalias) > 1:
            st.warning("⚠️ **Monitoreo Reforzado**: Anomalías significativas presentes")
        elif len(anomalias) == 1:
            st.info("🔍 **Investigación Puntual**: Anomalía aislada detectada")
        else:
            st.success("✅ **Comportamiento Normal**: Sin anomalías detectadas")
    
    with col_visualizacion:
        st.subheader(f"📈 Análisis de {tipo_datos}")
        
        # Gráfico principal
        fig = go.Figure()
        
        # Datos normales
        datos_normales = df_deteccion[~df_deteccion.index.isin(anomalias.index)]
        fig.add_trace(go.Scatter(
            x=datos_normales['Día'], 
            y=datos_normales['Valor'],
            mode='lines+markers', 
            name='Comportamiento Normal',
            line=dict(color='blue', width=2),
            marker=dict(size=6)
        ))
        
        # Anomalías
        if not anomalias.empty:
            fig.add_trace(go.Scatter(
                x=anomalias['Día'], 
                y=anomalias['Valor'],
                mode='markers', 
                name='Comportamiento Atípico',
                marker=dict(color='red', size=12, symbol='x', line=dict(width=2))
            ))
        
        # Límites
        fig.add_hline(
            y=limite_superior, 
            line_dash="dash", 
            line_color="orange",
            annotation_text=f"Lím. Sup: {limite_superior:,.0f}", 
            annotation_position="bottom right"
        )
        fig.add_hline(
            y=limite_inferior, 
            line_dash="dash", 
            line_color="orange",
            annotation_text=f"Lím. Inf: {limite_inferior:,.0f}", 
            annotation_position="top right"
        )
        
        # Línea de promedio
        fig.add_hline(
            y=base_value,
            line_dash="dot",
            line_color="green",
            annotation_text=f"Promedio: {base_value:,.0f}",
            annotation_position="top left"
        )
        
        fig.update_layout(
            title=f'Detección de Anomalías - {tipo_datos}',
            xaxis_title='Día',
            yaxis_title=tipo_datos,
            hovermode='closest',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Gráficos adicionales
    col_hist, col_box = st.columns(2)
    
    with col_hist:
        st.subheader("📊 Distribución de Datos")
        fig_hist = px.histogram(
            df_deteccion, 
            x='Valor',
            nbins=20,
            title='Distribución de Frecuencia',
            color_discrete_sequence=['lightblue']
        )
        
        # Añadir líneas de límites
        fig_hist.add_vline(x=limite_superior, line_dash="dash", line_color="red")
        fig_hist.add_vline(x=limite_inferior, line_dash="dash", line_color="red")
        fig_hist.add_vline(x=base_value, line_dash="dot", line_color="green")
        
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col_box:
        st.subheader("📦 Diagrama de Caja")
        fig_box = px.box(
            df_deteccion,
            y='Valor',
            title='Diagrama de Caja - Detección de Outliers',
            points='all'
        )
        
        # Resaltar anomalías
        if not anomalias.empty:
            fig_box.add_trace(go.Scatter(
                x=[0] * len(anomalias),
                y=anomalias['Valor'],
                mode='markers',
                marker=dict(color='red', size=8, symbol='x'),
                name='Anomalías Detectadas'
            ))
        
        st.plotly_chart(fig_box, use_container_width=True)
    
    # Reporte detallado de anomalías
    if not anomalias.empty:
        st.subheader("📋 Reporte Detallado de Anomalías")
        
        # Preparar datos del reporte
        reporte_anomalias = anomalias.copy()
        reporte_anomalias['Desviación'] = reporte_anomalias['Valor'] - base_value
        reporte_anomalias['Desviación %'] = ((reporte_anomalias['Valor'] - base_value) / base_value * 100).round(1)
        reporte_anomalias['Tipo'] = ['Alta' if x > limite_superior else 'Baja' for x in reporte_anomalias['Valor']]
        reporte_anomalias['Severidad'] = reporte_anomalias['Desviación %'].abs().apply(
            lambda x: 'Alta' if x > 100 else 'Media' if x > 50 else 'Baja'
        )
        
        # Mostrar tabla
        st.dataframe(
            reporte_anomalias[['Día', 'Valor', 'Tipo', 'Severidad', 'Desviación', 'Desviación %']],
            use_container_width=True
        )
        
        # Análisis de patrones
        st.subheader("🔍 Análisis de Patrones")
        
        if len(anomalias) >= 3:
            # Calcular frecuencia de anomalías
            dias_entre_anomalias = np.diff(anomalias['Día'])
            frecuencia_promedio = np.mean(dias_entre_anomalias)
            
            col_pat1, col_pat2, col_pat3 = st.columns(3)
            with col_pat1:
                st.metric("Frecuencia Promedio", f"{frecuencia_promedio:.1f} días")
            with col_pat2:
                tipos_anomalias = reporte_anomalias['Tipo'].value_counts()
                mayor_tipo = tipos_anomalias.idxmax()
                st.metric("Tipo Predominante", mayor_tipo)
            with col_pat3:
                severidad_pred = reporte_anomalias['Severidad'].value_counts().idxmax()
                st.metric("Severidad Predominante", severidad_pred)
    else:
        st.success("🎉 No se detectaron anomalías en el período analizado. El comportamiento se encuentra dentro de los parámetros normales.")



# Botón para volver al inicio
st.markdown("---")
if st.button("🏠 Volver al Inicio", key="btn_volver_inicio"):
    st.session_state.selected_funcion = None
    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "**Desarrollado como demostración de capacidades técnicas para el proceso de selección - "
    "Subjefe de División de Política Fiscal**"
)