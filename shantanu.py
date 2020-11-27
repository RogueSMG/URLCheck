import argparse
import subprocess
from multiprocessing.dummy import Pool as ThreadPool
import requests
# from requests_futures.sessions import FuturesSession





def curlit(url):
	#print('\nCurling...')
	# print(url)
	try:
		resp = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"}, timeout=3)
		print(url + ' : ' + str(resp.status_code))
		if resp.status_code == 200:
			resp2 = requests.get(url+"/zz11")
			# print(url)
			# print('First Request: ' + str(resp2))
			if resp2.status_code != 200:
				# print('Second Request: ' + url + ' : '+ str(resp2.status_code))
				# print('Valid URL: ' + url)
				with open("Live-Domains.txt", 'w') as f1:
					f1.write(url)
			# else:
			# 	with open("Live-Domains.txt", 'w') as f1:
			# 		f1.write(url)
	  
	except requests.exceptions.Timeout as e:
		# print('Except')
		print ('Timeout')
		# print(resp.status_code)


def spawns(urls):
	# global results
	print('\nGathering Source Codes...')
	results = pool.map(curlit, urls)
	pool.close()
	pool.join()



def main():

	with open(inputz, 'r') as fl:
		urls = fl.read().splitlines()

	spawns(urls)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Curl Test')
	parser.add_argument("--file", "-f", dest='input', help='File containing Domains/URLs', required=True)
	parser.add_argument("--threads", "-t", dest='threads', help='Number of Threads', default=2)
	args = parser.parse_args()

	inputz = args.input
	threads = int(args.threads)
	# dom = args.domains

	pool = ThreadPool(threads)
	# print(pool)
	main()