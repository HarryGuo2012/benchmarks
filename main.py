import download
import wash
from multiprocessing.dummy import Pool as ThreadPool

dom = 'bio'
low = '0 B'
up = '10000 B'

dom = input('Please enter domain: ')
up = input('Please enter the file upper size: ')
low = input('Please enter the file lower size: ')

download.set_dom(dom, low, up)
urls = download.get_download_url_list()

def deal_with_url(url):
    print('---------------')
    name = download.download_benchmark(url)
    wash.unzip(dom, name)
    wash.deal_file(dom, name)
    wash.remove_tmp(dom, name)

pool = ThreadPool(4)

pool.map(deal_with_url, urls)
pool.close()

