from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)#conexion a la base de datos
db = client["peopledb"] #base de datos 
collection = db["people"] #Coleccion 


@app.route("/") #Ruta
def Home():
    personas = collection.find({})
    pageModel = {'title': 'Mongo CRUD', 'data': personas}
    return render_template('list.html', model=pageModel )

@app.route("/create",methods=['GET'])
def createPerson():
    return render_template('add.html' )    

@app.route("/create",methods=['POST'])
def postCreate():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad  = request.form['edad']
    email = request.form['email']
    collection.insert_one({'nombre':nombre,"apellido":apellido,"edad":edad, "email":email})
    return redirect(url_for('Home'))

@app.route("/remove",methods=['POST'])
def postRemove():
    id = request.form['user_id']    
    collection.delete_many({'email':id})
    return redirect(url_for('Home'))

@app.route("/update",methods=['POST'])
def postUpdate():
    id = request.form['id']
    
    collection.update_one({'_id':    ObjectId(id)}, {'$set': {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
         'edad': request.form['edad'],
         'email': request.form['email']
    }})
    return redirect(url_for('Home'))

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=5000)