import download
import wash
from multiprocessing.dummy import Pool as ThreadPool
import sys

dom = 'bio'
low = '0 B'
up = '100 MB'

argvs = list(sys.argv)
dom = argvs[1]

download.set_dom(dom, low, up)
urls = download.get_download_url_list()

def deal_with_url(url):
    # print('---------------')
    name = download.download_benchmark(url)
    wash.unzip(dom, name)
    wash.deal_file(dom, name)
    wash.remove_tmp(dom, name)

pool = ThreadPool(4)

pool.map(deal_with_url, urls)
pool.close()

