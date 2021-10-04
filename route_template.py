from flask import Flask, render_template

app = Flask(__name__)

data_mahasiswa =[
    {'name': 'gamaria mandar',
    'kelas': 'info 1',
    'alamat': 'kampis' },

    {'name': 'abdul',
    'kelas': 'info 2',
    'alamat': 'tidore' },

    {'name': 'dulahu',
    'kelas': 'info 3',
    'alamat': 'oremi' }
]

# route ini mematahkan halamannya
# defaultnya = http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("home.html")

# patahannya = http://127.0.0.1:5000/about
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/data_mahasiswa')
def data_m():
    return render_template('data-mahasiswa.html', data_mahasiswa=data_mahasiswa)

@app.route('/artikel/<info>')
def artikel_info(info):
    return "halaman artikel " + info
     

if __name__ == '__main__':
    app.run(debug=True)
