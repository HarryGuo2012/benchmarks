import urllib.request
import re
import os
import sys

dom = ''
file_size_lower = ''
file_size_upper = ''

def getHtml(url):
	if not os.path.isdir('htmls'):
		os.mkdir('htmls')
	
	if os.path.isfile(os.path.join('htmls', dom + '.html')):
		print('Html file already exists, skip catching html')
		f = open(os.path.join('htmls', dom + '.html'), 'r')
		return f.read()
		
	request = urllib.request.Request(url)

	response = urllib.request.urlopen(request)

	html = response.read()

	html = html.decode('utf-8')

	f = open(os.path.join('htmls', dom + '.html'), 'w')
	f.write(html)

	return html

def showDom():
	doms = ['asn', 'bio', 'bn', 'ca', 'chem', 'cit', 'eco', 'econ', 'email', 'graph500', 'heter', 'ia', 'inf', 'labeled', 'massive', 'misc', 'power', 'proximity', 'rand', 'rec', 'road', 'rt', 'sc', 'soc', 'socfb', 'tech', 'web', 'dynamic', 'tscc', 'bhoslib', 'dimacs', 'dimacs10', 'mldata']

	print("Avaliable domains: ")
	print(doms)

def KM2Num(size):

	size = size[0 : -1]

	num = size

	t = size[len(size) - 1]

	if t == 'K' or t == 'M':
		num = num[0 : -1]
	num = num[0 : -1]
	num = int(num)

	if t == 'K':
		num = num * 1000
	if t == 'M':
		num = num * 1000 * 1000
	
	return num

def set_dom(domain, file_lower, file_upper):
	"""set domain
	Args:
		dom: domain name
		file_size_lower: the lower size of file set [0-9] [KM]B
		file_size_upper: the upper size of file set [0-9] [KM]B
	"""
	global dom
	global file_size_lower
	global file_size_upper
	dom = domain
	file_size_lower = file_lower
	file_size_upper = file_upper
	file_size_lower = KM2Num(file_size_lower)
	file_size_upper = KM2Num(file_size_upper)

def get_download_url_list():
	"""get available benchmarks list
	
	Returns:
		benchmark list
	"""

	url = 'http://networkrepository.com/' + dom + '.php'
	dir = dom

	print('download from ' + url + ' to ./' + dir)

	# if os.path.isdir(dir):
	# 	print('directory of ' + dir + ' exists, skip make directory')
	# else:
	# 	print('make directory of ' + dir)
	# 	os.mkdir(dir)
	if not os.path.isdir(dir):
		os.mkdir(dir)
	
	print('Getting Html')
	html = getHtml(url)

	print('Html got, analysis start')
	print(html)

	haha = re.findall('success hrefRow tooltips" data.*?>Download', html, re.S)

	bibi = []

	for benchmark_url in haha:
		name = re.findall('data-url="(.*?)\.php"', benchmark_url)
		name = name[0]

		print(name)

		siz = re.findall('>(\d* [KM]B)', benchmark_url)
		if len(siz) == 0:
			continue
		siz = siz[0]

		siz = KM2Num(siz)

		if not (file_size_lower <= siz and siz <= file_size_upper):
			print(name + ' is not in size, skip')
			continue
		
		if os.path.isfile(os.path.join(dir, name + '.txt')):
			print(name + ' already exists, skip')
			continue
		
		bibi.append(benchmark_url)
	return bibi


def download_benchmark(benchmark_url):	
	"""download benchmark
	Args:
		benchmark from list returned by get_benchmark_list()
	Return:
		return benchmark name

	"""
	name = re.findall('data-url="(.*?)\.php"', benchmark_url)
	name = name[0]

	print('Try to download ' + name)

	downloadUrl = re.findall(' href="(.*?)">Download', benchmark_url)
	downloadUrl = downloadUrl[0]

	LocalPath = os.path.join(dom, name + '.zip')
	try:
		urllib.request.urlretrieve(downloadUrl, LocalPath)
	except urllib.error.HTTPError as e:
		print('HTTP Error: ' + name)
		return '-1'

	print(name + ' download finished')
	return name