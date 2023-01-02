import advertools as adv
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import csv
from ippanel import Client

#url site 
df = adv.sitemap_to_df("https://site.com/sitemap.xml") #ادرس سایت مپ شما
site = 'sc-domain:site.com' #ادرس سایت شما در سرچ کنیول

"""
اگر سایت شما به صورت
all url 
وریفای شده باید اول ادرس خود
sc-domain 
را اضافه کنید.
"""

#ippanel pattern
api_key = "9EqNJ#######################x3KgAJ0=" # api که از ای پی پنل گرفتید
sms = Client(api_key)


"""
پترن خود را بسازید 
و نام متغیر خود را 
file_name 
قرار بدید
"""
#functionS
def send_sms():
    pattern_values = {
        "file_name": "check_ME.csv",
    }

    message_id = sms.send_pattern(
        "iehsf#########",    # کد پترن
        "+985000######", # شماره سیستم ارسال پیامک
        "989101418818",  # شماره تلفن شما
        pattern_values,  # pattern values

    )

#function diffrent days
def diffren_days():
    lastCrawl = (datetime.datetime.strptime(lastCrawlTime , "%Y-%m-%dT%H:%M:%SZ"))
    today = datetime.date.today()
    someday = datetime.date(lastCrawl.year, lastCrawl.month, lastCrawl.day)
    diff =  today - someday
    return diff.days


#create sitemap csv
date_str = datetime.datetime.now().strftime('%Y-%m-%d')
filename_with_date = 'sitemap_{}.csv'.format(date_str)
sitemap_csv = open(filename_with_date, "w")

for link in df['loc']:
    sitemap_csv.write(link+'\n')
sitemap_csv.close()

#credentials console.cloud.google Service Accounts  
credentials = service_account.Credentials.from_service_account_file(
  "service_account.json") 

#credentials scoped 
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/webmasters','https://www.googleapis.com/auth/webmasters.readonly'])

service = build('searchconsole','v1',credentials=credentials)

#open sitemap
f = open(filename_with_date, 'r')


with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['URL','Date'])

with open('check_ME.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['URL','Date'])


for link in f:
    #request to inspect URL
    request = {
        'inspectionUrl': link,
        'siteUrl': site}
    
    # get response inspect URL
    response = service.urlInspection().index().inspect(body=request).execute()
    lastCrawlTime = response.get('inspectionResult').get('indexStatusResult').get('lastCrawlTime')

    if diffren_days() < 30:
        with open('result.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([request.get('inspectionUrl'), diffren_days()])
    else:
        with open('check_ME.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([request.get('inspectionUrl'), diffren_days()])


send_sms()



