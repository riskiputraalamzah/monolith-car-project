from peewee import *
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd

app = Flask(__name__)

global appType
appType = 'Monolith'

database = SqliteDatabase('carsweb.db')


class BaseModel(Model):
    class Meta:
        database = database


class TBCars(BaseModel):
    id = AutoField()  # Menambahkan ID sebagai AutoField
    carname = TextField()
    carbrand = TextField()
    carmodel = TextField()
    carprice = TextField()


def create_tables():
    with database:
        database.create_tables([TBCars])


@app.route('/')
def indeks():
    return render_template('index.html', appType=appType)


@app.route('/createcar')
def createcar():
    return render_template('createcar.html', appType=appType)


@app.route('/createcarsave', methods=['GET', 'POST'])
def createcarsave():
    fName = request.form['carName']
    fBrand = request.form['carBrand']
    fModel = request.form['carModel']
    fPrice = request.form['carPrice']

    # simpan di DB
    car_simpan = TBCars.create(
        carname=fName,
        carbrand=fBrand,
        carmodel=fModel,
        carprice=fPrice
    )
    return redirect(url_for('readcar'))


@app.route('/readcar')
def readcar():
    rows = TBCars.select()
    return render_template('readcar.html', rows=rows, appType=appType)


@app.route('/updatecar')
def updatecar():
    return render_template('updatecar.html', appType=appType)


@app.route('/updatecarsave', methods=['POST'])
def updatecarsave():
    car_id = request.form['carId']
    car = TBCars.get_or_none(TBCars.id == car_id)
    if not car:
        return render_template('updatecar.html', appType=appType, error="Car ID does not exist.")

    fName = request.form['carName'] or car.carname
    fBrand = request.form['carBrand'] or car.carbrand
    fModel = request.form['carModel'] or car.carmodel
    fPrice = request.form['carPrice'] or car.carprice

    query = TBCars.update(
        carname=fName,
        carbrand=fBrand,
        carmodel=fModel,
        carprice=fPrice
    ).where(TBCars.id == car_id)
    query.execute()

    return redirect(url_for('readcar'))


@app.route('/deletecar')
def deletecar():
    return render_template('deletecar.html', appType=appType)


@app.route('/deletecarsave', methods=['GET', 'POST'])
def deletecarsave():
    car_id = request.form['carId']
    car = TBCars.get_or_none(TBCars.id == car_id)
    if not car:
        return render_template('deletecar.html', appType=appType, error="Car ID does not exist.")

    car_delete = TBCars.delete().where(TBCars.id == car_id)
    car_delete.execute()
    return redirect(url_for('readcar'))


@app.route('/searchcar')
def searchcar():
    return render_template('searchcar.html', appType=appType)


@app.route('/searchcarsave', methods=['POST'])
def searchcarsave():
    search_query = request.form['searchQuery']
    results = TBCars.select().where(
        (TBCars.carname.contains(search_query)) |
        (TBCars.carbrand.contains(search_query)) |
        (TBCars.carmodel.contains(search_query)) |
        (TBCars.carprice.contains(search_query))
    )
    return render_template('searchcar.html', appType=appType, results=results, search_query=search_query)


@app.route('/help')
def help():
    return "ini halaman Helps"

# Route untuk mengupload file CSV


@app.route('/uploadcsv', methods=['GET', 'POST'])
def uploadcsv():
    if request.method == 'POST':
        file = request.files['csvFile']
        if file and file.filename.endswith('.csv'):
            # Membaca file CSV menggunakan pandas
            df = pd.read_csv(file)

            # Menyimpan setiap baris ke database
            for index, row in df.iterrows():
                # Menggunakan .get() untuk menghindari KeyError
                TBCars.create(
                    carname=row.get('name', None) or "null",
                    carbrand=row.get('brand', None) or "null",
                    carmodel=row.get('model', None) or "null",
                    carprice=row.get('price', None) or "null"
                )
            return redirect(url_for('readcar'))

    return render_template('uploadcsv.html', appType=appType)


if __name__ == '__main__':
    create_tables()
    app.run(
        port=5010,
        host='0.0.0.0',
        debug=True
    )
