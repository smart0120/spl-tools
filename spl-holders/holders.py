import requests

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'getProgramAccounts',
    'params': [
        'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA',
        {
            'encoding': 'jsonParsed',
            'filters': [
                {
                    'dataSize': 165,
                },
                {
                    'memcmp': {
                        'offset': 0,
                        'bytes': 'TOKEN_ADDRESS',
                    },
                },
            ],
        },
    ],
}

response = requests.post('http://api.mainnet-beta.solana.com', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '\n  {\n    "jsonrpc": "2.0",\n    "id": 1,\n    "method": "getProgramAccounts",\n    "params": [\n      "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",\n      {\n        "encoding": "jsonParsed",\n        "filters": [\n          {\n            "dataSize": 165\n          },\n          {\n            "memcmp": {\n              "offset": 0,\n              "bytes": "FBHFo6uQheu5WNXhryDUpkDwyCQP6e1iTF56veLVJu3a"\n            }\n          }\n        ]\n      }\n    ]\n  }\n'
#response = requests.post('http://api.mainnet-beta.solana.com', headers=headers, data=data)

with open('holders.json', 'wb') as f:
    f.write(response.content)
