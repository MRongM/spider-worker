from scrapy.spiders import Spider


class DYSpider(Spider):
    name = 'dy'
    start_urls = ['https://www.douyin.com/?']

    def parse(self, response):
        titles = response.xpath('//span/text()').extract()
        for title in titles:
            print(title.strip())