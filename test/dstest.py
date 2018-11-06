#from ds18b20 import DS18B20	
import logging
	
# test temperature sensors
logging.basicConfig(filename='test.log', format="%(asctime)s %(levelname)s: %(message)s",level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# x = DS18B20()
# count=x.device_count()
# i = 0
# while i < count:
# 	print(x.tempC(i))
# 	i += 1