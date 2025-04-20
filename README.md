# PDF to Image Converter

A simple program to convert PDF files into separate images.

## System Requirements

This application requires:

1. **Python 3.6+** - The scripting language used for this tool
2. **pdf2image package** - A Python library for converting PDFs to images
3. **Poppler** - A PDF rendering library used by pdf2image

### Installing Requirements:

#### 1. Install Python:
Download and install Python from [python.org](https://www.python.org/downloads/)

#### 2. Install pdf2image:
```
pip install pdf2image
```

#### 3. Install Poppler:

##### Windows:
1. Download Poppler for Windows from: https://github.com/oschwartz10612/poppler-windows/releases/
2. Extract the ZIP file to a folder on your computer (e.g., `C:\Program Files\poppler`)
3. Add the Poppler bin folder to your PATH environment variable in Windows

##### Linux:
```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils

# Fedora
sudo dnf install poppler-utils

# Arch Linux
sudo pacman -S poppler
```

##### macOS:
```bash
brew install poppler
```

## Usage

1. Place the PDF files you want to convert in the same folder as the script
2. Run the script using:
```
python pdf2img.py
```

The conversion results will be saved in the `output` folder with the following structure:
```
output/
  pdf_filename/
    page-01.png
    page-02.png
    ...
    page-NN.png
```

## Configuration

You can modify the following configuration options in the `pdf2img.py` file:
- `dpi` parameter: Image resolution (default: 300)
- `format` parameter: Output image format (png or jpg)

Example of modifying parameters in the function call:
```python
pdf_to_images(pdf_path, output_dir, dpi=600, format="jpg")
```