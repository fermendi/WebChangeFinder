-------------------------------------------------------------
# WebChangeFinder

Simple bot for detecting changes in websites.

#### Fernando Mendiburu - 2020
-------------------------------------------------------------

# Table of Contents

- [Installation](#installation)
- [Dependences](#Dependences)

This bot finds changes in a website chosen by the user.

## Installation

Go to `/home/user` directory:

```
$ cd
```

Download from [here](https://github.com/fermendi/WebChangeFinder/archive/master.zip) or using git clone:

```
$ git clone https://github.com/fermendi/WebChangeFinder.git
```

## Dependences

Update the package index by running the following command:

```
$ sudo apt-get update
```

#### Install `python` (using Python 2.7.17)

```
$ sudo apt-get install python
```

#### Install `pip` for `Python 2` with:

```
$ sudo apt-get install python-pip
```

#### Install `selenium` package:

See this [explanation](https://selenium-python.readthedocs.io/installation.html) or see below:

```
$ pip install selenium
```

Selenium requires a driver to interface with the chosen browser.
Google Chrome driver is available [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
See the version of your Google Chrome browser before download the driver.

Download the driver in the same script folder or change the driver path in the script.

#### Install `request` library:

This library makes HTTP requests in Python.

```
$ pip install requests
```
