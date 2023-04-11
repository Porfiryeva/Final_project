from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from bfoparser import settings
from bfoparser.spiders.bonalogru import BonalogruSpider

import pickle
from sys import argv

# для теста
# inns = ['3447001553',
#      '12345678',
#      '3447003470',]
#      # '3447003247',
#      # '3447003416',
#      # '3447002444',
#      # '3447000165',
#      # '3447002910',
#      # '5032200629',
#      # '5032186043',
#      # '5032184021',
#      # '5032190642',
#      # '5032194260',
#      # '5032188788',
#      # '5032206081',
#      # '5032197768',
#      # '5032185280']
# пока так криво напрямую
inn_path = r'D:/docs/GB/Финальный проект/parsed_data/inn/inn_0/inn_00.pickle'
with open(inn_path, 'rb') as f:
    inns = pickle.load(f)

if __name__ == '__main__':
    # # чтобы скормить пауку порцию инн
    # inn_path = argv[1]
    # # список строк
    # with open(inn_path, 'rb') as f:
    #     inns = pickle.load(f)

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(BonalogruSpider, inns=inns, year='2021')

    # остановится сам
    process.start()
