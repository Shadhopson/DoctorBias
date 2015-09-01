from lxml import html
import requests

page requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
tree = html.fromstring(page.text)

print tree
