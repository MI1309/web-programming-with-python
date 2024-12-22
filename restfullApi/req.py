# from requests import put, get

# route = input("masukkan route url: ")
# url = f"http://127.0.0.1:5000/{route}"

# put_data = input("masukkan data: ")       
            
# put(url, data={"data":f"{put_data}"})
# put("http://127.0.0.1:5000/api", data={"data": "data api"}).json()

# print(f"data diambil url {url}:",get(url).json())
# print("data api:", get("http://127.0.0.1:5000/api").json())    

from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
args = parser.parse_args()
