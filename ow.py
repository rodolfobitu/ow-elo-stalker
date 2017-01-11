import scheduler
import logging
import time
import schedule

def get_ranked_job():
	


def main():
	shedule.every(10).minutes.do(get_ranked_job)

	while true:
		schedule.run_pending()
		time.sleep(1*60)


if __name__ == 'main' :
	logging.basicConfig(stream=sys.stdout,
        	            level=logging.INFO,
                	    format='%(asctime)s %(levelname)-5s %(message)s',
          	   	    datefmt='%Y-%m-%d %H:%M:%S')
	main()
