import datetime
import requests
import pandas
from bs4 import BeautifulSoup
import smtplib #smtplib这个模块是管发邮件
from email.mime.text import MIMEText #构造邮件内容
from email.mime.multipart import MIMEMultipart #发带附件的邮件用的


teng_total = []
time1 = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")

email_host = 'smtp.qq.com'     #邮箱服务器地址
email_user = '*@qq.com'  # 发送者账号
email_pwd = '*'
# 发送者密码是邮箱的授权码，不是登录的密码
maillist = '1063157989@qq.com'


url = 'http://v.qq.com/tech'
res = requests.get(url)
res.encoding = 'utf-8'
soup1 = BeautifulSoup(res.text,'html.parser')
for teng in soup1.select('.mod_figure_1f2r '):
    for i in range(0,10):
        url1 = teng.select('.figure')[i]['href']#['.figure']#[1]
        title = teng.select('.figure_detail')[i]('a')[0]['title']#[1].text
        teng_total.append({
            '网页' : url1,
            '标题' : title,
            })
        print(url1,title)
df = pandas.DataFrame(teng_total)
file = df.to_excel(time1+'txrd'+'.xlsx')


file = time1+'txrd'+'.xlsx'       
def toemail():
    
    new_msg = MIMEMultipart()
    #构建了一个能发附件的邮件对象
    new_msg.attach(MIMEText('腾讯视频'+time1+'热点信息'))
    # 邮件内容
    new_msg['Subject'] = '腾讯视频'+time1+'热点信息'    # 邮件主题
    new_msg['From'] = email_user    # 发送者账号
    new_msg['To'] = maillist    # 接收者账号列表
    print(file)
    att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = ('application/octet-stream')
    att["Content-Disposition"] = ( 'attachment; filename='+time1+'txrd'+'.xlsx')
    new_msg.attach(att)
    smtp = smtplib.SMTP(email_host,port=25) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
    smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
    smtp.sendmail(email_user, maillist, new_msg.as_string())
    # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    smtp.quit() # 发送完毕后退出smtp
    print ('email send success.')


toemail()