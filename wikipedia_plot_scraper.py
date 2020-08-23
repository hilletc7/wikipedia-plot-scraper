import urllib
import urllib.request as ur
from bs4 import BeautifulSoup

url = input("Enter a moive/book url from Wikipedia:")

url = ur.urlopen(url)
html = url.read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

startt = text.find("Wikipedia") + 10
endt = text.find("From", startt) - 1
title = text[startt:endt]

start = text.find("Plot[edit]") + 10
end = text.find("[edit]", start)
plot = text[start:end]

filename = "%s.txt" % title

text_file = open(filename, "w", encoding="utf-8")
text_file.write(plot)
text_file.close()

lines = open(filename, encoding="utf-8").read()
lines = lines[lines.find('\n')+1:lines.rfind('\n')]

print("")
print(title)
print("")
print(lines)

text_file = open(filename, "w", encoding="utf-8")
text_file.write(lines)
text_file.close()
