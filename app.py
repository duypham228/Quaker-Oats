from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import pprint as pp
import json
# from models import Earthquake

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text
from flask import request
from werkzeug.utils import redirect

app = Flask(__name__, static_url_path='/static')

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:369491Nghia@localhost:5432/quaker_oats'
db = SQLAlchemy(app)

engine = create_engine('postgresql://postgres:369491Nghia@localhost:5432/quaker_oats')

# engine = db.create_engine('postgresql+psycopg2://postgres:369491Nghia@localhost:5432/postgresql+psycopg2://postgres:369491Nghia@localhost:5432/quaker_oats')
# connection = engine.connect()
class Earthquake(db.Model):
    __tablename__ = 'earthquakes'

    ID = db.Column(db.Integer, primary_key=True)
    Epoch = db.Column(db.Float)
    Time = db.Column(db.String())
    Year = db.Column(db.Integer())
    Mo = db.Column(db.Integer())
    Dy = db.Column(db.Integer())
    Hr = db.Column(db.Integer())
    Mn = db.Column(db.Integer())
    Sec = db.Column(db.Float())
    Tsu = db.Column(db.Integer())
    Vol = db.Column(db.Integer())
    Location_Name = db.Column(db.String())
    Latitude = db.Column(db.Float())
    Longitude = db.Column(db.Float())
    Focal_Depth_km = db.Column(db.Float())
    Mag = db.Column(db.Float())
    MMI_Int = db.Column(db.Float())
    Deaths = db.Column(db.Integer())
    Deaths_Description = db.Column(db.Integer())
    Missing = db.Column(db.Integer())
    Missing_Description = db.Column(db.Integer())
    Injuries = db.Column(db.Integer())
    Injuries_Description = db.Column(db.Integer())
    Damage_MilDollar = db.Column(db.Float())
    Damage_Description = db.Column(db.Integer())
    Houses_Damaged = db.Column(db.Integer())
    Houses_Damaged_Description = db.Column(db.Integer())
    Total_Deaths = db.Column(db.Integer())
    Total_Death_Description = db.Column(db.Integer())
    Total_Missing = db.Column(db.Integer())
    Total_Missing_Description = db.Column(db.Integer())
    Total_Injuries = db.Column(db.Integer())
    Total_Injuries_Description = db.Column(db.Integer())
    Total_Damage_MilDollar = db.Column(db.Float())
    Total_Damage_Description = db.Column(db.Integer())
    Total_Houses_Destroyed = db.Column(db.Integer())
    Total_Houses_Destroyed_Description = db.Column(db.Integer())
    Total_Houses_Damaged = db.Column(db.Integer())
    Total_Houses_Damaged_Description = db.Column(db.Integer())
    Summary_Text = db.Column(db.String())

    def __init__(self, ID ,Epoch ,Time ,Year ,Mo ,Dy, Hr ,Mn ,Sec,Tsu,Vol,Location_Name,Latitude,Longitude,Focal_Depth_km,Mag,MMI_Int,Deaths,Deaths_Description ,Missing ,Missing_Description ,Injuries ,Injuries_Description ,Damage_MilDollar ,Damage_Description, Houses_Destroyed, Houses_Destroyed_Description ,Houses_Damaged ,Houses_Damaged_Description ,Total_Deaths ,Total_Death_Description ,Total_Missing ,Total_Missing_Description ,Total_Injuries ,Total_Injuries_Description ,Total_Damage_MilDollar ,Total_Damage_Description ,Total_Houses_Destroyed ,Total_Houses_Destroyed_Description ,Total_Houses_Damaged,Total_Houses_Damaged_Description, Summary_Text):
        self.ID = ID
        self.Epoch = Epoch
        self.Time = Time
        self.Year = Year
        self.Mo = Mo
        self.Dy = Dy
        self.Hr = Hr
        self.Mn = Mn
        self.Sec = Sec
        self.Tsu = Tsu
        self.Vol = Vol
        self.Location_Name = Location_Name
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Focal_Depth_km = Focal_Depth_km
        self.Mag = Mag
        self.MMI_Int = MMI_Int
        self.Deaths = Deaths
        self.Deaths_Description = Deaths_Description
        self.Missing = Missing
        self.Missing_Description = Missing_Description
        self.Injuries = Injuries
        self.Injuries_Description = Injuries_Description
        self.Damage_MilDollar = Damage_MilDollar
        self.Damage_Description = Damage_Description
        self.Houses_Destroyed = Houses_Destroyed
        self.Houses_Destroyed_Description = Houses_Destroyed_Description
        self.Houses_Damaged = Houses_Damaged
        self.Houses_Damaged_Description = Houses_Damaged_Description
        self.Total_Deaths = Total_Deaths
        self.Total_Death_Description = Total_Death_Description
        self.Total_Missing = Total_Missing
        self.Total_Missing_Description = Total_Missing_Description
        self.Total_Injuries = Total_Injuries
        self.Total_Injuries_Description = Total_Injuries_Description
        self.Total_Damage_MilDollar = Total_Damage_MilDollar
        self.Total_Damage_Description = Total_Damage_Description
        self.Total_Houses_Destroyed = Total_Houses_Destroyed
        self.Total_Houses_Destroyed_Description = Total_Houses_Destroyed_Description
        self.Total_Houses_Damaged = Total_Houses_Damaged
        self.Total_Houses_Damaged_Description = Total_Houses_Damaged_Description
        self.Summary_Text = Summary_Text

    def __repr__(self):
        return [
            self.ID , 
            self.Epoch , 
            self.Time , 
            self.Year , 
            self.Mo ,
            self.Dy , 
            self.Hr , 
            self.Mn , 
            self.Sec , 
            self.Tsu , 
            self.Vol , 
            self.Location_Name , 
            self.Latitude , 
            self.Longitude , 
            self.Focal_Depth_km , 
            self.Mag , 
            self.MMI_Int , 
            self.Deaths , 
            self.Deaths_Description , 
            self.Missing , 
            self.Missing_Description , 
            self.Injuries , 
            self.Injuries_Description , 
            self.Damage_MilDollar , 
            self.Damage_Description , 
            self.Houses_Destroyed,
            self.Houses_Destroyed_Description,
            self.Houses_Damaged , 
            self.Houses_Damaged_Description , 
            self.Total_Deaths , 
            self.Total_Death_Description , 
            self.Total_Missing , 
            self.Total_Missing_Description , 
            self.Total_Injuries , 
            self.Total_Injuries_Description , 
            self.Total_Damage_MilDollar ,
            self.Total_Damage_Description , 
            self.Total_Houses_Destroyed ,
            self.Total_Houses_Destroyed_Description ,
            self.Total_Houses_Damaged,
            self.Total_Houses_Damaged_Description,
            self.Summary_Text
        ]

    
    def serialize(self):
        return {
            'ID': self.ID, 
            'Epoch' : self.Epoch,
            'Time' : self.Time,
            'Year' : self.Year,
            'Mo' : self.Mo,
            'Dy' : self.Dy,
            'Hr' : self.Hr,
            'Mr' : self.Mn,
            'Sec' : self.Sec,
            'Tsu' : self.Tsu,
            'Vol' : self.Vol,
            'Location_Name' : self.Location_Name,
            'Latitude' : self.Latitude,
            'Longitude' : self.Longitude,
            'Focal_Depth_km' : self.Focal_Depth_km,
            'Mag' : self.Mag,
            'MMI_Int' : self.MMI_Int,
            'Deaths' : self.Deaths,
            'Deaths_Description' : self.Deaths_Description,
            'Missing' : self.Missing,
            'Missing_Description' : self.Missing_Description,
            'Injuries' : self.Injuries,
            'Injuries_Description' : self.Injuries_Description,
            'Damage_MilDollar' : self.Damage_MilDollar,
            'Damage_Description' : self.Damage_Description,
            'Houses_Destroyed' : self.Houses_Destroyed,
            'Houses_Destroyed_Description' : self.Houses_Destroyed_Description,
            'Houses_Damaged' : self.Houses_Damaged,
            'Houses_Damaged_Description' : self.Houses_Damaged_Description,
            'Total_Deaths' : self.Total_Deaths,
            'Total_Death_Description' : self.Total_Death_Description,
            'Total_Missing' : self.Total_Missing,
            'Total_Missing_Description' : self.Total_Missing_Description,
            'Total_Injuries' : self.Total_Injuries,
            'Total_Injuries_Description' : self.Total_Injuries_Description,
            'Total_Damage_MilDollar' : self.Total_Damage_MilDollar,
            'Total_Damage_Description' : self.Total_Damage_Description,
            'Total_Houses_Destroyed' : self.Total_Houses_Destroyed,
            'Total_Houses_Destroyed_Description' : self.Total_Houses_Destroyed_Description,
            'Total_Houses_Damaged' : self.Total_Houses_Damaged,
            'Total_Houses_Damaged_Description' : self.Total_Houses_Damaged_Description,
            'Summary_Text' : self.Summary_Text
        }


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/main_vis', methods=['GET'])
def main_vis():
    return render_template('main_vis.html')

@app.route('/general_info', methods=['GET'])
def general_info():
    return render_template('general_info.html')

@app.route('/get_map_data')
def get_map_data():
    session = Session(engine)
    
    year1 = request.args.get('year1', default = 1800, type = int)
    year2 = request.args.get('year2', default = 2021, type = int)
    start_year = min(year1,year2)
    end_year = max(year1, year2)

    mag1 = request.args.get('mag1', default = 0, type = float)
    mag2 = request.args.get('mag2', default = 10, type = float)
    min_magnitude = min(mag1,mag2)
    max_magnitude = max(mag1,mag2)
    tsunami_temp = request.args.get('tsunami', default = False, type = bool)
    tsunami = -1000
    if tsunami_temp:
        tsunami = 0
    volcano_temp = request.args.get('volcano', default = False, type = bool)
    volcano = -1000
    if volcano_temp:
        volcano = 0
    print(start_year, end_year, tsunami_temp)
    location_temp = request.args.get('location', default = '', type = str)
    location = "%"+location_temp.upper()+"%"
    print(location, '------------')
    result = session.query(Earthquake)\
            .where(Earthquake.Year >= start_year)\
            .where(Earthquake.Year <= end_year)\
            .where(Earthquake.Mag >= min_magnitude)\
            .where(Earthquake.Mag <= max_magnitude)\
            .where(Earthquake.Tsu >= tsunami)\
            .where(Earthquake.Vol >= volcano)\
            .filter(Earthquake.Location_Name.like(location))\
            .all()
    output = []
    for row in result:
        temp = row.__dict__
        temp.pop('_sa_instance_state')
        for key in temp:
            if temp[key]==-1000:
                temp[key]=0
        output.append(temp)
    with open('static/json/earthquake_data_small.json', 'w') as f:
        json.dump(output, f)
    return redirect(url_for('main_vis'))

if __name__ == "__main__":
    app.run(debug=True)
