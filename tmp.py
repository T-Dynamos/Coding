import string    
import random
rstr = lambda S : str(''.join(random.choices(string.ascii_uppercase + string.digits, k = S)))
import time
#for i in range (1,13):
#	time.sleep(0.1)
	#print(str(i)+"."+rstr(4))
import base64
import requests
class Github():
	token = "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"
	repo = "T-Dynamos"
	def __init__(self):
		token = self.token
		repo = self.repo
	def upload(file,path):
		token = "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"
		repo = "T-Dynamos"
		url = f"https://api.github.com/repos/{repo}/PythonHeader/contents/{path}"
		f = open(file,"rb").read()
		filex = base64.b64encode(f)
		print (filex.decode())
		data = '{"message":"Sample File","content":"'+filex.decode()+'"}'
		headers = {"Authorization":f"token {token}"}
		a = requests.put(url,data=data, headers=headers)
		return a.text
		

print(Github.upload("/sdcard/tmp.py","tmp.py"))	