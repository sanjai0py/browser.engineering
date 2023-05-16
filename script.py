from urllib.parse import urlparse
import socket

url = "https://browser.engineering/index.html"

def request(url):
    # Parse a URL into 6 components:
    # <scheme>://<netloc>/< path >
    # <params >?<query >#<fragment>
    host = urlparse(url)

# 1. Creating new socket
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

# 2. Connecting to the socket
    s.connect((host.netloc, 80))

# 3. Sending requets for data
    s.send(f"GET {host.path} HTTP/1.0\r\n".encode("utf8") +
           f"Host: {host.netloc}\r\n\r\n".encode("utf8"))

# 4. The response received from the server
    response = s.makefile("r", encoding="utf8", newline="\r\n")

    # reading the first line of the file
    statusline = response.readline()

    # HTTP/1.1 404 Not Found
    version, status, explanation = statusline.split(" ", 2)

    # Checking if the response is OK
    assert status == "200", f"{status}: {explanation}"

    # refer this image for better understanding
    # http://www.tcpipguide.com/free/diagrams/httpresponse.png
    headers = {}
    while True:
        line = response.readline()
        if line == "\r\n":
            break
        header, value = line.split(":", 1)
        headers[header.lower()] = value.strip()

    assert "transfer-encoding" not in headers
    assert "content-encoding" not in headers

    body = response.read()
    s.close()
    return body


print(request(url))
