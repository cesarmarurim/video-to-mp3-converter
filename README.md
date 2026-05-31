# 🎬 Convertidor de Video a MP3

Herramienta de línea de comandos en Python para convertir archivos de video (MP4, MKV) a audio MP3, con selección de calidad, barra de progreso en tiempo real y soporte para metadatos personalizados.

---

## ✨ Características

- 🎵 Convierte archivos **MP4** y **MKV** a **MP3**
- 📊 **Barra de progreso** en tiempo real durante la conversión
- 🎚️ Selección de **calidad de audio**: 128, 192 o 320 kbps
- 🏷️ Agrega **metadatos** al MP3: título, artista, álbum, año y género
- 🔁 Permite convertir **múltiples archivos** en la misma sesión
- 🇲🇽 Interfaz completamente en **español**

---

## 📋 Requisitos

- Python 3.7+
- [ffmpeg](https://ffmpeg.org/) instalado en el sistema

### Instalar ffmpeg

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu / Debian:**
```bash
sudo apt install ffmpeg
```

**Windows:**
Descarga el instalador desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) y agrégalo al PATH.

---

## 🚀 Uso

```bash
python3 mp4_to_mp3.py
```

El programa te guiará paso a paso:

1. **Ingresa la ruta** del archivo de video (puedes arrastrarlo a la terminal)
2. **Elige la calidad** de audio
3. **Agrega metadatos** opcionales (título, artista, álbum, año, género)
4. Espera a que la **barra de progreso** llegue al 100%

```
==================================================
      🎬  Convertidor de Video a MP3
      Formatos soportados: MP4, MKV
==================================================

📂 Ingresa la ruta del archivo (MP4 o MKV):
   (puedes arrastrar el archivo a la terminal)
   > /ruta/a/tu/video.mp4

🎚️  Selecciona la calidad de audio:
   1) 128 kbps  — Tamaño reducido, buena calidad
   2) 192 kbps  — Calidad estándar (recomendado)
   3) 320 kbps  — Máxima calidad, archivo más grande

   Opción (1/2/3): 2

🏷️  Metadatos del archivo (Enter para omitir):
   Título: Mi Canción
   Artista: Artista Ejemplo
   Álbum: 
   Año: 2024
   Género: 

   Progreso:
   [███████████████████████████████████] 100.0%

✅ ¡Listo! Archivo guardado en:
   /ruta/a/tu/video.mp3
   Tamaño: 8.42 MB
```

---

## 📁 Estructura del proyecto

```
mp4-to-mp3/
├── mp4_to_mp3.py   # Script principal
└── README.md       # Documentación
```

---

## 🛠️ Tecnologías

- **Python** — lógica del programa e interfaz CLI
- **ffmpeg** — motor de conversión y escritura de metadatos
- **subprocess** — comunicación en tiempo real con ffmpeg para la barra de progreso

---

## 📄 Licencia

MIT License — libre para usar, modificar y distribuir.
