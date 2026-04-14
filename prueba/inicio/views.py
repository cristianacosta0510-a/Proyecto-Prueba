from django.shortcuts import render,HttpResponse

# Create your views here.
menu=""""
    <a href="/">Home</a>
    <a href="/formulario">Registrar</a>
    <a href="/contacto">Contactanos</a>
    """
def principal(resquest):
    contenido="<h1>HOLA DJANGO</h1>"
    return HttpResponse(menu+contenido)

def contacto(request):
    contenido="""<h2>Contacto</h2>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Mensaje:</p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="Enviar"/></p>"""
    return HttpResponse(contenido)

def nombre(request):
    contenido="<h1>Sebastian Zamudio Martinez</h1>"
    return HttpResponse(contenido)

def formulario(request):
    contenido="""<h2> Registrar </h2>
    <p>Matricula: <input type="text" name="matricula"></p>
    <p>Nombre: <input type="text" name="nombre"></p>
    <p>Carrera:
        <select name="carrera">
            <option>ING. DGS</option>
            <option>ING. EVND</option>
        </select>
    </p>
    <input type="radio" name="turno" value="matutino">Matutino
    <input type="radio" name="turno" value="vespertino">Vespertino
    <p><input type="Button" name="enviar" value="Enviar"></p>
    """
    return HttpResponse(contenido)
