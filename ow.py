import logging
import time
import schedule
import psycopg2
import urllib.request
import json
import datetime
import yaml
import sys

def build_url(plat, reg, tag):
	url = config['api'] + '{}/{}/{}/profile'
	return url.format(plat,reg,tag)

def get_ranked_job():
	conn = connect()
	cur = conn.cursor()
	users = get_users(cur)
	for user in users:
		logging.info(user)
		id = user[0]
		tag = user[1]
		plat = user[2]
		reg = user[3]
		url = build_url(plat,reg,tag)
		logging.info('Getting: ' + url)
		resp = urllib.request.urlopen(url)
		j = resp.read().decode('utf-8')
		data = json.loads(j)
		rank = int(data['data']['competitive']['rank'])
		insert_rank(cur, id, rank)
		conn.commit()
	conn.close()


def insert_rank(cur, id, rank):
	query = open(config['insert-rank'],'r').read()
	query = query.format(id, rank)
	logging.info('Running: \n' + query)
	cur.execute(query)
	


def get_users(cur):
	query = open(config['users-query'],'r').read()
	logging.info('Running: \n' + query)
	cur.execute(query)
	return cur.fetchall()


def connect():
	return psycopg2.connect(host=config['host'], port=config['port'], database=config['database'])

def main():
	schedule.clear()
	schedule.every(10).minutes.do(get_ranked_job)

	while True:
		schedule.run_pending()
		time.sleep(1*60)


if __name__ == '__main__' :
	logging.basicConfig(stream=sys.stdout,
        	            level=logging.INFO,
                	    format='%(asctime)s %(levelname)-5s %(message)s',
          	   	    datefmt='%Y-%m-%d %H:%M:%S')
	config = yaml.load(open('config.yaml','r').read())
	main()
