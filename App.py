############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)




# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudionic'
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"




### ----TABLA categorias------###

#### Mostrar todos categorias ####

@cross_origin()
@app.route('/getAllcategoria', methods=['GET'])
def getAllcategoria():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM categorias')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idcategoria': result[0], 'codcategoria': result[1], 'categoria': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

#### Agregar categorias ####
@cross_origin()
@app.route('/add_categoria', methods=['POST'])
def add_categoria():
    if request.method == 'POST':
        codcategoria = request.json['codcategoria']
        categoria = request.json['categoria']  
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO categorias (codcategoria,categoria) VALUES (%s,%s)", (codcategoria,categoria))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


### Actualizar categoria ###
@cross_origin()
@app.route('/updatecategoria/<idcategoria>', methods=['PUT'])
def update_categoria(idcategoria):
    codcategoria = request.json['codcategoria']
    categoria = request.json['categoria']  
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE categorias
        SET codcategoria = %s,
            categoria = %s
        WHERE idcategoria = %s
    """, (codcategoria,categoria,idcategoria))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})

### Eliminar categoria ###
@cross_origin()
@app.route('/deletecategoria/<idcategoria>', methods = ['DELETE'])
def delete_categoria(idcategoria):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM categorias WHERE idcategoria = %s', (idcategoria,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

###*************************************************************************************###

###---Tabla Marcas---###

#### Mostrar todos  marcas ####
@cross_origin()
@app.route('/getAllmarca', methods=['GET'])
def getAllmarca():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM marcas')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idmarca': result[0], 'codmarca': result[1], 'marca': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### Agregar  marcas ####
@cross_origin()
@app.route('/add_marca', methods=['POST'])
def add_marca():
    if request.method == 'POST':
        codmarca = request.json['codmarca']
        marca = request.json['marca']  
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO marcas (codmarca,marca) VALUES (%s,%s)", (codmarca,marca))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


### Actualizar marca ###
@cross_origin()
@app.route('/updatemarca/<idmarca>', methods=['PUT'])
def update_marca(idmarca):
    codmarca = request.json['codmarca']
    marca = request.json['marca']  
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE marcas
        SET codmarca = %s,
            marca = %s
        WHERE idmarca = %s
    """, (codmarca,marca,idmarca))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### Eliminar marca ###
@cross_origin()
@app.route('/deletemarca/<idmarca>', methods = ['DELETE'])
def delete_marca(idmarca):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM marcas WHERE idmarca = %s', (idmarca,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

###*************************************************************************************###

##---Tabla Productos--##

### Mostrar todos productos ###

@cross_origin()
@app.route('/getAllproductos', methods=['GET'])
def getAllproductos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idproductos': result[0], 'codproducto': result[1], 'idcateg': result[2], 'idmrc': result[3], 'descripcion': result[4], 'precio': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)

#### Agregar  productos ####
@cross_origin()
@app.route('/add_producto', methods=['POST'])
def add_producto():
    if request.method == 'POST':
        codproducto = request.json['codproducto']  
        idcateg = request.json['idcateg'] 
        idmrc  = request.json['idmrc']    
        descripcion = request.json['descripcion']
        precio = request.json['precio'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (codproducto,idcateg,idmrc,descripcion,precio) VALUES (%s,%s,%s,%s,%s)", (codproducto,idcateg,idmrc,descripcion,precio))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    
### Actualizar productos ###
@cross_origin()
@app.route('/updateproducto/<idproductos>', methods=['PUT'])
def update_producto(idproductos ):
    codproducto = request.json['codproducto']  
    idcateg = request.json['idcateg'] 
    idmrc  = request.json['idmrc']    
    descripcion = request.json['descripcion']
    precio = request.json['precio'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE prestamos
        SET codproducto  = %s,
            idcateg = %s,
            idmrc = %s,
            descripcion = %s,
            precio = %s
        WHERE idproductos  = %s
    """, (codproducto,idcateg,idmrc,descripcion,precio,idproductos))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})

### Eliminar producto ###
@cross_origin()
@app.route('/deleteproducto/<idproductos>', methods = ['DELETE'])
def delete_producto(idproductos):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE idproductos = %s', (idproductos,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
