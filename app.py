from flask import Flask, render_template

app = Flask(__name__)

Puestos = [
  {
   "id": 1,
    "nombre": "Director de Escena",
    "Lugar de trabajo": "Ensenada, BCS"
  },
  {
   "id": 2,
    "nombre": "Director de Operaciones",
    "Lugar de trabajo": "Tijuana, BC"
  },
  {
   "id": 3,
    "nombre": "Director de Baile",
    "Lugar de trabajo": "Saltillo, Coahulia"
  },
  {
   "id": 4,
    "nombre": "Director de Orquesta",
    "Lugar de trabajo": "Torreon, Coahulia"
  } 
]


@app.route("/")
def hola():
    return render_template('home.html',
                          jobs=Puestos)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  