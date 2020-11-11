from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
# #comandos 
#  set FLASK_APP=main.py para poner el proyecto de destinacion
client = MongoClient('localhost', 27017)
db = client["persona"] #bas de datos 
collection = db["Personas"] #tabla <__ en sql seria una tabla

app = Flask(__name__)

@app.route("/")
def Home():
    personas = collection.find({})
    pageModel = {'title': 'Momgodb crud', 'content':"Esto es una prueba", 'data': personas}
    return render_template('index.html', model=pageModel )

#POST GET PUT  DELETE
@app.route("/Persona",methods=['POST'])
def Post_Persona():
    nombre =  data = request.form['nombre']
    appellido =  data = request.form['apellido']
    edad =  data = request.form['edad']
    collection.insert_one({'nombre':nombre,"apellido":appellido,"edad":edad})
    return  redirect("/",302)



if __name__ == "__main__":
    app.run(debug=True)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True


#a mi tambien me salia ese error, no se si quieras leer esto, a ver si tu lo entiendes?