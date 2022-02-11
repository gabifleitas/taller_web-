from flask import Flask, escape, request, render_template, url_for  #Importamos la libreria Flask: para crear la pagina, 


app = Flask(__name__) #Inicializamos la app con el nombre

@app.route('/') #Definimos que en la ruta de inicio sera aplicada la funcion hola
def hola():
    return 'Hi Penguins!'

@app.route('/coach') #para que funcione en chrome, hay que poner /coach. Se crea la ruta coach
def hola_coaches(): #Definir la funcion que sera devuelta
    nombre = 'Gabi' #se inicializa un dato
    devolver = request.args.get('nombre', nombre) #cuando la pagina pide el "nombre", lo que se devuelve es la variable nombre (Enri)
    #Se define que sera devuelto y se renderiza
    return f'Hola, {escape(devolver)}' #retornamos al html

@app.route('/inicio') #creamos la ruta de inicio
def inicio():
    return render_template('inicio.html') #renderizar nuestra pagina html

@app.route('/contacto') #creamos la ruta de contacto
def contacto():
    return render_template('contacto.html')

app.run(debug=True) #para ejecutar, luego escribir en la terminal: "py .\app.py"

