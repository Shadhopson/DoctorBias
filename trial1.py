from lxml import html
import pprint
import requests
page = requests.get('https://www.zocdoc.com/doctor/kyawt-aung-md-130392?LocIdent=70050&reason_visit=75&insuranceCarrier=-1&insurancePlan=-1')
tree = html.fromstring(page.text)

#print tree

buyers = tree.xpath('//*[@itemprop="reviewBody"]/text()')
#prices = tree.xpath('//h2/text()')
#print 'Doctor Review ', buyers
doctorReviews = open('drKyawtReview.txt','a')
doctorReviews.write(pprint.pformat(buyers))
#print 'Prices: ', prices
#doctorReviews = open('doctorReviews.txt','a')

#for item in buyers:
#    print>>doctorReviews, item
#    doctorReviews.write(item)

#doctorReviews.close()

