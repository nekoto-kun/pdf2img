import os
import sys
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_dir, dpi=300, format="png"):
    """Convert PDF to images.
    
    Args:
        pdf_path: Path to the PDF file.
        output_dir: Directory to save the images.
        dpi: Resolution of the images.
        format: Image format (png or jpg).
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the PDF file name without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create a subdirectory for the PDF
    pdf_output_dir = os.path.join(output_dir, pdf_name)
    os.makedirs(pdf_output_dir, exist_ok=True)
    
    print(f"Converting {pdf_path} to {format} images...")
    
    try:
        # Convert PDF to images
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            fmt=format,
            thread_count=os.cpu_count() or 4
        )
        
        # Save each page as an image
        for i, image in enumerate(images):
            page_num = i + 1
            output_file = os.path.join(pdf_output_dir, f"page-{page_num:02d}.{format}")
            image.save(output_file)
            print(f"Page {page_num}/{len(images)} saved to {output_file}")
        
        print(f"Successfully converted {pdf_path} to {len(images)} images.")
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the output directory
    output_dir = os.path.join(script_dir, "output")
    
    # Get all PDF files in the script directory
    pdf_files = [f for f in os.listdir(script_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to convert.")
    
    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(script_dir, pdf_file)
        pdf_to_images(pdf_path, output_dir)
    
    print("\nAll PDFs have been processed. Images saved to the output directory.")

if __name__ == "__main__":
    main()