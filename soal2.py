import pandas as pd
import numpy as np
from flask_mysqldb import MySQL
import mysql.connector
import base64
import matplotlib.pyplot as plt

mydb=mysql.connector.connect(
    host='localhost',
    user='agammsantos',
    passwd=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8'),
    database='world'
)

x=mydb.cursor()
x.execute('drop view asean;') 
x.execute("create view asean (Negara_Asean,Luas_Daratan,Populasi_Negara,GNP,Ibukota,Populasi_Ibukota) as select country.Name,country.SurfaceArea,country.Population,GNP,city.Name,city.Population from country join city on city.CountryCode=country.Code where Region='Southeast Asia' and city.Name!='Ho Chi Minh City' and city.Name!='Quezon' group by country.Name;")
mydb.commit()

query='select * from asean'
df=pd.read_sql(query,con=mydb)


xvals=range(11)
xnames=df['Negara_Asean']
yvals=df['Populasi_Negara']
plt.figure('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa)')
plt.bar(xvals,yvals,color=np.random.rand(3,))
plt.grid(True)
plt.title('Populasi Negara ASEAN')
plt.xticks(xvals, xnames)
for a,b in zip(xvals, yvals):
    plt.text(a-0.3, b+1000000, str(b))

plt.figure('Persentase Penduduk ASEAN')
plt.pie(yvals,labels=xnames,startangle=-90, 
    autopct='%1.1f%%', textprops={'color':'white'})
plt.legend(xnames)
plt.title('Persentase Penduduk ASEAN')

xvals=range(11)
xnames=df['Negara_Asean']
yvals=df['GNP']
plt.figure('Pendapatan Bruto Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')
plt.bar(xvals,yvals,color=np.random.rand(3,))
plt.grid(True)
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xticks(xvals, xnames)
for a,b in zip(xvals, yvals):
    plt.text(a-0.2, b+2000, str(b))

xvals=range(11)
xnames=df['Negara_Asean']
yvals=df['Luas_Daratan']
plt.figure('Persentase Luas Daratan ASEAN')
plt.pie(yvals,labels=xnames,startangle=-90,
    autopct='%1.1f%%', textprops={'color':'white'})
plt.legend(xnames)
plt.title('Persentase Luas Daratan ASEAN')
plt.show()