# PDFDuplicator

Una sencilla aplicación en Python para duplicar el contenido de archivos PDF.

## Requisitos

- Python 3.x
- PyPDF2
- tkinter (incluido en la mayoría de instalaciones de Python)

Instala las dependencias con:

```bash
pip install PyPDF2
```

## Uso

1. Ejecuta el script `duplicador.py`:
   ```bash
   python duplicador.py
   ```
2. Selecciona el archivo PDF que deseas duplicar.
3. Indica cuántas veces quieres duplicar el contenido del PDF.
4. El archivo original será reemplazado por uno nuevo con las páginas duplicadas.

## Crear un ejecutable (.exe)

Puedes generar un ejecutable usando [PyInstaller](https://pyinstaller.org/):

1. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Genera el ejecutable:
   ```bash
   pyinstaller --onefile --windowed duplicador.py
   ```
   El ejecutable se creará en la carpeta `dist`.

## Notas

- Solo funciona con archivos PDF.
- El archivo original será sobrescrito.
