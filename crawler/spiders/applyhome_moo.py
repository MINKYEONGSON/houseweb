import datetime

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils import reactor

from crawler.items import ApplyItem, ApplyHomeTypeItem


class ApplyhomeMooSpider(scrapy.Spider):
    name = 'applyhome_moo'
    allowed_domains = ['www.applyhome.co.kr']
    start_urls = ['https://www.applyhome.co.kr/ai/aia/selectAPTRemndrLttotPblancListView.do']
    max_parsing_count = 1

    def parse(self, response):
        self.max_parsing_count -= 1
        count = 0
        for row in response.xpath('//table//tbody//tr'):
            item = ApplyItem()
            item['name'] = row.xpath('td[1]//text()').extract_first()

            tmp = row.xpath('td[3]//text()').get().split('-')
            item['publish_date'] = datetime.date(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))

            tmp1 = str(row.xpath('td[4]//text()').get()).split(' ~ ')[0].split('-')
            item['start_date'] = datetime.date(year=int(tmp1[0]), month=int(tmp1[1]), day=int(tmp1[2]))
            item['end_date'] = item['start_date']
            item['vote_n'] = item['start_date']

            if item['end_date'] >= datetime.date.today():
                count += 1
                yield item

                param1 = row.xpath('@data-pbno').get()
                param2 = row.xpath('@data-hmno').get()
                url = 'https://www.applyhome.co.kr/ai/aia/selectAPTRemndrLttotPblancDetailView.do?' \
                      'houseManageNo=%s&pblancNo=%s&gvPgmId=AIA03M01' % (param1, param2)
                item['url'] = url
                yield scrapy.Request(url, callback=self.parse_detail, meta={'item': item})

        if count > 0 or self.max_parsing_count > 0:
            page_button = response.xpath('//*[@class="pageview"]//a/@href').getall()
            for i in range(len(page_button)):
                if page_button[i] == 'javasctipt:void(0)':
                    if len(page_button) > i + 1:
                        yield scrapy.Request(
                            url=response.urljoin(page_button[i + 1]),
                            callback=self.parse
                        )

    def parse_detail(self, response):
        item = response.meta.get('item')
        item['address'] = response.xpath('//table[1]//tbody//tr[1]//td[2]//text()').extract_first()
        tmp2 = response.xpath('//table[1]//tbody//tr[2]//td[2]//text()').extract_first()
        item['home_count'] = int(str(tmp2).replace('세대', ''))

        for t in response.xpath('//table[2]//tbody//tr'):
            sub_item = ApplyHomeTypeItem()
            sub_item['name'] = t.xpath('td[1]//text()').get()
            sub_item['price'] = None
            sub_item['apply'] = item['name']
            yield sub_item
