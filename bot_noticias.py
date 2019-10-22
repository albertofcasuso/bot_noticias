from newsapi import NewsApiClient
import secret

# Init
newsapi = NewsApiClient(api_key=secret.api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(country='mx')

lista = ""
separador = ' - '
separador_el_universal = ' | '
articulos = top_headlines['articles']
for articulo in articulos:
    if separador_el_universal in articulo['title']:
        titulo = articulo['title'].split(separador_el_universal, 1)[0]
    else:
        titulo = articulo['title'].split(separador, 1)[0]

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
