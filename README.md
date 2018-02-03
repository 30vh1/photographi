``` This is a project still in early stages of development so, heavy changes should be expected !!! ```  
# PhotograΦ   

> Take screenshots of various services and websites on an automated form  

## Table of contents

1. [About](#about)
2. [Non-python Dependencies](#dependencies)
3. [How To](#how-to)  

    - [Installation](#installation)
    - [Usage](#usage)  

## About    

This is a project I am developing with various purposes.
1. The first one is to get in touch with **python**. As for now I've only used it as a resource for small scripts as a bash substitute in most cases.  
2. The second one is to begin with a middle-sized project. It's been a while since I tried to start a project from beginning to end and this is feels like a right project to do it, not too complicated but with some time of development and a lot of learning put in it.  

Probably there's more to it than what I've just wrote but, you get the idea right? :)  


## Non-python dependencies  

As this project is built upon **Selenium** using **Google Chrome**, **Chromedriver** and **Google Chrome** are a must that should be satisfied in order to be able to take advantage of this Software.

### On Windows  

* Download and install Google Chrome from [here][google-chrome-url-windows]  
* Download the latest version of Chromedriver from [here][chromedriver-url-windows]  
  
### On Linux  
* Install Google Chrome from your package manager or download it from [here][google-chrome-url-linux]  

    * It's also possible to use Chromium instead of Google Chrome for those who desire it  
* Install Chromedriver from your package manager o dowload the latest version from [here][chromedriver-url-linux]   

## How-To

### Installation  
### Configuration
### Usage   
```python  
λ  python.exe .\capture.py -h
usage: capture.py [-h] [-path [path]] [-file [file]] [-threads [threads]]
                  [-ip [ip]]

Takes screenshots of a IP or group of IP

optional arguments:
  -h, --help          show this help message and exit
  -path [path]        path to store all data (Optional)
  -file [file]        file to read IP/domains from
  -threads [threads]  number of threads to use (only when reading from file)
  -ip [ip]            ip to scan (In case there's only one
``` 
### Example  
* Executing the following line   

```shell  
λ  .\capture.py -path ../test/captures -ip http://google.es
```

* Will create a folder named ```captures``` under the test directory
``` 
/photographi |
			 | /src
					| capture.py
					| capture_IP.py
					| customip.py
			 | /test
				 	| /captures
					 			| http_google.es.png
				 	| url_list.txt
			 | .gitignore
			 | LICENSE
			 | README.md

``` 

* And will save a screenshot like the following one with the naming scheme ```PROTOCOL_ADDRESS_PORT.DOMAINEXTENSION.png```  
![Capture of the site http://google.es](https://raw.githubusercontent.com/30vh1/photographi/master/test/captures/http_google.es.png)

[chromedriver-url-linux]: https://chromedriver.storage.googleapis.com/index.html
[chromedriver-url-windows]: https://chromedriver.storage.googleapis.com/index.html  
[google-chrome-url-linux]: https://www.google.com/chrome/browser/desktop/index.html  
[google-chrome-url-windows]: https://www.google.com/chrome/browser/desktop/index.html  
