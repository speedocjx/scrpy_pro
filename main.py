from scrapy import cmdline
cmdline.execute("scrapy crawl dmoz -o item.json".split())