import json
import io

data={
    'name':'chetan',
    'roll':1004,
    'city':'kalapani'}
    
json_data=json.dumps(data)
print(json_data)
print(type(json_data))

print()

stream=io.BytesIO(json_data)
print(stream)
print(type(stream))