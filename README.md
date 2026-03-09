Web Scraping de Publicações do X (Twitter) via Nitter

Este projeto automatiza a coleta de publicações de um usuário do X (Twitter) usando Web Scraping em Python, sem precisar de login ou da API. A solução foi construída em cima do Nitter, uma interface alternativa ao Twitter que apresenta o conteúdo de forma mais limpa e fácil de extrair.

O script usa o Selenium para abrir e navegar automaticamente pela página do usuário no Nitter. A partir daí, ele percorre a timeline, identifica cada postagem nos elementos HTML e puxa as informações relevantes de cada uma.

Tecnologias utilizadas: Python, Selenium, WebDriver Manager, Pandas, CSV.

o script extrai: autor do post, texto completo da publicação, data de publicação, número de comentários, reposts e likes, número de visualizações.

Todos os dados coletados são organizados em um DataFrame do Pandas e exportados para um arquivo CSV, pronto para análises.
