import httpx
from httpx import Request
from httpx import USE_CLIENT_DEFAULT
client = httpx.Client()
request = Request('GET', 'https://www.example.com')
client.send(request, timeout=USE_CLIENT_DEFAULT)