# from werkzeug.datastructures import Headers
from app import db
import csv


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
    Longtitude = db.Column(db.Float())
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
    Total_Houses_Destroyed = db.Column(db.Float())
    Total_Houses_Destroyed_Description = db.Column(db.Integer())
    Total_Houses_Damaged = db.Column(db.Integer())
    Total_Houses_Damaged_Description = db.Column(db.Integer())

    def __init__(self, ID ,Epoch ,Time ,Year ,Mo ,Dy, Hr ,Mn ,Sec,Tsu,Vol,Location_Name,Latitude,Longtitude,Focal_Depth_km,Mag,MMI_Int,Deaths,Deaths_Description ,Missing ,Missing_Description ,Injuries ,Injuries_Description ,Damage_MilDollar ,Damage_Description ,Houses_Damaged ,Houses_Damaged_Description ,Total_Deaths ,Total_Death_Description ,Total_Missing ,Total_Missing_Description ,Total_Injuries ,Total_Injuries_Description ,Total_Damage_MilDollar ,Total_Damage_Description ,Total_Houses_Destroyed ,Total_Houses_Destroyed_Description ,Total_Houses_Damaged,Total_Houses_Damaged_Description):
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
        self.Longtitude = Longtitude
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

    def __repr__(self):
        # return 'ID {}'.format(self.ID)
        return self

    
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
            'Longtitude' : self.Longtitude,
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
            'Total_Houses_Damaged_Description' : self.Total_Houses_Damaged_Description
        }
db.create_all()

# tsv_file = open("static/earthquake_data.tsv")
# read_tsv = csv.reader(tsv_file, delimiter="\t")
# count = 0
# for row in read_tsv:
#     if count > 0:
#         for i in range (4,39):
#             if row[i]=='':
#                 row[i]='-1000'
#         new_data = Earthquake(  row[0],  row[1],  row[2],  row[3],  row[4],
#                                 row[5],  row[6],  row[7],  row[8],  row[9],
#                                 row[10], row[11], row[12], row[13], row[14],
#                                 row[15], row[16], row[17], row[18], row[19],
#                                 row[20], row[21], row[22], row[23], row[24],
#                                 row[25], row[26], row[27], row[28], row[29],
#                                 row[30], row[31], row[32], row[33], row[34], 
#                                 row[35], row[36], row[37], row[38]
#         )
#         db.session.add(new_data)
#         db.session.commit()
#     count +=1
  

