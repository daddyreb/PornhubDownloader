#!/usr/bin/env python
import re
from request import get_request
import sys


def get_help():
	print("""
Usage: porndown [options...] <url>
		""")


try:
	url_type = sys.argv[1]
	url = sys.argv[2]
except Exception as e:
	get_help()
