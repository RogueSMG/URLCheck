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
		# print(resp.headers)
		if resp.status_code == 200:
			resp2 = requests.get(url+"/zz11")
			
			# print(resp.headers.keys())
			if 'content-length' in resp.headers.keys():
				preLength = resp.headers['Content-Length']
				print('[H]Basic URL Check: ' + url + '\nContent-Length: ' + preLength + '\n')
			
			else:
				preLength = str(len(resp.content))
				print('Basic URL Check: ' + url + '\nContent-Length: ' + str(len(resp.content)) + '\n')	

				if resp2.status_code != 200:
					
					if 'Content-Length' in resp2.headers.keys():
						# print('Basic URL Check: ' + url + ' Content-Length: ' + resp2.headers['Content-Length'])
						postLength = resp2.headers['Content-Length']
						print('[H]DoA Check: ' + url + ' - Successful\nContent-Length: ' + resp2.headers['Content-Length'])
						print('[H]Content-Length Difference: ' + str(int(preLength) - int(postLength)) + '\n')
					
					else:
	
						postLength = str(len(resp2.content))
						print('DoA Check: ' + url + ' Successful\nContent-Length: ' + str(len(resp2.content)))
						print('Content-Length Difference: ' + str(int(preLength) - int(postLength)) + '\n')


					with open("Live-Domains.txt", 'a+') as f1:
						f1.write(url+'\n')

				else:
					print(url + ' : Bummer!')

	  		

	except requests.exceptions.RequestException as e:
		# print('Except')
		# raise 
		print(url + ' : BIG-Bummer!')
		pass
		
		# print(resp.status_code)


def spawns(urls):
	# global results
	print('\nGathering Source Codes...\n')
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