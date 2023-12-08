from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'rangga', 'umur':'16thn'}

 komentar = [

  {

   'penulis': {'nama': 'jaja'},

   'ucapan': 'hai rangga, artikel yang menarik'

  },

  {

   'penulis': {'nama': 'riaa'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)