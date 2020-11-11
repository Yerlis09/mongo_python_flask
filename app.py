from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
# #comandos 
#  set FLASK_APP=main.py para poner el proyecto de destinacion
client = MongoClient('localhost', 27017)#conexion a la base de datos
db = client["persona"] #base de datos 
collection = db["Personas"] #Coleccion 

app = Flask(__name__)

@app.route("/") #Ruta
def Home():
    personas = collection.find({})
    pageModel = {'title': 'Momgodb crud', 'content':"Esto es una prueba", 'data': personas}
    return render_template('index.html', model=pageModel )

#POST GET PUT  DELETE
@app.route("/Persona",methods=['POST'])
def Post_Persona():
    nombre =  data = request.form['nombre']
    apellido =  data = request.form['apellido']
    edad =  data = request.form['edad']
    email =  data = request.form['email']
    collection.insert_one({'nombre':nombre,"apellido":apellido,"edad":edad, "email":email})
    return  redirect("/",302)



if __name__ == "__main__":
    app.run(debug=True)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True


