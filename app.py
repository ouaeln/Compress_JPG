import os
from PIL import Image

def compress_image(image_path, output_path, quality=85):
    """
    Compress the image at the given path and save it to the output path.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): Quality level for compression (1-100, higher is better quality).
    """
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensures compatibility for all JPG formats
        img.save(output_path, "JPEG", optimize=True, quality=quality)

def compress_images_in_directory(directory, quality=85):
    """
    Compresses all JPG images in the given directory.
    
    Args:
        directory (str): Path to the directory containing images.
        quality (int): Compression quality (default is 85, adjust as needed).
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"compressed_{filename}")
            compress_image(image_path, output_path, quality)
            print(f"Compressed {filename} to {output_path}")

if __name__ == "__main__":
    # Set the current directory (where the script is located)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Adjust quality level for compression as necessary
    quality_level = 85  # Change this to suit your compression needs (1-100)

    # Compress all JPG images in the current directory
    compress_images_in_directory(current_directory, quality=quality_level)
