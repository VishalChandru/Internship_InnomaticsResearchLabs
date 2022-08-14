from crypt import methods
import os
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from hashids import Hashids
import secrets
import validators
import subprocess

app = Flask('__name__')

##### SQL Alchemy ####
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])
db = SQLAlchemy(app)
Migrate(app,db)


#### Create Model #####
class UrlShort(db.Model):
    __tablename__ = 'UrlShort'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text)
    url_short = db.Column(db.Text)

    def __init__(self,url,url_short):
        self.url = url
        self.url_short = url_short


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if validators.url(url):
            new_url = UrlShort(url,None)
            db.session.add(new_url)
            db.session.commit()
            a = UrlShort.query.filter_by(url=url).all()
            hashid = hashids.encode(a[-1].id)
            url_short = request.host_url + hashid

            update = UrlShort.query.get_or_404(a[-1].id)
            update.url = url
            update.url_short = url_short
            db.session.commit()
            return render_template('index.html', url = url, url_short = url_short, hashid = hashid)
        else:
            return render_template('Invalid.html')
    return render_template('index.html')

@app.route('/history')
def history():
    disp = UrlShort.query.order_by(UrlShort.id).all()
    return render_template('history.html', disp = disp)

@app.route('/delete')
def delete():
    try:
        dele = UrlShort.query.order_by(UrlShort.id).all()
        for i in dele:
            db.session.delete(i)
            db.session.commit()
    except:
        return render_template('index.html')
    else:
        return render_template('index.html')
    
@app.route('/<short>')
def decode(short):
    code = UrlShort.query.filter(UrlShort.url_short.endswith(short)).all()
    if code:
        for i in code:
            return redirect(i.url)
    else:
        return render_template('Invalid.html')

@app.route('/copy/<hashid>')
def copy(hashid=None):
        code = UrlShort.query.filter(UrlShort.url_short.endswith(hashid)).all()
        subprocess.run("pbcopy", universal_newlines=True, input=code[0].url_short)
        return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)