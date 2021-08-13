from flask import Flask, flash, request, redirect, url_for, render_template
import requests
import urllib.request
from PIL import Image

app = Flask(__name__)

app.secret_key = "secret key"


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


@app.route('/fish1share', methods=['POST'])
def upload_image1():
    if request.method == 'POST':
        img = request.form['img']
        resource = urllib.request.urlopen(img)
        output = open('./static/uploads/fish1.png', "wb")
        output.write(resource.read())
        output.close()
        original_image = Image.open('./static/uploads/fish1.png')
        roate_image = original_image.rotate(90, expand=1)
        final_image = roate_image.resize(
            (1280, 720)).save('./static/uploads/fish1.png')
        flash('Image successfully uploaded')
        return redirect(url_for('home'))

# -----
# FISH 2 Functions
# -----


@app.route('/fish2')
def fish2():
    fish = "../static/images/fish2.jpg"
    link = "/fish2share"
    return render_template('paint.html', fish=fish, link=link)


@app.route('/fish2share', methods=['POST'])
def upload_image2():
    if request.method == 'POST':
        img = request.form['img']
        resource = urllib.request.urlopen(img)
        output = open('./static/uploads/fish2.png', "wb")
        output.write(resource.read())
        output.close()
        original_image = Image.open('./static/uploads/fish2.png')
        roate_image = original_image.rotate(90, expand=1)
        final_image = roate_image.resize(
            (1280, 720)).save('./static/uploads/fish2.png')
        flash('Image successfully uploaded')
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host='192.168.43.142')
