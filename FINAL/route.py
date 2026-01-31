from flask import render_template, request, redirect, url_for
def route(app):

        @app.route("/")
        def home():
            return render_template("PPrincipal.html")
        
        @app.route("/admin")
        
        def admin():
            param = {}
            return render_template("PPrin_admin.html", param=param)
        @app.route("/lista-pedidos")
        
        def lista_pedidos():
            return render_template("Lista_pedidos.html")
        
        @app.route("/detalle-pedido/<int:id>", methods=['GET', 'POST'])
        def detalle_pedido(id):
            # 1. Simulamos los datos de un pedido para que el HTML tenga qué mostrar
            # En el futuro, aquí buscarás en tu base de datos usando el 'id'
            pedido_ejemplo = {
                "id": id,
                "cliente": "Juan Pérez",
                "fecha": "2023-10-27",
                "total": 5500,
                "estado": "Pendiente",
                "productos": [
                    {"nombre": "Top Ariel", "cantidad": 1, "precio": 25000}
                ]
                
            }
            # 2. Manejo del formulario (cuando presionas "Guardar")

            if request.method == 'POST':
                nuevo_estado = request.form.get('estado')
                print(f"Cambiando el pedido {id} al estado: {nuevo_estado}")
                # Aquí guardarías el cambio en la base de datos
                pedido_ejemplo["estado"] = nuevo_estado 

            return render_template("Detalle_del_Pedido.html", pedido=pedido_ejemplo)
        
        @app.route("/editar-producto/<int:id>", methods=['GET', 'POST'])
        def editar_producto(id):

            
            # 1. Simulamos la búsqueda del producto en la base de datos
            # En un caso real, harías: producto = db.get_producto_by_id(id)
            producto_datos = {
                "id": id,
                "nombre": "Top Ariel",
                "precio": 25000,
                "detalles": "Top de color negro",
                "categoria": "Top",
                "estado": "Stock",
                "color": "n",
                "imagen": "top_ariel.jpg"
            }

            # 2. Si el usuario hace clic en "Editar Producto" (POST)
            if request.method == 'POST':
                # Capturamos los datos del formulario
                nombre = request.form.get('nombre')
                precio = request.form.get('precio')
                detalles = request.form.get('detalles')
                categoria = request.form.get('categoria')
                estado = request.form.get('estado')
                color = request.form.get('color')
                
                # Manejo del archivo (foto)
                foto = request.files.get('archivo')
                if foto and foto.filename != '':
                    print(f"Nueva foto recibida: {foto.filename}")
                    # Aquí guardarías la foto en la carpeta static/img

                # Aquí iría la lógica para actualizar tu Base de Datos
                print(f"Producto {id} actualizado: {nombre}, ${precio}")

                # Después de editar, redirigimos al admin o a la lista
                return redirect(url_for('admin'))

            # 3. Si es GET, mostramos el formulario con los datos actuales
            return render_template("Editar_Prod.html", producto=producto_datos)

        @app.route("/crear-producto", methods=['GET', 'POST'])
        def crear_producto():

            
            if request.method == 'POST':
                # 1. Capturamos los datos de texto del formulario
                nombre = request.form.get('nombre')
                precio = request.form.get('precio')
                detalles = request.form.get('detalles')
                categoria = request.form.get('categoria')
                color = request.form.get('color')
                
                # 2. Capturamos la imagen
                foto = request.files.get('archivo')
                
                # 3. Simulación de guardado (esto lo verás en tu terminal)
                print("--- NUEVO PRODUCTO RECIBIDO ---")
                print(f"Nombre: {nombre}")
                print(f"Precio: {precio}")
                print(f"Categoría: {categoria}")
                print(f"Color: {color}")
                if foto and foto.filename != '':
                    print(f"Imagen: {foto.filename}")
                
                # 4. Redirigimos a la página de administración tras crear
                return redirect(url_for('admin'))

            # Si es GET, simplemente mostramos el formulario
            return render_template("Crear_Prod.html")
        
        @app.route("/login-admin", methods=['GET', 'POST'])
        def login_admin():


            # 1. Si el usuario envía el formulario (POST)
            if request.method == 'POST':
                email = request.form.get('email')
                password = request.form.get('password')

                # Validación de ejemplo
                if email == "admin@coast.com" and password == "1234":
                    print(f"Login exitoso: {email}")
                    # Redirigimos a la lista de pedidos después del éxito
                    return redirect(url_for('lista_pedidos'))
                else:
                    return render_template("Login_Admin.html", error="Credenciales incorrectas")

            # 2. Si entra por primera vez (GET)
            return render_template("Login_Admin.html")
            
        @app.route("/carrito")
        def carrito():
            '''
            Info:
            Carga la página del carrito.
            Por ahora solo renderiza la vista.
            Luego se conectará con controller y model.
            '''
            param = {}
            return render_template("carrito.html", param=param)
        
        
        @app.route("/catalogo")
        def catalogo():
            '''
            Info:
            Carga la página del catalogo.
            Por ahora solo renderiza la vista.
            Luego se conectará con controller y model.
            '''
            param = {}
            return render_template("Catalogo.html", param=param)
        
        @app.route("/detalles")
        def detalles():

            param = {}
            return render_template("detalles.html", param=param)
        
        @app.route("/login")
        def login():
            ''' Info:
            Carga la pagina del login  
            ''' 
            param={}
            return render_template("Login.html", param=param)
        
        @app.route('/signin', methods =["GET", "POST"])
        def signin(): 
            ''' Info: 
            Recepciona la solicitud request que es enviada
            desde el formulario de login 
            retorna la pagina home en caso de exito 
                    o la pagina login en caso de fracaso
            '''
            param={}
            return render_template("Signin.html", param=param)

        @app.route("/miscompras")
        def miscompras():
            ''' Info:
            Carga la pagina de mis comrpas  
            ''' 
            param={}
            return render_template("miscompras.html", param=param)
        
        @app.route("/pago")
        def pago():
            ''' Info:
            Carga la pagina de mis comrpas  
            ''' 
            param={}
            return render_template("pago.html", param=param)