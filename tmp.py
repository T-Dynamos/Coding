
import base64
import requests

class Github:
	def __init__(self,token = "",repo="",owner=""):
		self.token = token
		self.repo = repo
		self.owner = owner
	def upload(self,file,path,message):
		url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{path}"
		f = open(file,"rb").read()
		filex = base64.b64encode(f)
		data = '{"message":"'+message+'","content":"'+filex.decode()+'"}'
		headers = {
			"Authorization":f"token {self.token}",
			"Content-Type": "application/json"
		}
		a = requests.put(url,data=data, headers=headers)
		return a.text

Github_Instance = Github(token="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",repo="PythonHeader",owner="T-Dynamos")

print(Github_Instance.upload("/sdcard/tmp.py","tmp.py","Test with api"))	