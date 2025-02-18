from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from Background_remove import remove_background
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    processed_image = None

    if request.method == "POST":
        if "file" not in request.files:
            print("No file part")  # Debugging
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            print("No selected file")  # Debugging
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)

            file.save(input_path)
            print(f"File saved at: {input_path}")  # Debugging

            # Process the image
            remove_background(input_path, output_path)
            print(f"Processed image saved at: {output_path}")  # Debugging

            # Define URLs to be passed to HTML
            uploaded_image = f"/uploads/{filename}"
            processed_image = f"/output/{filename}"
            print(f"Passing to template -> Uploaded: {uploaded_image}, Processed: {processed_image}")  # Debugging

    return render_template("index.html", uploaded_image=uploaded_image, processed_image=processed_image)

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# Route to serve processed images
@app.route('/output/<filename>')
def processed_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)

# Route for downloading processed image
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
