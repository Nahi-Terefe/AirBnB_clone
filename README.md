# 0x00. AirBnB clone - The console

`Release date: Dec-28-2022`

<img src="img/65f4a1dd9c51265f49d0.png">

## 0x00.Table of contents

* [0x01 Introduction](#0x01-Introduction)
* [0x02 Environment](#0x02-Environment)
* [0x03 Installation](#0x03-Installation)
* [0x04 Testing](#0x04-Testing)
* [0x05 Usage](#0x05-Usage)
* [0x06 License](#0x07-License)
* [0x07 Contributing](#0x08-Contributing)
* [0x0A References](#0x0A-References)
* [0x0B Credits](#0x0B-Credits)

## 0x01 Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The console willl perform the following tasks:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## 0x02 Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.9.10. The editors used were VIM 8.1.2269, VSCode 1.6.4 and Control version using Git 2.33.1.

## 0x03 Installation

```bash
git clone https://github.com/Nahi-Terefe/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

### Execution

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 0x04 Testing

All the test are defined in the `tests` folder.

### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

* Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Python Unit Tests

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```


## 0x05 Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Commands

> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
15fe2bfd-3ad9-40b6-bae4-551fac624b83
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '15fe2bfd-3ad9-40b6-bae4-551fac624b83', 'created_at': datetime.datetime(2022, 02, 01, 17, 14, 48, 426587), 'updated_at': datetime.datetime(2021, 02, 03,  17, 14, 48, 426587)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) create User
13e7f8e0-f8ec-406c-853c-4a46a6de8a40
(hbnb) destroy User 13e7f8e0-f8ec-406c-853c-4a46a6de8a40
(hbnb) show User 13e7f8e0-f8ec-406c-853c-4a46a6de8a40
** no instance found **
(hbnb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
826f61f7-4804-49e2-9d82-4a592a5a9f75
(hbnb) all BaseModel
["[BaseModel] (826f61f7-4804-49e2-9d82-4a592a5a9f75) {'id': '826f61f7-4804-49e2-9d82-4a592a5a9f75', 'created_at': datetime.datetime(2022, 2, 4, 17, 24, 17, 366821), 'updated_at': datetime.datetime(2022, 2, 4, 17, 24, 17, 366821)}"]
["[BaseMode
```

* count

> *Prints the number of instances of a given class.*

```bash
(hbnb) count BaseModel
2
(hbnb)
```

* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*

```bash
(hbnb) update User 826f61f7-4804-49e2-9d82-4a592a5a9f75 email "dummy@gmail.com"
(hbnb) show User 826f61f7-4804-49e2-9d82-4a592a5a9f75
[User] (s) [User] (826f61f7-4804-49e2-9d82-4a592a5a9f75) {'id': '826f61f7-4804-49e2-9d82-4a592a5a9f75', 'created_at': datetime.datetime(2022, 2, 4, 17, 24, 17, 366821), 'updated_at': datetime.datetime(2022, 2, 4, 17, 24, 17, 366821)}, 'email': 'dummy@gmail.com'}
(hbnb)

```
## 0x06 License

This project is under the MIT License.

## 0x07 Contributing

This is a team project for practice and learning purposes. Contribution is welcome and encouraged.
## 0x0A References

https://www.tutorialspoint.com/python/index.htm

https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/

https://www.w3schools.com/python/python_modules.asp

https://docs.python.org/3.4/tutorial/modules.html#packages

https://docs.python.org/3/library/unittest.html

https://developers.google.com/edu/python

## 0x0B Credits

> *Console team: Nahom Fikadu & Kidus Efrem


Nahom Fikadu

<a href="https://twitter.com/NahiFikadu" target="_blank">  <img align="left" alt="Nahom Fikadu | Twitter" src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FNahiFikadu" /> </a>

<a href="https://github.com/Nahi-Terefe" target="_blank">  <img align="left" src="https://img.shields.io/github/followers/Nahi-Terefe?style=social" alt="Nahom Terefe | Github"> </a>

<br/>
<br/>

Kidus Efrem

<a href="https://github.com/K1dus" target="_blank">  <img align="left" src="https://img.shields.io/github/followers/K1dus?style=social"> </a>

<br/>
