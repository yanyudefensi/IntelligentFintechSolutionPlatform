from scrapy import Field
from scrapy import Item

class AntfinItem(Item):
    title = Field()
    abstract = Field()
    type = Field()
    content = Field()
    url= Field()
    vender= Field()