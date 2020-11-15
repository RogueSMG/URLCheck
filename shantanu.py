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
        if resp.status_code == 200:
            # print(resp.status_code)
            resp2 = requests.get(url+"/zz11")
            if resp2.status_code == 200:
            	with open("Dead-Domains.txt", 'w') as f1:
            		f1.write(url)
            else:
            	with open("Live-Domains.txt", 'w') as f1:
            		f1.write(url)
      
    except Exception as e:
        # print('Except')
        print ('Exception')
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