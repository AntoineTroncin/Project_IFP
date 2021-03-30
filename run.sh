#!/bin/sh

if [ -f "/Project_IFP/myprojectenvir"  ] ; then
             source "myprojectenvir/bin/activate"
             python main.py
     else
	     virtualenv env
	     env/bin/pip freeze > requirements.txt
	     env/bin/pip install -r requirements.txt
	     python main.py

fi
