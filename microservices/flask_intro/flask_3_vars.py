from pprint import pprint
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    print('**********************************************')
    print('** Processing request:')
    print('** Request:')
    print(request)
    print('** Request environ:')
    pprint(request.environ)

    response = jsonify({'Hello': 'World!'})

    print('** Response:')
    print(response)
    print('** response data:')
    print(response.data)
    print('**********************************************')

    return response


@app.route('/api/person/<int:person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})
    return response


if __name__ == '__main__':
    print('**********************************************')
    print('** Starting app:')
    print(app.url_map)
    print('**********************************************')
    app.run()