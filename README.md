# Rest API Python Django

## Description
Restful API Example Python Django

## Onboarding and Development Guide
### Prerequisites
- Python3 3.7.7 (Primary)
- GIT

### Setup and Installation
#### Linux
```
$ export LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
$ sudo apt-get update
$ sudo apt-get install python3.6
$ sudo dnf install python3
```
#### Mac
```
$ export LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH" (Latest OS X)
$ export PATH=/usr/local/bin:/usr/local/sbin:$PATH (OS X 10.12 (Sierra) or older)
$ brew install python
```
#### Setup Project
```
$ python3 -V
$ pip install --upgrade pip
$ python3 -m venv env
$ . env/bin/activate
$ cp env.sample .env
$ pip install -r requirements.txt
$ pip manage.py makemigrations
$ pip manage.py migrate
```
#### Run Project
```
$ python3 manage.py runserver <port>
```
#### Console
```
$ python3 manage.py shell
```
