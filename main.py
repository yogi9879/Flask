from flask import Flask , render_template#, request#,make_response
app = Flask(__name__)

@app.route('/')
def upload_file():
   return "Hello yogesh ggg u gotcha yuhudf22"
'''
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
     # data=database(f)
      dataset=pd.read_csv(f)
      results=MLfun.Model(dataset)
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully' + str(results)
'''
if __name__ == '__main__':
   app.run()
