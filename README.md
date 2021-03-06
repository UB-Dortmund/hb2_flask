# Research Bibliography Platform

The Research Bibliography Platform is a joint project between the University Library Bochum and the University Library
Dortmund. It is comprised of a web application for submitting, editing and searching bibliographic metadata about
publications produced by the UAR universities and a linked data platform for structured querying of the data.

## Host Your Own Version
To host your own instance of the platform, you should first clone this repository.

Make a new virtual environment in a Python 3 installation (if you need to maintain several Python versions next to each
other, we recommend installing [pyenv](https://github.com/yyuu/pyenv)).

Install the dependencies into this environment with ```pip install -r requirements.txt```.

Edit the contents of ```secrets.py``` and save it as ```site_secrets.py```.

You can then run the web app with ```python hb2_flask.py```

## License

The MIT License

Copyright 2015-2016 University Library Bochum <bibliogaphie-ub@rub.de>.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
