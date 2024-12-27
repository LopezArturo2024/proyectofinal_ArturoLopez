Descripcion del programa: 
--> globastore corresponde a un nombre ficticio de una tienda retaile online que vende productos en distintas categorias. Se crearon modelos para "Clientes", "Empleados", 
"Productos","Ventas" e "Inventario". De esta forma, se puede obtener una idea del concepto de la empresa. 

Tecnologias utilizadas:
--> Viscual Studio Code donde se realizó la programacion en Python de la página Web. Creacionistas de modelos, vistas y templates segun la forma de programación MVT.
--> Lenguaje Python
--> Framework Django
--> Archivos .css, .js y .html para el esqueleto y estilo de la págia web. 
--> ChatGPT como ayuda a consultas y mejoras estéticas de la web, así como aspectos técnicos para mejorar el programa. 
--> Git y GitHub para trabajar con versiones del programa y subir el repositorio. 

Uso recomendado del programa: 
--> 1. Primero se debe crear una nueva carpeta en Visual Studio Code (VSC) e iniciar una version con Git. Se debe usar el comando en la terminal: "git init"

--> 2. Después se debe agregar el origen para realizar la extraccion del repositorio de GitHub. Para esto se utiliza el siguiente comando en la terminal: "git remote add origin https://github.com/LopezArturo2024/Tercera-pre-entrega_ArturoLopez.git"

--> 3. Se realiza el siguiente comando en la terminal para traer el repositorio a nuestra carpeta en VSC: "git pull original master"

--> 4. En VSC se deben haber creado dos carpetas llamadas "globalstore" (Proyecto) y "info_app" (aplicación), la base de datos de SQlite, el archivo manage.py y este archivo README.md. 

--> 5. En la terminal colocamos el siguiente comando: "python manage.py migrate" y debería aparecernos la aplicación en la seccion de "Operations to perform".

--> 6. Damos inicio a nuestro servidor con el comando "python manage.py runserver" y accedemos a la URL que se genera. 

--> 7. En la página vamos a acceder a la siguiente URL: Localhost/info_app/portada/ y nos va a dirigir a la página principal del proyecto. Nota: No se porque la primera vez no aparece el listado de las URL, pero si se pueden acceder a ellas. 

--> 8. Se recomienda para el uso y lógica de la página web que primero se agreguen los empleados, despues los productos de la tienda y por último el inventario. Después se agreguen los clientes y por último se registren las ordenes de venta. Nota: No existe lógica o relación entre las tablas y entidades y por eso se señala la lógica de como debería utilizarse.

--> 9. Juegue jaja!
