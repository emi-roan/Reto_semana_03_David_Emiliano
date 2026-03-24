# Reto_semana_03_David_Emiliano
# 🚀 Analizador de Ventas Transaccionales (Reto Semana 3)

## 📊 Programación para Ciencia de Datos | IPN - ESCOM
**Estudiante:** David Emiliano Rodríguez Anduiza  
**Institución:** Instituto Politécnico Nacional  
**Semestre:** Febrero - Julio 2026

---

## 📖 1. Resumen del Proyecto
Este sistema de software ha sido desarrollado para abordar la necesidad de procesar grandes volúmenes de transacciones de ventas en una tienda de tecnología. El programa actúa como un **motor de consolidación**, transformando datos desestructurados en un reporte de inteligencia de negocios que jerarquiza los productos según su rentabilidad (Ingreso Total).

---

## 🛠️ 2. Arquitectura y Decisiones de Diseño

### ⚙️ Procesamiento de Flujos (Standard Input)
Se optó por el uso de `sys.stdin` siguiendo la filosofía de diseño de Unix.
* **Justificación:** Esto permite la **escalabilidad**. El programa puede procesar archivos de gigabytes de tamaño mediante redirección de flujo (`<`), funcionando como un nodo en un pipeline de datos sin cargar todo el dataset en la memoria RAM simultáneamente.

### 🧠 Estructura de Datos: Diccionarios (Hash Maps)
La lógica de agrupación se basa en diccionarios de Python.
* **Eficiencia Algorítmica:** La búsqueda y actualización de cada producto se realiza en tiempo constante **O(1)**. 
* **Complejidad Global:** El procesamiento completo tiene una complejidad de **O(n)**, donde *n* es el número de transacciones, lo cual es el estándar óptimo para el análisis de Big Data.

### 🛡️ Robusted y Data Wrangling
El código implementa una capa de limpieza de datos (*Sanitization*):
* **Normalización:** Uso de `.strip()` para eliminar espacios accidentales en nombres de productos.
* **Manejo de Excepciones:** Bloques `try-except` capturan errores de tipo `ValueError` (cuando un precio no es numérico) o `IndexError` (cuando faltan columnas), permitiendo que el flujo continúe sin interrupciones.

---

## 📋 3. Especificaciones del Dataset (entrada.txt)

El archivo de entrada debe ser un CSV con la siguiente estructura semántica:
1. **Fecha:** (YYYY-MM-DD) - Utilizada para registro cronológico.
2. **Producto:** (String) - Identificador único del artículo.
3. **Cantidad:** (Integer) - Unidades vendidas en la transacción.
4. **Precio Unitario:** (Float) - Valor monetario por unidad.

---

## 📈 4. Historial de Desarrollo (Metodología Git)

Se utilizó un flujo de trabajo de **Desarrollo Incremental**, documentado a través de commits con etiquetas semánticas:

| Commit | Fase | Descripción Técnica |
| :--- | :--- | :--- |
| **Commit 1** | `feat` | Estructura base: Configuración del lector de `stdin` y gestión de encabezados. |
| **Commit 2** | `feat` | Motor de Agregación: Implementación de diccionarios para acumulación de métricas. |
| **Commit 3** | `fix` | Formateo y Orden: Algoritmo de ordenamiento descendente (Lambda) y precisión decimal. |
| **Commit 4** | `fix` | Robustez: Inserción de validaciones lógicas y gestión de errores en tiempo de ejecución. |
| **Commit 5** | `docs` | Documentación Técnica: Redacción de especificaciones, arquitectura y manual de uso. |

---

## 🚀 5. Manual de Uso

### Requisitos
* Python 3.x instalado.
* Archivo de datos `entrada.txt` en el mismo directorio.

### Comando de ejecución
```bash
python main.py < entrada.txt