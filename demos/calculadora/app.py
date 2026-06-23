import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
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

        numero_1 = int(formulario.numero_1)
        numero_2 = int(formulario.numero_2)
        operacion = formulario.operacion

        try:
            if operacion == 'sumar':
                resultado = numero_1 + numero_2

            elif operacion == 'restar':
                resultado = numero_1 - numero_2

            elif operacion == 'multiplicacion':
                resultado = numero_1 * numero_2

            elif operacion == 'dividir':
                if numero_2 == 0:
                    resultado = "No se puede dividir entre 0"
                else:
                    resultado = numero_1 / numero_2

            elif operacion == 'raiz':
                resultado = numero_1 ** 0.5

            elif operacion == 'potencia':
                resultado = numero_1 ** numero_2

            elif operacion == 'modulo':
                resultado = numero_1 % numero_2

            elif operacion == 'limpiar':
                numero_1 = 0
                numero_2 = 0
                resultado = 0

            else:
                resultado = "Operación no válida"

        except Exception as e:
            resultado = f"Error: {e}"

        return render.calculadora(numero_1, numero_2, resultado)


if __name__ == "__main__":
    app.run()
    