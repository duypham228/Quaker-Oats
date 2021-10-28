from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import pprint as pp

# from models import Earthquake
import models
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text

app = Flask(__name__, static_url_path='/static')

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:369491Nghia@localhost:5432/quaker_oats'
db = SQLAlchemy(app)

engine = create_engine('postgresql://postgres:369491Nghia@localhost:5432/quaker_oats')

# engine = db.create_engine('postgresql+psycopg2://postgres:369491Nghia@localhost:5432/postgresql+psycopg2://postgres:369491Nghia@localhost:5432/quaker_oats')
# connection = engine.connect()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/main_vis', methods=['GET'])
def main_vis():
    return render_template('main_vis.html')

@app.route('/get_map_data')
def get_map_data():
    stmt = select(models.Earthquake) #.where(models.Earthquake.Vol != -1000)
    session = Session(engine)
    # result = session.execute(stmt).all()
    result = session.query(models.Earthquake).where(models.Earthquake.Vol > 1).all()
    print(type(result), '-----------------------------------')
    # print(result)
    #  result = session.execute(text("select * from earthquakes limit 10;"))
    # print(type(stmt), '----------------------------')
    # print(type(result[0]), '----------------------------------')
    
    output = '['
    for row in result:
        temp = row.__dict__
        temp.pop('_sa_instance_state')
        output += pp.pformat(temp)
        output += ','
    output = output[:-1]
    output += ']'
    # return str(result[0].__dict__)
    return output


if __name__ == "__main__":
    app.run(debug=True)