import subprocess
import re
import sys
from pathlib import Path


FORMATOS_SOPORTADOS = {".mp4", ".mkv"}


def limpiar_path(path: str) -> str:
    return path.strip().strip("'\"")


def parsear_segundos(tiempo: str) -> float:
    try:
        partes = tiempo.strip().split(":")
        h, m, s = float(partes[0]), float(partes[1]), float(partes[2])
        return h * 3600 + m * 60 + s
    except Exception:
        return 0.0


def barra_progreso(porcentaje: float, ancho: int = 35) -> str:
    lleno = int(ancho * porcentaje / 100)
    barra = "█" * lleno + "░" * (ancho - lleno)
    return f"[{barra}] {porcentaje:5.1f}%"


def pedir_metadatos() -> dict:
    print("\n🏷️  Metadatos del archivo (Enter para omitir):")

    campos = [
        ("title",   "Título"),
        ("artist",  "Artista"),
        ("album",   "Álbum"),
        ("date",    "Año"),
        ("genre",   "Género"),
    ]

    metadatos = {}
    for clave, nombre in campos:
        valor = input(f"   {nombre}: ").strip()
        if valor:
            metadatos[clave] = valor

    return metadatos


def convertir(input_path: str, bitrate: str, metadatos: dict):
    input_file = Path(input_path)

    if not input_file.exists():
        print(f"\n❌ No se encontró el archivo: {input_path}")
        return

    if input_file.suffix.lower() not in FORMATOS_SOPORTADOS:
        formatos = ", ".join(FORMATOS_SOPORTADOS)
        print(f"\n⚠️  Formato no soportado. Usa: {formatos}")
        return

    output_path = input_file.with_suffix(".mp3")

    print(f"\n🎵 Convirtiendo: {input_file.name}")
    print(f"   Calidad: {bitrate}")
    print(f"   Destino: {output_path}\n")

    cmd = [
        "ffmpeg", "-i", str(input_file),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", bitrate,
    ]

    for clave, valor in metadatos.items():
        cmd += ["-metadata", f"{clave}={valor}"]

    cmd += [
        "-y",
        "-progress", "pipe:2",
        "-nostats",
        str(output_path)
    ]

    proceso = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    duracion_total = None
    re_duracion = re.compile(r"Duration:\s*(\d+:\d+:\d+\.\d+)")
    re_tiempo = re.compile(r"out_time=(\d+:\d+:\d+\.\d+)")

    print("   Progreso:")

    for linea in proceso.stderr:
        if duracion_total is None:
            m = re_duracion.search(linea)
            if m:
                duracion_total = parsear_segundos(m.group(1))

        m = re_tiempo.search(linea)
        if m and duracion_total:
            tiempo_actual = parsear_segundos(m.group(1))
            porcentaje = min(tiempo_actual / duracion_total * 100, 100)
            sys.stdout.write(f"\r   {barra_progreso(porcentaje)}")
            sys.stdout.flush()

    proceso.wait()

    if proceso.returncode != 0:
        print(f"\n\n❌ Error durante la conversión.")
    else:
        sys.stdout.write(f"\r   {barra_progreso(100)}\n")
        sys.stdout.flush()
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"\n✅ ¡Listo! Archivo guardado en:")
        print(f"   {output_path}")
        print(f"   Tamaño: {size_mb:.2f} MB")


def main():
    print("=" * 50)
    print("      🎬  Convertidor de Video a MP3")
    print("      Formatos soportados: MP4, MKV")
    print("=" * 50)

    print("\n📂 Ingresa la ruta del archivo (MP4 o MKV):")
    print("   (puedes arrastrar el archivo a la terminal)")
    input_path = input("   > ").strip()
    input_path = limpiar_path(input_path)

    if not input_path:
        print("\n❌ No ingresaste ninguna ruta. Saliendo.")
        return

    print("\n🎚️  Selecciona la calidad de audio:")
    print("   1) 128 kbps  — Tamaño reducido, buena calidad")
    print("   2) 192 kbps  — Calidad estándar (recomendado)")
    print("   3) 320 kbps  — Máxima calidad, archivo más grande")

    opciones = {"1": "128k", "2": "192k", "3": "320k"}

    while True:
        eleccion = input("\n   Opción (1/2/3): ").strip()
        if eleccion in opciones:
            bitrate = opciones[eleccion]
            break
        print("   ⚠️  Opción inválida, elige 1, 2 o 3.")

    metadatos = pedir_metadatos()

    convertir(input_path, bitrate, metadatos)

    print("\n" + "=" * 50)
    otro = input("¿Deseas convertir otro archivo? (s/n): ").strip().lower()
    if otro == "s":
        print()
        main()
    else:
        print("\n👋 ¡Hasta luego!\n")


if __name__ == "__main__":
    main()
