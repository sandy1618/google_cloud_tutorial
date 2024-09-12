from flask import jsonify

def hello_world(request):
    request_json = request.get_json()
    name = request_json.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")
