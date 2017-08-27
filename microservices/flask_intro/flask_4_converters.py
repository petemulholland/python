from pprint import pprint
from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}


class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser


@app.route('/api')
def my_microservice():
    print(request)
    pprint(request.environ)

    response = jsonify({'Hello': 'World!'})

    print(response)
    print(response.data)

    return response


@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello': name})
    return response


if __name__ == '__main__':
    print('**********************************************')
    print('** Starting app:')
    print(app.url_map)
    print('**********************************************')
    app.run()