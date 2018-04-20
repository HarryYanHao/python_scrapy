# -*-coding:utf-8-*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*-coding:utf-8-*-
import sys
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myProject.items import MyprojectItem
import re
from w3lib.html import remove_tags

reload(sys)
sys.setdefaultencoding("utf-8")


class ListSpider(CrawlSpider):
     # 爬虫名称
     name = "myProject"
     # 设置下载延时
     download_delay = 1
     # 允许域名
     allowed_domains = ["www.jj59.com"]
     # 开始URL
     start_urls = [
         "https://www.jj59.com/jjart/422180"
     ]
     # 爬取规则,不带callback表示向该类url递归爬取
     rules = (
         #Rule(SgmlLinkExtractor(allow=(r'https://news.cnblogs.com/n/page/\d',))),
         Rule(SgmlLinkExtractor(allow=(r'www.jj59.com/jjart/\d',)), callback='parse_content'),
     )



     # 解析内容函数
     def parse_content(self, response):
         def go_remove_tag(value):
             # 移除标签
             content = remove_tags(value)
             # 移除空格 换行
             return re.sub(r'[\t\r\n\s]', '', content)
         item = MyprojectItem()

         # 当前URL
         title = response.selector.xpath('//*[contains(@class, "title")]/h1')[0].extract().decode('utf-8')
         #img = response.selector.xpath('//div[@class="picurl"]/img/@src')[0].extract().decode('utf-8')

         content = response.selector.xpath('/html/body/div[2]/div[1]/div[1]/div[4]')[0].extract().decode('utf-8')
         number = response.selector.xpath('//div[@class="info"]/small[@id="dj"]')[0].extract().decode('utf-8')
         author = response.selector.xpath('//div[@class="info"]/a')[0].extract().decode('utf-8')

         #print(content);
         #exit();
         item['title'] = go_remove_tag(title)

         #item['img'] = img
         item['content'] = go_remove_tag(content)

         item['number'] = go_remove_tag(number)
         item['author'] = go_remove_tag(author)


         yield item



