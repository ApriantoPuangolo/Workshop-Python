from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

#konfigurasi mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWOR'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db_kontak'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#routing
@app.route('/') #menampilkan data
def halo():
    return render_template('index.html')

@app.route('/tambah')
def tambah():
    return render_template('tambah_kontak.html')
