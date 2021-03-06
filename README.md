# Silly Dog Meme Generator

This is a silly dog meme generator written with Python and [Flask](https://flask.palletsprojects.com/en/1.1.x/) Web Application framework.

## Demo

I am currently exploring options where to deploy this, most likely Heroku, once it's ready I will add the link here 🧐

![](resource/gif/demo.gif)

## Functionality

Basic functionality of the application are as follows:

- Users can generate randomized memes

Future functionalities I may add:

- Allow users to upload their own meme quotes and dog photos.

## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You should have [pip](https://pip.pypa.io/en/stable/installing/) installed.

### Installation

First install the dependencies by running `pip install -r requirements.txt`. Then you can follow the below instructions depending on the type of your terminal.

Bash

```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

CMD

```
> set FLASK_APP=hello.py
> flask run
 * Running on http://127.0.0.1:5000/
```

PowerShell

```
> $env:FLASK_APP = "hello.py"
> flask run
 * Running on http://127.0.0.1:5000/
```

## Contributing

If you would like to suggest an update of your own, please submit it as a pull request.

#### Submitting a Pull Request

1. Create a feature branch: `git checkout -b project-suggestion`
2. Commit your changes: `git commit -m "Explain Feature"`
3. Push to the branch: `git push origin project-suggestion`
4. Submit a pull request.
   Please note that this only works if you have forked the repository.
