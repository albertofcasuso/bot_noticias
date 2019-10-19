from newsapi import NewsApiClient
import secret

# Init
newsapi = NewsApiClient(api_key=secret.api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(country='mx')

lista = ""
articulos = top_headlines['articles']
for articulo in articulos:
    # print(articulo['description'])
    # print(articulo['urlToImage'])
    lista += """
    <div class="card mb-4">
      <img class="card-img-top" src='"""+articulo['urlToImage']+"""' alt="Card image cap">
      <div class="card-body">
        <h2 class="card-title">"""+articulo['title']+"""</h2>
        <p class="card-text"></p>
        <a href='"""+articulo['url']+"""' class="btn btn-primary">Leer más &rarr;</a>
      </div>
      <div class="card-footer text-muted">
        """+articulo['publishedAt']+"""
      </div>
    </div>
    """
