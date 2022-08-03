from flask import Flask, render_template,request
import re


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        regex = request.form.get('regexname')
        string = request.form.get('stringname')
        lis = re.findall(regex,string)
        return render_template('index.html',lis = list(enumerate(lis)))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)