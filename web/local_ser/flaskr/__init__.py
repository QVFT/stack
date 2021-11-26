import os

import mysql.connector
from flask import Flask, redirect, render_template, request, url_for # pip install this
from flask_sqlalchemy import SQLAlchemy
import pandas as pd # pip install this
import psycopg2 # brew install this
import urllib.parse as up # pip install this

connection = mysql.connector.connect(
                    host='directorQVFT.mysql.pythonanywhere-services.com',
                    db='directorQVFT$farmledger',
                    user='directorQVFT',
                    password='qvft_db!!!'
                    )



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


    @app.route('/input_farm')
    def input_farm():
        return render_template('input_farm.html')

    @app.route("/input_farm", methods=["POST"])
    def add_signup_to_db():
        farm_id = request.form.get('farm_id')
        farm_description = str(request.form.get('farm_description'))
        """Pass data as SQL parameters with mysql."""
        cursor = connection.cursor()
        sql = """INSERT INTO farm (farm_id, farm_description) VALUES (%s, %s) """
        record_tuple = (farm_id, farm_description)
        cursor.execute(sql,record_tuple)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()
        return render_template('index.html')



    return app
