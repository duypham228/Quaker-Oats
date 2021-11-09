# from werkzeug.datastructures import Headers
from app import db
from app import Earthquake
import csv

db.create_all()
tsv_file = open("static/earthquake_data.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
count = 0
for row in read_tsv:
    if count > 0:
        if row[0]=='548':
            print(row, '----------------------------------')
            break
        for i in range (4,39):
            if row[i]=='':
                row[i]='-1000'
        
        new_data = Earthquake(  row[0],  row[1],  row[2],  row[3],  row[4],
                                row[5],  row[6],  row[7],  row[8],  row[9],
                                row[10], row[11], row[12], row[13], row[14],
                                row[15], row[16], row[17], row[18], row[19],
                                row[20], row[21], row[22], row[23], row[24],
                                row[25], row[26], row[27], row[28], row[29],
                                row[30], row[31], row[32], row[33], row[34], 
                                row[35], row[36], row[37], row[38]
        )
        db.session.add(new_data)
        db.session.commit()
    count +=1
  

