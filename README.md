# Lector QR Web con Backend en Python (Flask)

Este proyecto permite escanear códigos QR desde una interfaz web responsive compatible con dispositivos móviles. El backend está construido con Flask en Python.

---

## 🖥 Requisitos (desde cero en Windows)

### 1. Instalar Python

1. Ir a [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Descargar el instalador para Windows (por ejemplo: "Windows installer (64-bit)")
3. Durante la instalación:
   - Marcar la opción **"Add Python to PATH"**
   - Luego hacer clic en **"Install Now"**

---

### 2. Descargar el proyecto

#### Opción 1: Con Git instalado

```bash
git clone https://github.com/hazaelsintigo/lector_qr.git
cd lector_qr
```

#### Opción 2: Sin Git

1. Ir a [https://github.com/hazaelsintigo/lector_qr](https://github.com/hazaelsintigo/lector_qr)
2. Clic en **"Code" > "Download ZIP"**
3. Extraer el ZIP y abrir la carpeta

---

### 3. Crear un entorno virtual

Desde la carpeta del proyecto, ejecutar:

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
venv\Scripts\activate
```

---

### 4. Instalar dependencias

```bash
pip install flask flask-cors
```

---

### 5. Ejecutar el servidor

```bash
python app.py
```

Luego, abrir un navegador y entrar a:

```
http://localhost:5000/
```

---

## 📱 Características

- Interfaz responsive usando Bootstrap
- Botón para escanear códigos QR con la cámara
- Abre enlaces escaneados en una nueva pestaña automáticamente

---
