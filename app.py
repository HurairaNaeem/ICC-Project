from flask import Flask, render_template
from PIL import Image, ImageTk
import numpy as np
import cv2
import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def interface():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

@app.route("/onClick1", methods=['GET'])
def onClick1():
    fin = "C:/Users/dell/Desktop/other/coins.png"
    img = Image.open(fin)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
    return render_template('index.html', img=img_str)

@app.route("/onClick2", methods=['GET'])
def onClick2():
    fin = "./coins.png"
    img = Image.open(fin)
    img = np.array(img)
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    (thresh, binary) = cv2.threshold(gray, 102, 255, cv2.THRESH_BINARY)
    n_components, label, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    for i in range(1,len(stats)):
        img = cv2.rectangle(img, (stats[i][0], stats[i][1]), (stats[i][0] + stats[i][2], stats[i][1] + stats[i][3]), (0, 255, 0), 1)
        img = cv2.circle(img, (int(centroids[i][0]), int(centroids[i][1])), 3, (255, 0, 0), -1)
    i = Image.fromarray(img)
    buffered = BytesIO()
    i.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
    return render_template('index.html', img=img_str)

@app.route("/onClick3", methods=['GET'])
def onClick3():
    fin = "C:/Users/dell/Desktop/other/coins.png"
    img = Image.open(fin)
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    (thresh, binary) = cv2.threshold(gray, 102, 255, cv2.THRESH_BINARY)
    n_components, label, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    img = cv2.cvtColor(binary, cv2.COLOR_GRAY2RGB)
    for i in range(1,len(stats)):
        img = cv2.rectangle(img, (stats[i][0], stats[i][1]), (stats[i][0] + stats[i][2], stats[i][1] + stats[i][3]), (255, 0, 0), 2)
        if i < len(stats) and not i == 5:
            img = cv2.line(img, (int(centroids[5][0]), int(centroids[5][1])), (int(centroids[i][0]), int(centroids[i][1])), (0, 0, 255), 1)
    i = Image.fromarray(img)
    buffered = BytesIO()
    i.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
    return render_template('index.html', img=img_str)