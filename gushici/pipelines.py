# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class GushiciPipeline:

    def __init__(self):
        self.names_seen = set()
        self.authors_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['title'] in self.names_seen and adapter['author'] in self.authors_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['title'])
            self.authors_seen.add(adapter['author'])
            return item
