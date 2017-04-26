#!/usr/bin/python
import os
from app import app
app.run(host=os.environ['IP'],port=int(os.environ['PORT']), debug=True)