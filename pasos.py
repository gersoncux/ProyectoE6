import urllib.request as url
import json
import math 
import time
from datetime import datetime
    
# Latitud y Logitud de la Ciudad de Madrid (usada como ejemplo)
latitud=14.5833
longitud=-90.5167
n=10 #número de veces que pasará la ISS

Pass=url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud,longitud,n))
response_Pass= url.urlopen(Pass)

Pass_obj = json.loads(response_Pass.read())
print ("")
pass_list=[]
for count,item in enumerate(Pass_obj["response"], start=0):
	pass_list.append(Pass_obj['response'][count]['risetime'])
	print(datetime.fromtimestamp(pass_list[count]).strftime('%d-%m-%Y %H:%M:%S'))
