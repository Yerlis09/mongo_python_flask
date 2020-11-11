from flask import Flask,render_template,request
from flask.views import MethodView

class Person(MethodView):
    def  get(self):
        return render_template('index.html')
    def post(self):
        return "Test"