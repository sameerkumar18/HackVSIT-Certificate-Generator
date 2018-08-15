from PIL import Image,ImageFont,ImageDraw
from flask import Flask,request,render_template,session,abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.contrib.fixers import ProxyFix
from uploader import s3_upload
import os,uuid

app = Flask(__name__)
app.secret_key = '5ji*cmvb!_06h3t=+i02*-_6zdho56@^-i38f*ns0dr)-2-'

app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
limiter = Limiter(app, key_func=get_remote_address)

def makeCerti(name,college_name):
    image = Image.open('hack-certi.png')
    name_font_type = ImageFont.truetype('Myriad Pro Bold Condensed.ttf',35)
    college_font_type = ImageFont.truetype('Myriad Pro Bold Condensed.ttf',32)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(1070,550),text=name,fill="#3f889e",font=name_font_type)
    draw.text(xy=(800,590),text=college_name,fill="#3f889e",font=college_font_type)
    image.show()
    image.save(name+'.jpg')
    url = s3_upload(name+".jpg")
    os.remove(name+".jpg")
    return url


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        print(token)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token


@limiter.limit("3/minute")
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        college_name = request.form.get('college_name')
        return render_template("image.html",contents=makeCerti(name,college_name))

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=False, threaded=True)
