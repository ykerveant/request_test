#  https://www.themarketingtechnologist.co/measure-your-python-projects-with-google-analytics/
#  bot issues : https://www.quantable.com/analytics/bots-in-google-analytics/
#  untick "exclude known bots and spiders" in Ga view property to let the hit getting in
#  https://www.bounteous.com/insights/2014/03/04/tracking-offline-transactions-universal-analytics/?lang=en-ca
#  https://www.optimizesmart.com/understanding-universal-analytics-measurement-protocol/
#  campaign data : https://www.optimizesmart.com/sending-campaign-data-via-measurement-protocol-google-analytics/

#  intercept request https://github.com/AutomatedTester/browsermob-proxy-py

#  MAIN CHALLENGE IS TO BYPASS THE BOTFILTERING
#  to do : write a function to send pageviews (with utm)



import requests


def track_google_analytics_event(event_category, event_action, event_label):
    tracking_id = 'UA-145181024-1'
    clientid_str = 'yanito211'
    tracking_url = 'https://www.google-analytics.com/collect?v=1&t=event' \
                   '&tid=' + tracking_id + \
                   '&cid=' + clientid_str + \
                   '&ec=' + event_category + \
                   '&ea=' + event_action + \
                   '&el=' + event_label + \
                   '&aip=1'
    r = requests.post(tracking_url)
    print(tracking_url)
    print("-"*50)
    print(r.status_code)
    print("-"*50)
    print(r.headers)
    print("-"*50)


track_google_analytics_event('yann category', 'yann action', 'yann label')


def track_google_analytics_pageview(host_name, page_name, page_title):
    tracking_id = 'UA-145181024-1'
    clientid_str = 'yanito211'
    tracking_url = 'https://www.google-analytics.com/collect?v=1&t=pageview' \
                   '&tid=' + tracking_id +\
                   '&cid=' + clientid_str + \
                   '&dh=' + host_name + \
                   '&dp=' + page_name + '&dt=' + page_title + \
                   '&aip=1'
    r = requests.post(tracking_url)
    print(tracking_url)
    print("-"*50)
    print(r.status_code)
    print("-"*50)
    print(r.headers)
    print("-"*50)


track_google_analytics_pageview('www.mysite.com', '/article1111', 'The great article')


"""
=> integration headers

import requests

url = 'SOME URL'

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

response = requests.get(url, headers=headers)

"""
#  or : https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit
"""
220

Provide a User-Agent header:

import requests

url = 'http://www.ichangtou.com/#company:data_000008.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.content)
FYI, here is a list of User-Agent strings for different browsers:

List of all Browsers

"""

"""
SENDING MULTIPLE HITS IN ONE REQUEST / NOT COLLECT BUT BATCH

"User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.69 Safari/537.36

POST https://www.google-analytics.com/batch?

v=1&t=event&tid=UA-1500844-18&cid=98880ed4-c224-4b3c-b2e2-35a491373751&ec=videos-1&ea=play&el=spider%2520man1&ev=100

v=1&t=event&tid=UA-1500844-18&cid=98880ed4-c224-4b3c-b2e2-35a491373751&ec=videos-2&ea=play&el=spider%2520man2&ev=100

v=1&t=event&tid=UA-1500844-18&cid=98880ed4-c224-4b3c-b2e2-35a491373751&ec=videos-3&ea=play&el=spider%2520man3&ev=100"


"""