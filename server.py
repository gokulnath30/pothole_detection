from flask import Flask,render_template,jsonify,request
from fileinput import filename
import time

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload",methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':  
        f = request.files['files']
        fpath = 'static/uploads/'+str(time.time())+'.png'
        f.save(fpath)  

    return jsonify(res = "Done")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')