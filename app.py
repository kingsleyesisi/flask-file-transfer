from flask import Flask, render_template, request, make_response
from werkzeug.utils import secure_filename
import socket
import os 



app = Flask(__name__)

host = socket.gethostbyname(socket.gethostname())

@app.route('/', methods=['POST', 'GET'])
def login():
    upload_success = False
    if request.method == 'POST':
        upload = request.files['upload']
        upload.save(secure_filename(upload.filename))
        upload_success = True

    return render_template('input.html', upload_success=True)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=2024)