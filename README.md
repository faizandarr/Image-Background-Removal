# Image-Background-Removal
This Python script removes the background from an image using the Hugging Face transformers library and the 'briaai/RMBG-1.4' model for image segmentation. The output is a transparent PNG image with the background removed.

# Background Removal Script Using Hugging Face Transformers

This Python script removes the background from an image using a pre-trained deep learning model from **Hugging Face (`briaai/RMBG-1.4`)**. The output is a **transparent PNG image** with the background removed.

## Features
✅ Automatically removes the background from an image  
✅ Uses a **state-of-the-art image segmentation model**  
✅ Saves the processed image with a **transparent background**  

##  Installation
Before running the script, install the required dependencies:

```bash
pip install torch torchvision pillow numpy transformers>=4.39.1
