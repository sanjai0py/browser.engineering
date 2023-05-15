from urllib.parse import urlparse
import socket

# the url to request response for.
url = "https://browser.engineering/index.html"
# url = "http://example.org/index.html"

# parsing the url
host = urlparse(url)


s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
)

s.connect((host.netloc, 80))

s.send("GET {} HTTP/1.0\r\n".format(host.path).encode("utf8") +
       "Host: {}\r\n\r\n".format(host.netloc).encode("utf8"))
       
response = s.makefile("r", encoding="utf8", newline="\r\n")

statusline = response.readline()
version, status, explanation = statusline.split(" ", 2)
assert status == "200", "{}: {}".format(status, explanation)


headers = {}
while True:
    line = response.readline()
    if line == "\r\n":
        break
    header, value = line.split(":", 1)
    headers[header.lower()] = value.strip()
# print(headers)
assert "transfer-encoding" not in headers
assert "content-encoding" not in headers

body = response.read()
s.close()
print(body)
print(response.read())


# creating a requets function that abstracts the above code

def request (url):
    print("Suuuuuuuuuuuuu")