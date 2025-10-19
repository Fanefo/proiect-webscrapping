import scrapy

class EbihoreanulSpider(scrapy.Spider):
    name = "ebihoreanul"
    allowed_domains = ["www.ebihoreanul.ro"]
    def start_requests(self):
        url = getattr(self, 'url', 'https://www.ebihoreanul.ro/')
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # Gaseste toate articolele de pe pagina principala
        for article in response.css('div.article > div.title > a'):
            link = article.css('::attr(href)').get()
            title = "".join(article.css('::text').getall()).strip()
            
            # Pentru fiecare articol, genereaza o noua cerere catre link-ul sau
            # si paseaza datele deja extrase (titlu, link) prin meta
            yield response.follow(link, callback=self.parse_article, meta={'link': link, 'title': title})

    def parse_article(self, response):
        # Extrage datele pasate din metoda parse
        title = response.meta['title']
        link = response.meta['link']
        
        # Extrage textul articolului de pe pagina curenta
        paragraphs = response.css('div.article-content div.text p::text').getall()
        text = "\n".join(paragraphs).strip()
        
        # Produce item-ul final cu toate datele
        yield {
            'title': title,
            'link': link,
            'text': text
        }
