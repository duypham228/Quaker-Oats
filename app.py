from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://duy:2281998duy@localhost:5432/quaker_oats'
db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/main_vis', methods=['GET', 'POST'])
def main_vis():
    if request.method == 'POST':
      startYear = request.form['startYear']
      endYear = request.form['endYear']
      print(startYear, endYear)
      return redirect(url_for("main_vis"))
    else:
        return render_template('main_vis.html')

@app.route('/general_info', methods=['GET'])
def general_info():
    return render_template('general_info.html')

@app.route('/get_map_data')
def get_map_data():
    return "Hello"    


if __name__ == "__main__":
    app.run(debug=True)
