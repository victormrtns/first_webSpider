#Import frameworks
import scrapy
#Create a class and use as a parameter "scrapy.Spider", to the pycharm knows that QuotesSpider is a Spider

class QuotesSpider(scrapy.Spider):
    #A name to identify this class
    name = "quotes"
    #Define a list of urls that i wanna scrape
    start_urls =["http://quotes.toscrape.com/page/1/"]
    #Define a method of this class
    # Response is the response.css/ the HTML of the page
    def parse(self,response):
        for quote in response.css('div.quote'):
            #To generate many dictionaries containing the data extracted from the page
            yield {
                'author':quote.css('small.author::text').get(),
                'text':quote.css('span.text::text').get(),
                'tags':quote.css('div.tags a.tag::text').getall()
            }
        #Pickup the next page
        next = response.css('li.next a::attr(href)').get()
        #If the next page tag exists, do:
        if next is not None:
            #follow has to go to the next page and call the same function
            yield response.follow(next, callback=self.parse)



