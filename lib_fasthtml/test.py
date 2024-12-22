from starlette.testclient import TestClient
from main import app

# testing request ke website itu

# web client
client = TestClient(app)

# route
r = client.get("/home")
print(r.text)