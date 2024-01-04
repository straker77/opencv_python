import os  # Add this line to import the os module
import ssl
import cv2
import numpy as np
from flask import Flask, send_file, request , jsonify
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

@app.route('/send_image_1', methods=['GET', 'POST'])
def send_image_1():
    try:
        # Assuming the image file is named 'preexisting_image.jpg'
        image_path = 'cybill.jpg'
        
        # Perform image resizing logic here if needed
        
        # Send the resized image back in the response
        return send_file(image_path, mimetype='image/jpeg')

    except Exception as e:
        return str(e)

@app.route('/send_image_2', methods=['GET', 'POST'])
def send_image_2():
    try:
        # Assuming the image file is named 'preexisting_image.jpg'
        image_path = 'monika.png'
        
        # Perform image resizing logic here if needed
        
        # Send the resized image back in the response
        return send_file(image_path, mimetype='image/png')

    except Exception as e:
        return str(e)



# Ensure the 'uploads' folder exists
uploads_folder = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploads_folder, exist_ok=True)

app.config['UPLOAD_FOLDER'] = uploads_folder   



	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   global uploaded_filename
   if request.method == 'POST':
      f = request.files['file']
      uploaded_filename=secure_filename(f.filename)
     # uploaded_filepath='uploads/hure.png'

      filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
      f.save(filepath)
     # return 'file uploaded successfully'
      return filepath




@app.route('/reload/<timestamp>', methods=['GET', 'POST'])
def reload_file(timestamp):
    global uploaded_filename
    try:
       # f = request.files['file']
        # Assuming the image file is named 'preexisting_image.jpg'
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)
       # image_path = 'marine.jpg'
        # Perform image resizing logic here if needed
        #uploaded_filepath='uploads/hure.png'
        
        # Send the resized image back in the response
        return send_file(image_path, mimetype='image/jpg')

    except Exception as e:
        return str(e)  

@app.route('/upload2/<sessionid>', methods = ['GET', 'POST'])
def upload_file2(sessionid):
   global uploaded_filename
   if request.method == 'POST':
      f = request.files['file']
      uploaded_filename=generate_filename_with_sessionid(f.filename, sessionid)
    
     # uploaded_filepath='uploads/hure.png'

     # filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)
      f.save(filepath)
     # return 'file uploaded successfully'
      return filepath      
                 

@app.route('/convert_to_png/<timestamp>', methods=['GET', 'POST'])
def convert_to_png(timestamp):
    global uploaded_filename
    try:
       
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

            # Perform image resizing logic here if needed

            # Convert to PNG
            png_path = os.path.splitext(image_path)[0] + '.png'
            img = Image.open(image_path)
            img.save(png_path, format='PNG')

            # Send the resized image back in the response
            return send_file(image_path, mimetype='image/png')
           

    except Exception as e:
        return str(e)



@app.route('/convert_to_pdf/<timestamp>', methods=['GET', 'POST'])
def convert_to_pdf(timestamp):
    global uploaded_filename
    try:
       
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

            # Perform image resizing logic here if needed

            # Convert to PNG
            pdf_path = os.path.splitext(image_path)[0] + '.pdf'
            img = Image.open(image_path)
            img.save(pdf_path, format='PDF')

            # Send the resized image back in the response
            return send_file(pdf_path, mimetype='application/pdf')
           

    except Exception as e:
        return str(e)

@app.route('/convert_to_jpg/<timestamp>', methods=['GET', 'POST'])
def convert_to_jpg(timestamp):
    global uploaded_filename
    try:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

        # Perform image resizing logic here if needed

        # Convert to JPG
        jpg_path = os.path.splitext(image_path)[0] + '.jpg'
        img = Image.open(image_path)
        # Convert to RGB mode if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save as JPEG
        img.save(jpg_path, format='JPEG')

        # Check if the file is created and has a non-zero size
        if os.path.exists(jpg_path):
            file_size = os.path.getsize(jpg_path)
            if file_size > 0:
                # Send the resized image back in the response
                return send_file(jpg_path, mimetype='image/jpeg')
            else:
                return f"Error: The resulting JPG file has zero size. File path: {jpg_path}"
        else:
            return "Error: Failed to convert to JPG or the resulting file is not created."

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/convert_to_gif/<timestamp>', methods=['GET', 'POST'])
def convert_to_gif(timestamp):
    global uploaded_filename
    try:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

        # Perform image resizing logic here if needed

        # Convert to JPG
        jpg_path = os.path.splitext(image_path)[0] + '.jpg'
        img = Image.open(image_path)
        # Convert to RGB mode if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save as JPEG
        img.save(jpg_path, format='GIF')

        # Check if the file is created and has a non-zero size
        if os.path.exists(jpg_path):
            file_size = os.path.getsize(jpg_path)
            if file_size > 0:
                # Send the resized image back in the response
                return send_file(jpg_path, mimetype='image/gif')
            else:
                return f"Error: The resulting JPG file has zero size. File path: {jpg_path}"
        else:
            return "Error: Failed to convert to JPG or the resulting file is not created."

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/convert_to_bmp/<timestamp>', methods=['GET', 'POST'])
def convert_to_bmp(timestamp):
    global uploaded_filename
    try:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

        # Convert to BMP
        bmp_path = os.path.splitext(image_path)[0] + '.bmp'
        img = Image.open(image_path)

        # Convert to RGB mode if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

         # Save as BMP with specific settings
        img.save(bmp_path, format='BMP', quality=100, compression=None)

        # Check if the file is created and has a non-zero size
        if os.path.exists(bmp_path):
            file_size = os.path.getsize(bmp_path)
            if file_size > 0:
                # Send the resized image back in the response
                return send_file(bmp_path, mimetype='image/bmp')
            else:
                return f"Error: The resulting BMP file has zero size. File path: {bmp_path}"
        else:
            return "Error: Failed to convert to BMP or the resulting file is not created."

    except Exception as e:
        return f"Error: {str(e)}"      



@app.route('/thermalvision/<timestamp>', methods=['GET', 'POST'])
def thermalvision(timestamp):
    global uploaded_filename
    try:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename)

        # Convert to JPG
        thermal_path = os.path.splitext(image_path)[0] + '_thermal.jpg'
        # Read the input image
        img = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply a color map to the grayscale image (using the 'COLORMAP_JET' for a thermal effect)
        thermal_img = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

        # Save the thermal vision effect image
        cv2.imwrite(thermal_path, thermal_img)


         # Check if the file is created and has a non-zero size
        if os.path.exists(image_path):
            file_size = os.path.getsize(image_path)
            if file_size > 0:
                # Send the resized image back in the response
                return send_file(thermal_path, mimetype='image/jpg')
            else:
                return f"Error: The resulting thermal file has zero size. File path: {thermal_path}"
        else:
            return "Error: Failed to convert to thermal or the resulting file is not created."

    except Exception as e:
        return f"Error: {str(e)}"      


def generate_filename_with_sessionid(filename, sessionid):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]
    
    # Create a new filename with sessionid
    new_filename = f"{secure_filename(filename.replace(file_extension, ''))}_{sessionid}{file_extension}"

    return new_filename


               


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)







		



