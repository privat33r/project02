#!/usr/bin/python3

#Created:29Mar19 Author:
#Description: Handles logins from index.html, perform input validation and updates database

import mysql.connector #library for database being used
from mysql.connector import errorcode #  allows you to check and handle errors
import config
import sys
import re
import cgi
import cgitb; cgitb.enable()
from helper import End # neat way of ending the page
import hashlib

from inputClass import Input #this is to escape characters when dealing with user inputs
