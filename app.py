from flask import Flask,render_template,request,redirect
app = Flask(__name__)
from pymongo import MongoClient
from bson.objectid import ObjectId

# #comandos 
#  set FLASK_APP=main.py para poner el proyecto de destinacion
client = MongoClient('localhost', 27017)#conexion a la base de datos
db = client["persona"] #base de datos 
collection = db["Personas"] #Coleccion 




@app.route("/") #Ruta
def Home():
    personas = collection.find({})
    pageModel = {'title': 'Momgodb crud', 'content':"Esto es una prueba", 'data': personas}
    return render_template('index.html', model=pageModel )


#creo que no se pude usar la misma url 
@app.route("/Persona/")
@app.route("/Persona/<id>",methods = ['GET'])
def Get_Update_Persona(id=None):
    try :
        data = collection.find_one({'_id':    ObjectId(id)})

        model = {"data" : data, "id":id}
    
        return render_template('/Person/index.html',model=model)
    except IndexError as e:
        return e

#POST GET PUT  DELETE
@app.route("/CreatePersona",methods=['POST'])
def Post_Persona():
    
    nombre =  data = request.form['nombre']
    apellido =  data = request.form['apellido']
    edad =  data = request.form['edad']
    email =  data = request.form['email']
    collection.insert_one({'nombre':nombre,"apellido":apellido,"edad":edad, "email":email})
    return  redirect("/",302)

@app.route('/DeletePersona/<id>',methods=["DELETE"])
def delete_Persona(id):
    db.delete_one({'_id': ObjectId(id)})
    return redirect({'msg': 'usuario eliminado'})

@app.route('/UpdatePersona/<id>',methods=["POST"])
def Update_Persona(id=None):
   
    collection.update_one({'_id':    ObjectId(id)}, {'$set': {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
         'edad': request.form['edad'],
         'email': request.form['email']


    }})
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
         'edad': request.form['edad'],
         'email': request.form['email']
    }
    model= {"id":id,"ok":True, 'data':data}
    return render_template('/Person/index.html',model=model)





# start the development server using the run() methodif __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000)
    
    #app.config['ENV'] = 'development'
    #app.config['DEBUG'] = True
    #app.config['TESTING'] = True


