# learning-python
Learning python through online tutorials

## Resources
* [Fullstack Python](https://www.fullstackpython.com/)
* [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Troubleshooting
* Cloud9 - [Getting Started with Flask on Cloud9](https://damyanon.net/getting-started-with-flask-on-cloud9/)
* Cloud9 - open file from terminal: [http://stackoverflow.com/questions/28028178/cloud-9-how-to-open-a-file-in-the-c9-editor-from-c9-terminal](http://stackoverflow.com/questions/28028178/cloud-9-how-to-open-a-file-in-the-c9-editor-from-c9-terminal)
* Cloud9 - shebang path: [https://unix.stackexchange.com/questions/94071/running-python-script-from-linux-terminal](https://unix.stackexchange.com/questions/94071/running-python-script-from-linux-terminal0)
* Python - shebang path: [http://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script](http://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script)
* Cloud9 - IP/Port: [https://community.c9.io/t/running-flask-python-application/10997/2](https://community.c9.io/t/running-flask-python-application/10997/2)
* Cloud9 - IP/Port: [https://maltmann.wordpress.com/2014/03/25/setting-up-flask-app-on-cloud9/](https://maltmann.wordpress.com/2014/03/25/setting-up-flask-app-on-cloud9/)

## Getting Started on Cloud9

### Optimize Your C9 Experience (optional)
Install the c9 library to open a file in the C9 editor from the C9 terminal:

```
$ sudo npm install -g c9
```

You can then use the following command to open a file in the editor:
```
$ c9 open run.py
```

### Install Flask

```
$ sudo easy_install flask
```

### Create the Folder Structure

```
app
app/static
app/templates
tmp
```

### Create the Basic Files

```
app/__init__.py
app/views.py
run.py
```

### ```__init__.py```
Add the following code:

```
from flask import Flask

app = Flask(__name__)
from app import views
```

### ```views.py```
Add the following code:

```
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
```

### ```run.py```
Also can be ```app.py```.

Add the following code (note that this file contains environment information specific to Cloud9):

```
#!/usr/bin/python
from app import app
app.run(host='0.0.0.0', port=8080, debug=True)
```

Indicate what python interpreter to use (if you have multiple versions installed) in the shebang line (Unix-specific):

```
#!/usr/bin/python
```

You can find the path to use in your environment by using the following command:

```
$ type -P python
```

In the call to ```app.run()```, specify the server IP (0.0.0.0) and port (8080) for Cloud9:

```
app.run(host='0.0.0.0', port=8080, debug=True)
```

Alternatively, import and pass the C9 environment variables:

```
import os
...
app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
```

### Make ```run.py``` Executable
On Linux, indicate that the ```run.py``` file is executable (may need ```sudo```):

```
$ chmod a+x run.py
```

Then run the file:

```
$ ./run.py
```
