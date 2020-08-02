# @Author:      Rui Dong
# @DateTime:    2020/07/20
# @Description: 导入国家工作日业务功能实现
# @Version:     1.0

import csv
import requests
from lxml import etree
import time
import datetime

class HolidayRequest(object):
    def __init__(self, year):
        self.year = year

        self.dataRes = []
        self.data = []
        self.dataSave = []
        self.dateList = []#  按每周五天计算

        self.parseHTML()
        self.dateRange(self.year)
        self.exportCSV()

    def parseHTML(self):
        """页面解析"""
        url = 'https://wannianrili.51240.com/ajax/'
        s = requests.session()
        headers = {
            'Host': 'wannianrili.51240.com',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://wannianrili.51240.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
        #result = []
        # 生成月份列表
        dateList = [self.year + '-' + '%02d' % i for i in range(1, 13)]
        for year_month in dateList:
            s = requests.session()
            url = 'https://wannianrili.51240.com/ajax/'
            payload = {'q': year_month}
            response = s.get(url, headers=headers, params=payload)
            element = etree.HTML(response.text)
            html = element.xpath('//div[@class="wnrl_riqi"]')
            print('In Working:', year_month)
            for _element in html:
                # 获取节点属性
                item = _element.xpath('./a')[0].attrib
                if 'class' in item:
                    if item['class'] == 'wnrl_riqi_xiu':
                        tag = 0
                    elif item['class'] == 'wnrl_riqi_ban':
                        tag = 1
                    else:
                        pass
                    _span = _element.xpath('.//text()')
                    # 1 -> workingday , 0 -> resting
                    # refresh data
                    self.dataRes.append( {year_month + '-' + _span[0]} )
                    self.dataSave.append( [year_month + '-' + _span[0],tag ] )
                    self.data.append({'Date': year_month + '-' + _span[0] , 'Tag': tag})
        # print(self.dataRes)
        # return result
        self.exportCSV()

    #-----------导出为csv----------#    
    def exportCSV(self):
        """导出CSV"""
        headers = ['Date' , 'Tag']
        # 如果存入乱码，添加 encoding='utf-8-sig'
        with open(self.year + 'Holiday.csv', 'w', newline='')as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows( self.dateList )
            f_csv.writerows(self.data)

    #----------计算计划的工作日表---------#
    import time
 
    #生成出生当年所有日期
    def dateRange(self,year):
    #     时间格式
    
        fmt = '%Y-%m-%d'
        dateStart = str( str(year) + '-01-01' )
        dateEnd = str( str(year) + '-12-31' )

        weekday = datetime.datetime.strptime( dateStart,fmt ).weekday() 
        tag = self.isWorkingDay( weekday )
        self.dateList.append( {'Date': dateStart,'Tag': tag} )

        dateStart = datetime.datetime.strptime( dateStart,fmt )
        dateEnd = datetime.datetime.strptime( dateEnd,fmt )

        while dateStart < dateEnd:
            dateStart += datetime.timedelta( days=+1 )
            weekday = datetime.datetime.strptime( dateStart.strftime(fmt),fmt ).weekday()
            tag = self.isWorkingDay( weekday )
            self.dateList.append( {'Date': dateStart.strftime(fmt),'Tag': tag} )

    #-------判断是否是工作日------#
    def isWorkingDay( self,day ):
        if day == 6 or day == 7:
            return 0
        else:
            return 1
            

if __name__ == '__main__':
    rili = HolidayRequest('2020')