from transformers import pipeline  # <-- Add this import
from PIL import Image

def remove_background(input_image_path: str, output_image_path: str):
    """Remove the background from an image and save the processed image."""
    
    # Initialize the image segmentation model
    segmentation_model = pipeline(
        "image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True
    )
    
    # Open the input image
    with Image.open(input_image_path) as image:
        # Process the image
        result = segmentation_model(image)
    
    # The result is the mask image directly
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
    print(f"Processed image saved to {output_image_path}")

remove_background("/teamspace/studios/this_studio/5.jpg","/teamspace/studios/this_studio/5_test.jpg")