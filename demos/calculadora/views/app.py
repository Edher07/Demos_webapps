import web

urls = (
    '/', 'Index',
    '/calculadora','Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    

class Calculadora:
    def GET(self):
        numero_1 = 0
        numero_2 = 0
        resultado = 0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero_1 = int(formulario['numero_1'])
        numero_2 = int(formulario['numero_2'])
        operacion = formulario['operacion']

        # TODO: programar la operación sumar
        # TODO: programar la operación restar
        # TODO: programar la operación dividir
        # TODO: programar la operación multiplicar
        # TODO: programar la operación raiz cuadrada al numero_1
        # TODO: programar la operación potencia numero_1 ** numero_2
        # TODO: programar la operación modulo
        # TODO: programar la operación limpiar los valores


        if operacion == 'sumar':
            resultado =  numero_1 + numero_2
        elif operacion == 'restar':
            resultado =  numero_1 - numero_2
         elif operacion == 'dividir':
            resultado =  numero_1 / numero_2
         elif operacion == 'multiplicacion':
            resultado =  numero_1 * numero_2
        elif operacion == 'raiz':
            resultado =  numero_1 ** 0.5 
         elif operacion == 'potencia':
            resultado =  numero_1 ** numero_2
         elif operacion == 'modulo':
            resultado =  numero_1 % numero_2
         elif operacion == 'limpiar':
         
            numero_1 = 0
            numero_2 = 0
            resultado = 0









        print(f"El tipo de dato es: {type(numero_1)}")

        return f"Formulario: {formulario}"
        #return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
    