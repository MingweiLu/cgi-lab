#!/usr/bin/env python3
import imp
import os
import json

# PRINT OUT ALL ENV VARIABLES AS PLAIN TEXT
# print("Content-Type: text/plain")
# print()
# print(os.environ)

#PRINT ENV VARIABLES AS JSON
# print("Content-Tpye: application/json")#let browser lnow to expect json
# print()
# print(json.dumps(dict(os.environ), indent=2)) #print w/ nice foormatting!

#PRINT QUERY PARANETER DATA IN HTML
print("Content-Type: text/html") #let browser know to expect html
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
