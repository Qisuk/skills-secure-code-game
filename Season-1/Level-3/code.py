# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass
        print(f"{path}")
        print(f"{str(path).find('..')}")
        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..'):
            return None
        if str(path).find('..') != -1:
            return None
        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        print(prof_picture_path)
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        print("get_tax_form_attachment")
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")
        try:
            with open(path, 'rb') as form:
                tax_data = bytearray(form.read())
        except Exception as ex:
            print(ex)
            return None

        # assume that tax data is returned on screen after this
        print(path)
        return path