# PHOTO GALLERY

## Description
#### This is a web application that allows users to view photos. They can select them based on the location where the photo was taken or the category of the photo..
#### By **gkarumba**
The user can:
* See various photos
* View photos by location/category
* Copy link to the photo
* View image details
## Setup/Installation Requirements
### Prerequisites
*django2.2
* python3.6
* pip
* Virtual environment(virtualenv)

### Cloning and running
* Clone the application using git clone(this copies the app onto your device). In terminal:

          $ git clone https://github.com/gkarumba/Photo-Gallery.git
          $ cd Photo-Gallery

* Creating the virtual environment

          $ python3.6 -m venv --without-pip virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

          $ python3.6 -m pip install -r requirements.txt

* Run the application:
        
          $ python3 manage.py runserver  
          
### Testing the Application
* To run the tests for the class files:

          $ python3.6 manage.py test

## Technologies Used
* Python 3.6
* Django2.2
## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Display Photos | On page load | List of various photos taken |
| Display Photos Details | On click photo | List of photos details |
| Display Photos Based on Location | On location | List of photos taken on that location |
| Display Photos Based on Category | On search photo category | List of photos on that category |
| Copy photo link to clipboard | On click copy | Copy photo link |

## Support and contact details
For any questions, troubleshooting or contributions,  find me on:
* Email: gachegua@gmail.com
### License
MIT License
Copyright (c) {2019} (gkarumba)[https://github.com/gkarumba/Photo-Gallery/blob/master/LICENSE]
