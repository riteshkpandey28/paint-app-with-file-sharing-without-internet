from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ----- Home page - displays 2 image ----
@app.route('/')
def home():
    return render_template('home.html')

# -----
# FISH 1 Functions
# -----

@app.route('/fish1')
def fish1():
    fish = "../static/images/fish1.jpg"
    link = "/fish1share"
    return render_template('paint.html', fish=fish, link=link)


@app.route('/fish1share')
def index1():
    link = "/fish1share"
    return render_template('index.html', link=link)


@app.route('/fish1share', methods=['POST'])
def upload_image1():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file.filename = 'fish1.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('Image successfully uploaded')
        return redirect(url_for('home'))
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

# -----
# FISH 2 Functions
# -----

@app.route('/fish2')
def fish2():
    fish = "../static/images/fish2.jpeg"
    link = "/fish2share"
    return render_template('paint.html', fish=fish, link=link)


@app.route('/fish2share')
def index2():
    link = "/fish2share"
    return render_template('index.html', link=link)


@app.route('/fish2share', methods=['POST'])
def upload_image2():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file.filename = 'fish2.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('Image successfully uploaded')
        return redirect(url_for('home'))
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True, host='192.168.43.142')
