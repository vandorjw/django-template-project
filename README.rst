========================
django-template-project
========================


A project template for Django 1.5, based off django-twoscoops-project

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using this version of the django template.
#. Install additional dependencies
#. Create the project


Working Environment
===================
 
Virtualenv with virtualenvwrapper
--------------------------------

First we need to install pip. You can either choose to install pip from the repository, or from a tarbar.
Please note that Debian Wheezy ships with an older version of pip which does not check the validity of the packages downloaded.
Please replace X.X with the current-stable version number for pip.::

    $ curl -O https://pypi.python.org/packages/source/p/pip/pip-X.X.tar.gz
    $ tar xvfz pip-X.X.tar.gz
    $ cd pip-X.X
    $ sudo python setup.py install

Now that pip is installed, use it to grab virtualenv and virtualenvwrapper.::

    $ sudo pip install virtualenv virtualenvwrapper

I place my VirtualEnvironments under /var/virtualenvs/. By default it does not exist.
Create it, and give yourself write permission by running the following.::

    $ sudo mkdir /var/virtualenvs/
    $ sudo usermod -a -G adm YOURUSERNAME
    $ sudo chgrp -R adm /var/virtualenvs/
    $ sudo chmod -R g+w /var/virtualenvs/

Add the following to your .bashrc file if you have the same setup as myself.::

    export WORKON_HOME=/var/virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

!notice! log-out and log back in for the changes to take effect !notice!

We are now ready to create our virtual python environment.::

    $ mkvirtualenv your_domain_here
    $ pip install django
    
Notice the lack of 'sudo'. After creating the virtualenv, your shell should have changed to (your_domain_here) in front.
If this did not occur, try running::

    $ workon your_domain_here

I put my sites under /var/www. For example /var/www/domain.com/, /var/www/vandorjw.me/, etc
You will find a index.html file under /var/www by default.::

    $ sudo mkdir /var/www/default
    $ mv /var/www/index.html /var/www/default

    
I will post my apache config files on a later day.


Installing Django
=================

To install Django in the new virtual environment, see the section about "VirtualEnv"

Creating your project
=====================

To create a new Django project called '**MY_PROJECT**' using
django-template-project, run the following command::

    $ django-admin.py startproject --template=https://github.com/vandorjw/django-template-project/archive/master.zip --extension=py,rst,html MY_PROJECT

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*


Environment Variables
======================


A good idea. More info to be added later




Acknowledgements
================

    - Many thanks to Randall Degges for the inspiration to write the book and django-skel.
    - All of the contributors_ to this project.

.. _contributors: https://github.com/vandorjw/django-template-project/blob/master/CONTRIBUTORS.txt
