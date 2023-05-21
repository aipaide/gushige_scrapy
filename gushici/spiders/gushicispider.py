import scrapy
from scrapy.http import Response
from scrapy.http import Request

from gushici.items import GushiciItem


class GushicispiderSpider(scrapy.Spider):
    name = "gushicispider"
    allowed_domains = ["shangshiwen.com"]
    # 分类标签
    index_url = "http://www.shangshiwen.com/"

    def start_requests(self):
        """
        获取首页内容
        """
        yield Request(self.index_url, self.parse_index)

    def parse_index(self, response:Response):
        """

        :type response: Response
        """
        # 获取标签url
        self.tag_urls = response.xpath("//div[@class='indexshicimark yuanjiao']//a/@href").extract()
        print(self.tag_urls)
        for tag_url in self.tag_urls:
            yield Request(response.urljoin(tag_url), self.parse_tags)

    def parse_tags(self, response:Response):
        # 详情处理
        page_urls =response.xpath("//div[@class='yuanjiao shicimark']/ul/li/a[1]/@href").extract()
        for page_url in page_urls:
            yield Request(response.urljoin(page_url), self.parse_detail)

        # 分页处理
        try:
            total_pages = int(response.xpath("//a[contains(text(), '下一页')]/preceding-sibling::a/text()").extract()[-1])
        except Exception:
            return
        for i in range(2, total_pages):
            url_list = response.url.rpartition("/")[-1].split('_')
            url_list[2]=str(i)
            next_url=response.urljoin("_".join(url_list))
            yield Request(next_url, self.parse_tags)

    def parse_detail(self, response:Response):
        # 获取并构造返回信息
        item = GushiciItem()
        item["title"] = response.css(".title.pad").xpath("b/text()").extract_first()
        item["time"]  = response.xpath("//span[contains(text(), '朝代')]/following-sibling::span/text()").extract_first()
        item["author"] = response.xpath("//span[contains(text(), '作者：')]/following-sibling::span/a/text()").extract_first()
        item["themes"] = response.xpath("//span[contains(text(), '类型：')]/following-sibling::span/a/text()").extract()
        item["content"] = "".join("".join(response.xpath("//span[contains(text(), '原文：')]/parent::p/following-sibling::p/text()").extract()).split())

        yield item