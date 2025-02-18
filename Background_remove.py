from transformers import pipeline
from PIL import Image

# Load the AI model for background removal
segmentation_model = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)

def remove_background(input_image_path: str, output_image_path: str):
    """Remove the background from an image and save the processed image."""
    
    # Open the input image
    with Image.open(input_image_path) as image:
        # Process the image
        result = segmentation_model(image)

    # Check if result is an Image
    if isinstance(result, Image.Image):
        mask = result
    else:
        raise ValueError("Unexpected result format from the segmentation model")

    # Ensure the mask is in the same size as the original image
    mask = mask.resize(image.size, Image.LANCZOS)
    
    # Convert mask to RGBA
    mask = mask.convert("RGBA")

    # Create a new image with transparent background
    output_image = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Paste the original image using the mask
    output_image.paste(image, (0, 0), mask)

    # Save the processed image
    output_image.save(output_image_path, format="PNG")
