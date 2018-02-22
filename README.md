版本：Python2.7
OS：Ubuntu

需求：
  使用python爬取有道翻译的翻译结果。

遇到的问题：
  1、表单验证中的salt和sign是动态的，根据js来分析它们的生成方法
    "salt"：由《当前的时间》和《1到10之间的随机数》生成
    "sign": n = 要查询的单词
            S = "fanyideskweb"
            r = "" + str(int(time.time()*1000)) + str(int(random.random()*10))
            D = "ebSeFb%=XZ%T[KZ)c(sy!"
            将（n+S+r+D）进行md5加密得到sign值

  2、所有的信息处理好之后，运行程序，响应结果为-->'errorCode': 50
    发现请求的url为“http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule”， 将其改为“http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule”之后，则可以返回正常的结果。#原因暂未查明。。。
