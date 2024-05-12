import os
from flask import jsonify

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# check_file_in_request
# This function checks if a file is included in the request.
# If the file is not included, it returns an error message.
# 
# Parameters:
# request: The HTTP request to check.
# 
# return: An error message if the file is not included in the request, or None if the file is included.
def check_file_in_request(request):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    return None


# check_file_name
# This function checks if a file has a name.
# If the file does not have a name, it returns an error message.
# 
# Parameters:
# file: The file to check.
# 
# return: An error message if the file does not have a name, or None if the file has a name.
def check_file_name(file):
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    return None

# save_file
# This function saves a file in the 'uploads' directory.
# It first gets the filename of the file.
# It then creates a file path by joining the 'uploads' directory and the filename.
# It then saves the file at the file path.
# 
# Parameters:
# file: The file to save.
# 
# return: The path to the saved file.
def save_file(file):
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    return file_path

# upload_file
# This function handles the file upload process.
# It first checks if the file is included in the request.
# If the file is not included, it returns an error.
# It then checks if the file has a name.
# If the file does not have a name, it returns an error.
# It then saves the file in the 'uploads' directory and returns the file path.
# 
# Parameters:
# request: The HTTP request containing the file.
# 
# return: The path to the uploaded file, or an error message if the file is not included in the request or does not have a name.
def upload_file(request):
    error = check_file_in_request(request)
    if error:
        return error

    file = request.files['file']
    error = check_file_name(file)
    if error:
        return error

    file_path = save_file(file)
    return file_path