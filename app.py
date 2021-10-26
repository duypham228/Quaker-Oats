from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://duy:2281998duy@localhost:5432/quaker_oats'
db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/main_vis', methods=['GET'])
def main_vis():
    return render_template('main_vis.html')

@app.route('/get_map_data')
def get_map_data():
    return "Hello"    


if __name__ == "__main__":
    app.run(debug=True)
