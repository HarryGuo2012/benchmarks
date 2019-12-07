import download
import wash
from multiprocessing.dummy import Pool as ThreadPool

dom = 'bio'

download.set_dom(dom, '0 B', '10000 B')
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

