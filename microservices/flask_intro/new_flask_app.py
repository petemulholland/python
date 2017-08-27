#!python
import sys
import os


def usage():
    print('usage:')
    print('new_flask_app <filename>')


FLASK_TEMPLATE = [
    'from flask import Flask, jsonify, g',
    '',
    '',
    'app = Flask(__name__)',
    '',
    '',
    "@app.route('/api')",
    "def my_microservice():",
    "    return jsonify({'Hello': 'World!'})",
    '',
    '',
    "if __name__ == '__main__':",
    '    app.run()',
]


def check_filename(filename):
    file_name, file_ext = os.path.splitext(filename)
    if not file_ext:
        file_ext = '.py'
    elif file_ext != '.py':
        file_name += file_ext
        file_ext = '.py'

    return file_name + file_ext


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        filename = check_filename(sys.argv[1])
        with open(filename, 'w') as f:
            f.writelines([line + '\n' for line in FLASK_TEMPLATE])
