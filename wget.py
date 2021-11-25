import sys
import requests
url =  sys.argv[1]
split_data = url.split("/")
file_name= split_data[len(split_data)-1]
r = requests.get(url)
open(f'{file_name}', 'wb').write(r.content)


