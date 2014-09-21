
# coding: utf-8

# In[1]:

import mechanize
browser = mechanize.Browser()
browser.open('http://acm.zju.edu.cn/onlinejudge/login.do')
browser.select_form(nr = 0)
browser.form['handle'] = 'liangjiaxing'
browser.form['password'] = ''
browser.submit()
browser.open('showRuns.do?contestId=1&search=true&firstId=-1&lastId=-1&problemCode=&handle=liangjiaxing&idStart=&idEnd=&languageIds=2&judgeReplyIds=5')


# In[4]:

s = '/onlinejudge/showSubmission.do?submissionId='
p = '/onlinejudge/showProblem.do?problemId='
J = 'JavaScript:%20goNext('
links = [link.url for link in browser.links()]


# In[5]:

p_link = ''
lastId = '-1'
while True:
    flag = False
    browser.open('http://acm.zju.edu.cn/onlinejudge/showRuns.do?contestId=1&search=true&firstId=-1&lastId='+lastId+'&problemCode=&handle=liangjiaxing&idStart=&idEnd=&languageIds=2&judgeReplyIds=5')
    links = [link.url for link in browser.links()]
    for link in links:
        if link[:len(J)] == J:
            lastId = link[len(J):-2]
            flag = True
        if link[:len(p)] == p:
            p_link = 'http://acm.zju.edu.cn'+link
        if link[:len(s)] == s:
            res = browser.open('http://acm.zju.edu.cn'+link)
            code = '/*\n'+p_link+'\n*/\n'+res.read()
            f = open('./hwn/ZOJ/'+link[-7:]+'.cpp', 'w')
            f.write(code)
            f.close()
    print lastId
    if not flag:
        break


# In[ ]:

print l


# In[ ]:



