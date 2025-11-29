# import pickle
# import base64
# from flask import Flask, request

# app = Flask(__name__)

# # ❌ VULNERÁVEL: Deserialization com pickle via HTTP
# @app.route('/load', methods=['POST'])
# def carregar_dados_vulneravel():
#     """Insecure deserialization - pickle.loads with user input"""
#     # Recebe dados do usuário via POST
#     data = request.data
    
#     # VULNERABILITY: pickle.loads can execute arbitrary code
#     obj = pickle.loads(data)
#     return str(obj)

# # ❌ VULNERÁVEL: Deserialization com base64 encoded pickle
# @app.route('/load_encoded', methods=['POST'])
# def carregar_base64_vulneravel():
#     """Insecure deserialization via base64 encoded pickle"""
#     encoded_data = request.form.get('data')
    
#     # Decode base64
#     decoded = base64.b64decode(encoded_data)
    
#     # VULNERABILITY: deserializing untrusted data
#     obj = pickle.loads(decoded)
#     return str(obj)

# # ❌ VULNERÁVEL: Deserialization via JSON body
# @app.route('/deserialize', methods=['POST'])
# def deserializar_json():
#     """Insecure deserialization from JSON request"""
#     json_data = request.get_json()
#     pickle_data = json_data.get('serialized')
    
#     # Convert from hex string to bytes
#     data_bytes = bytes.fromhex(pickle_data)
    
#     # VULNERABILITY: unsafe deserialization
#     result = pickle.loads(data_bytes)
#     return {"result": str(result)}

# # ❌ VULNERÁVEL: Deserialization via file upload
# @app.route('/upload', methods=['POST'])
# def upload_pickle_file():
#     """Insecure deserialization from uploaded file"""
#     if 'file' not in request.files:
#         return 'No file', 400
    
#     file = request.files['file']
#     file_content = file.read()
    
#     # VULNERABILITY: loading pickle from untrusted file
#     obj = pickle.loads(file_content)
#     return f"Loaded: {obj}"

# if __name__ == '__main__':
#     app.run(debug=True)
