from flask import *  
import os
import imageio
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
from werkzeug.utils import secure_filename
app = Flask(__name__)  

 
@app.route('/')  
def upload():  
    return render_template("Page.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        data = nib.load(f.filename)
        image_data = data.get_fdata()
        print(image_data.shape)
        #plt.imshow(image_data[:,135,:], cmap="gray")
        image_name=r"static/test.png"
        data=image_data[:,135,:]
        data=np.rot90(data, 1)
        imageio.imwrite(image_name, data)
        image = cv2.imread(r"static/test.png", 1)
        bigger = cv2.resize(image, (227, 227))
        #plt.subplot(121)
        #plt.imshow(bigger)
        #plt.show()
        image_name="static/test.png"
        data=bigger
        imageio.imwrite(image_name, data)

        return render_template("success.html", name = f.filename)


  
if __name__ == '__main__':  
    app.run(debug = True)  
