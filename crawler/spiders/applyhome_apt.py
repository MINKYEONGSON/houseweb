import datetime

import scrapy

from crawler.items import ApplyItem, ApplyHomeTypeItem


class ApplyhomeSpider(scrapy.Spider):
    name = 'applyhome'
    allowed_domains = ['www.applyhome.co.kr']
    start_urls = ['https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do']
    max_parsing_count = 5

    def parse(self, response):
        self.max_parsing_count -= 1
        count = 0
        for row in response.xpath('//table//tbody//tr'):
            item = ApplyItem()
            item['site'] = row.xpath('td[1]//text()').extract_first()
            item['type1'] = row.xpath('td[2]//text()').extract_first()
            item['type2'] = row.xpath('td[3]//text()').extract_first()
            item['name'] = row.xpath('td[4]//text()').extract_first()
            tmp = row.xpath('td[7]//text()').get().split('-')
            item['publish_date'] = datetime.date(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))

            tmp1 = str(row.xpath('td[8]//text()').get()).split(' ~ ')[0].split('-')
            item['start_date'] = datetime.date(year=int(tmp1[0]), month=int(tmp1[1]), day=int(tmp1[2]))

            tmp2 = str(row.xpath('td[8]//text()').get()).split(' ~ ')[1].split('-')
            item['end_date'] = datetime.date(year=int(tmp2[0]), month=int(tmp2[1]), day=int(tmp2[2]))

            if item['end_date'] >= datetime.date.today():
                count += 1
                # yield item

                param1 = row.xpath('@data-pbno').get()
                param2 = row.xpath('@data-hmno').get()
                url = 'https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancDetail.do?' \
                      'houseManageNo=%s&pblancNo=%s&gvPgmId=AIA01M01' % (param1, param2)
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
        tmp = response.xpath('//*[@class="tbl_st tbl_row tbl_col tbl_center"]//tr')[2:]
        for t in tmp:
            type_str = t.xpath('td[1]//text()').get()
            if type_str == '특별공급':
                tmp = t.xpath('td[2]//text()').get().split('-')
                item['vote_tk'] = datetime.date(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))
            elif type_str == '1순위':
                tmp = t.xpath('td[2]//text()').get().split('-')
                item['vote_1'] = datetime.date(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))
            elif type_str == '2순위':
                tmp = t.xpath('td[2]//text()').get().split('-')
                item['vote_2'] = datetime.date(year=int(tmp[0]), month=int(tmp[1]), day=int(tmp[2]))
            else:
                break
        yield item

        for t in response.xpath('//table[2]//tbody//tr'):
            sub_item = ApplyHomeTypeItem()
            sub_item['name'] = t.xpath('td[1]//text()').get()
            sub_item['price'] = int(t.xpath('td[2]//text()').get().replace(',', ''))
            sub_item['apply'] = item['name']
            yield sub_item
