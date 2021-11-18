import os
from flask import Flask, render_template, request # pip install this
import pandas as pd # pip install this
import psycopg2 # brew install this
import git
import urllib.parse as up

from werkzeug.wrappers import Request # pip install this



"""This section is dedicated to connecting and closing connections to our database"""
up.uses_netloc.append("postgres")
url = up.urlparse("postgres://nqmbojat:ShTOpoUpu2MP5my1fBjW-VoFpos0qaxp@queenie.db.elephantsql.com:5432/nqmbojat")
def db_connect():
    con = psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )
    return con

def db_close(con):
    con.close();





def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/forgot')
    def forgot():
        return render_template('forgot-password.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/collections')
    def collections():
        return render_template('collections.html')

    @app.route('/growthzone')
    def growthzone():
        return render_template('growthzone.html')

    @app.route('/nutrientzone')
    def nutrientzone():
        return render_template('nutrientzone.html')

    @app.route('/returnline')
    def returnline():
        return render_template('returnline.html')

    @app.route('/supplyline')
    def supplyline():
        return render_template('supplyline.html')

    @app.route('/livestream')
    def livestream():
        return render_template('livestream.html')

    @app.route('/farms')
    def farm():
        con = db_connect()
            #cursor
        cur = con.cursor()
        #execute query
        cur.execute('SELECT * FROM farm')
        #array of tuples
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns =['id', 'description'])
        #close cursor
        cur.close()
        db_close(con)
        return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

    @app.route('/webhook', methods=['POST'])    
    def webhook():
        if request.method == 'POST':
            print("hook received")
            repo = git.Git('../../')
            repo.pull('origin', 'main')
            return '', 200
        else:
            return '', 400

    @app.route('/input_farm')
    def input_farm():
        return render_template('input_farm.html')

    @app.route('/input_farm',methods=['POST'])
    def readingadd():
        farm_id = request.form.get('farm_id')
        farm_description = request.form.get('farm_description')
        con = db_connect()
            #cursor
        cur = con.cursor()
        #execute query
        cur.execute("INSERT INTO farm (farm_id, description) VALUES (%s, %s)" %(farm_id, farm_description))
        #cur.execute('INSERT INTO farm ('+ farm_id+", "+farm_description+")")
        con.commit()
        cur.close()
        db_close(con)
        return farm_id + " " + farm_description 
    
    return app
