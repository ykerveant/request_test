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
    tracking_url = 'https://www.google-analytics.com/collect?v=1&t=event&tid='+tracking_id+'&cid='+clientid_str+'&ec='+event_category+'&ea='+event_action+'&el='+event_label+'&aip=1'
    #  requests.post(tracking_url)
    r = requests.post(tracking_url)
    print(tracking_url)
    print("-"*50)
    print(r.status_code)
    print("-"*50)
    print(r.headers)
    print("-"*50)


track_google_analytics_event('yann category', 'yann action', 'yann label')

"""
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
import requests

def track_google_analytics_event(event_category, event_action, event_label):
    tracking_id = 'UA-XXXXX-X'	
	clientid_str = str(datetime.now())	
	tracking_url = 'https://www.google-analytics.com/collect?v=1&t=event&tid='+tracking_id+'&cid='+clientid_str+'&ec='+event_category+'&ea='+event_action+'&el='+event_label+'&aip=1'	
	requests.post(tracking_url)

"""
