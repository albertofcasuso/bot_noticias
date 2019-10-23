from newsapi import NewsApiClient
import secret

# Init
newsapi = NewsApiClient(api_key=secret.api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(country='mx')

lista = ""
separadores = [' - ', ' | ']
lista_de_excluidos = ['mediotiempo.com', 'quien.com', 'lasestrellas.tv', 'espn.com.mx']

articulos = top_headlines['articles']

for articulo in articulos:

    # Revisa el titulo del artículo para eliminar los separadores de la fuente y del universal
    for separador in separadores:
        if separador in articulo['title']:
            titulo = articulo['title'].split(separador, 1)[0]

# Revisa si hay un link a imagen y lo captura
    if articulo['urlToImage']:
        url_imagen = articulo['urlToImage']
    else:
        url_imagen = '#'
# Revisa que artículos están en la lista de fuentes excluidas.
    if articulo['source']['name'].lower() in lista_de_excluidos:
        pass
    else:
        # Mete en la variable lista los que no estén excluidos.
        lista += """
        <div class="card mb-4">
          <img class="card-img-top" src='"""+str(articulo['urlToImage'])+"""' alt="Card image cap">
          <div class="card-body">
            <h2 class="card-title">"""+titulo+"""</h2>
            <p class="card-text"></p>
            <a href='"""+str(articulo['url'])+"""' class="btn btn-primary" target="_blank" and rel="noopener noreferrer">Leer más &rarr;</a>
          </div>
          <div class="card-footer text-muted">
            """+str(articulo['source']['name'])+"""
          </div>
        </div>
        """
