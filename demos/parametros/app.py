import web

urls = (
    '/', 'Index',
    '/parametros','Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Parametros:
    def GET(self):
        titulo = "Página con parámetros"
        descripcion = """
                Lorem ipsum dolor sit amet consectetur adipiscing elit, aenean semper quis laoreet tellus quisque fames justo, nec imperdiet phasellus per donec vitae. Condimentum diam commodo luctus dictum pharetra ut et praesent vulputate augue himenaeos interdum purus, id convallis felis porttitor senectus etiam fermentum volutpat quam natoque nulla dui. Potenti facilisis in proin mauris cras dui diam eu vestibulum, nam hac suspendisse mus vivamus sed augue ante, tellus habitant per enim fermentum congue ultricies mollis.
                Commodo auctor venenatis nec per cum quam diam, sapien hendrerit tellus posuere vehicula magnis cursus facilisi, luctus curae a accumsan ultrices eros. Volutpat aliquam euismod sollicitudin quisque torquent blandit nullam orci montes, convallis mi habitant vitae varius pellentesque viverra himenaeos, natoque malesuada sem scelerisque vulputate metus augue fames facilisi, dapibus curae eget morbi tempus ac praesent. Taciti mattis nullam nec vel tincidunt nunc dictum rutrum pretium fames, orci et volutpat magnis suspendisse dis elementum at risus, parturient vitae cursus posuere ut massa sapien ridiculus montes.
                """
        return render.parametros(titulo,descripcion)

if __name__ == "__main__":
    app.run()
    