from flask import Flask, request, jsonify, url_for, send_file, render_template
from PIL import Image
from io import BytesIO
import os
import pillow_heif
import uuid

app = Flask(__name__)

# 设置上传目录
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['PREFERRED_URL_SCHEME'] = 'https'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith('.heic'):
        return jsonify({"error": "Only HEIC files are supported"}), 400

    try:
        # Read HEIC file using pillow-heif
        heif_file = pillow_heif.read_heif(file.read())
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data
        )

        # Save the converted JPG to a file
        output_filename = f"{uuid.uuid4().hex}.jpg"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)
        image.save(output_path, format="JPEG")

        # Generate a URL for the file
        file_url = url_for('download_file', filename=output_filename, _external=True, _scheme='https')

        return jsonify({"message": "File converted successfully", "url": file_url}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    return send_file(file_path, mimetype='image/jpeg', as_attachment=True)

@app.route('/view/<filename>', methods=['GET'])
def view_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    return send_file(file_path, mimetype='image/jpeg')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, debug=True)
