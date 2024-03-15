<?php 
    require_once "index.php";
?>
<!DOCTYPE html>
<!-- Lenguaje de la pagina en español -->
<html lang="es">
    <head>
        <!-- Codificación de caracteres estandar -->
        <meta charset="UTF-8">
        <!-- Ajustar el viewport y controlar la escala en dispositivos móviles -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Aplicación Móvil</title>
        <!-- Enlaza tu hoja de estilos CSS aquí -->
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <!-- Encabezado de la aplicación -->
        <header>
            <h1>Paint para telefono</h1>
        </header>
        <!-- Contenido principal -->
        <main>
            <!-- Aquí colocarás el contenido específico de tu aplicación -->
            <canvas id="lienzo" width="400" height="400" ></canvas>

            <div id="paleta" ></div>
        </main>

        <!-- Pie de página -->
        <footer>
            <p>&copy; 2024 Pedro J. Aguilar</p>
        </footer>

        <!-- Scripts JavaScript -->
        <!-- Coloca tus scripts al final del cuerpo para mejorar el rendimiento -->
        <script src="script/pintar.js"></script>
    </body>
</html>