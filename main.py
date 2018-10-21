ffrom flask import Flask, render_template, request,make_response
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug import secure_filename
import pandas as pd
import MLfun
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
     # data=database(f)
      dataset=pd.read_csv(f)
      results=MLfun.Model(dataset)
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully' + str(results)


