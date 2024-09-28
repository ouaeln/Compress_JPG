import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed

def compress_image(image_path, output_path, quality=85):
    """
    Compress the image at the given path and save it to the output path.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): Quality level for compression (1-100, higher is better quality).
    """
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")  # Ensures compatibility for all JPG formats
            img.save(output_path, "JPEG", optimize=True, quality=quality)
        print(f"Compressed {image_path} and saved to {output_path}")
    except Exception as e:
        print(f"Failed to compress {image_path}: {e}")

def compress_images_in_directory(directory, output_directory, quality=85, max_workers=4):
    """
    Compresses all JPG images in the given directory and saves them to the output directory using multithreading.
    
    Args:
        directory (str): Path to the directory containing images.
        output_directory (str): Path to save the compressed images.
        quality (int): Compression quality (default is 85, adjust as needed).
        max_workers (int): Number of threads to use for parallel processing.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List to store all image paths
    images_to_compress = []
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            images_to_compress.append((image_path, output_path))

    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(compress_image, img_path, out_path, quality) for img_path, out_path in images_to_compress]
        for future in as_completed(futures):
            # This will print once each thread completes
            future.result()

if __name__ == "__main__":
    # Set the current directory (where the script is located)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the output directory for compressed images
    output_directory = os.path.join(current_directory, "compressed_images")

    # Adjust quality level for compression as necessary
    quality_level = 85  # Change this to suit your compression needs (1-100)

    # Number of threads to use for multithreading
    num_workers = 4  # Adjust this based on your system's capabilities

    # Compress all JPG images in the current directory using multithreading
    compress_images_in_directory(current_directory, output_directory, quality=quality_level, max_workers=num_workers)
