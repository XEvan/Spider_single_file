# coding:utf-8
import hashlib
import random
import time
import urllib
import urllib2
import json

class Tran:
	def getSign(self, n):
		'''
		description:generate the sign_value
		param:S->"fanyideskweb"
		      r->当前时间和1~10随机数生成的值
		      D->"ebSeFb%=XZ%T[KZ)c(sy!"
		      n->要查询的内容
		'''
		S = "fanyideskweb"
		r = "" + str(int(time.time()*1000)) + str(int(random.random()*10))
		D = "ebSeFb%=XZ%T[KZ)c(sy!"
		sign = hashlib.md5(S+n+r+D)
		return sign.hexdigest()

	def tranInfo(self, url, formdata):
		'''
		description:post传入的formdata到url，抓取翻译后的信息（json格式）
		'''
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
			"Host":"fanyi.youdao.com",
			"Origin":"http://fanyi.youdao.com",
			"Referer":"http://fanyi.youdao.com/",
		}

		data = urllib.urlencode(formdata)

		request = urllib2.Request(url, data=data, headers=headers)
		response = urllib2.urlopen(request)
		return response.read()

def main():
	value = raw_input("Please enter the content you want to translate:")

	tran = Tran()

	formdata = {
		"i":value,
		"from":"AUTO",
		"to":"AUTO",
		"smartresult":"dict",
		"client":"fanyideskweb",
		"salt":int(time.time()*1000) + random.randint(1,10),
		"sign":tran.getSign(value),
		"doctype":"json",
		"version":"2.1",
		"keyfrom":"fanyi.web",
		"action":"FY_BY_REALTIME",
		"typoResult":"false"
	}

	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	result = tran.tranInfo(url, formdata)

	return result

if __name__ == "__main__":
	result = main()
	result = json.loads(result)
	print "source:", result["translateResult"][0][0]["src"]
	print "result:", result["translateResult"][0][0]["tgt"]
