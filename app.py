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

def compress_images_in_directory(directory, output_directory, quality=85):
    """
    Compresses all JPG images in the given directory and saves them to the output directory.
    
    Args:
        directory (str): Path to the directory containing images.
        output_directory (str): Path to save the compressed images.
        quality (int): Compression quality (default is 85, adjust as needed).
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            compress_image(image_path, output_path, quality)
            print(f"Compressed {filename} and saved to {output_path}")

if __name__ == "__main__":
    # Set the current directory (where the script is located)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the output directory for compressed images
    output_directory = os.path.join(current_directory, "compressed_images")

    # Adjust quality level for compression as necessary
    quality_level = 85  # Change this to suit your compression needs (1-100)

    # Compress all JPG images in the current directory
    compress_images_in_directory(current_directory, output_directory, quality=quality_level)
