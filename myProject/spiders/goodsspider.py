# -*-coding:utf-8-*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*-coding:utf-8-*-
import sys
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myProject.items import GoodsItem
import re
from w3lib.html import remove_tags

reload(sys)
sys.setdefaultencoding("utf-8")


class GoodsSpider(CrawlSpider):
     # 爬虫名称
     name = "goods"
     # 设置下载延时
     download_delay = 1
     # 允许域名
     allowed_domains = ["www.shopin.net"]
     # 开始URL
     start_urls = [
         "http://www.shopin.net"
     ]
     # 爬取规则,不带callback表示向该类url递归爬取
     rules = (
         #Rule(SgmlLinkExtractor(allow=(r'product/\d',)), ),
         Rule(SgmlLinkExtractor(allow=(r'product/\d',)), callback='parse_content',follow=True),
     )



     # 解析内容函数
     def parse_content(self, response):
         def go_remove_tag(value):
             # 移除标签
             content = remove_tags(value)
             # 移除空格 换行
             return re.sub(r'[\t\r\n\s]', '', content)
         item = GoodsItem()

         # 当前URLgetUsers
         if len(response.selector.xpath('//div[@class="right pr "]/h2')) > 0:
            goodsName = response.selector.xpath('//div[@class="right pr "]/h2')[0].extract().decode('utf-8')
         else :
             goodsName = '';
         if len(response.selector.xpath('//div[@class="sub-title"]')) > 0:
            goodsNumber = response.selector.xpath('//div[@class="sub-title"]')[0].extract().decode('utf-8')
         else :
             goodsNumber = '';
         if len(response.selector.xpath('//span[@class="f20"]')) > 0:
            price = response.selector.xpath('//span[@class="f20"]')[0].extract().decode('utf-8')
         else:
             price = 0.00;

         image = response.selector.xpath('//ul[@id="nav_item"]/li[1]/a/img/@src').extract()
         #img = response.selector.xpath('//div[@class="picurl"]/img/@src')[0].extract().decode('utf-8')





         #print(content);
         #exit();
         item['goodsName'] = go_remove_tag(goodsName)
         item['goodsNumber'] = go_remove_tag(goodsNumber)
         item['price'] = go_remove_tag(price)
         item['image'] = image

         #item['img'] = img


         yield item



