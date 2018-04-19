import urllib2
f = urllib2.urlopen('http://vikingi-online.com/online/4-season/')
out = open('site.txt','w')
s = f.read()
text = s[s.find('<body'):s.find('</body>') ]
s = ''
out.write(text)
