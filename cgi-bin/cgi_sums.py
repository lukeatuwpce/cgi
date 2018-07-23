#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

try:
    total = sum(map(int, operands))
    body = f"Total: {total}"
except (ValueError, TypeError):
    body = "sum failed: provide integer operands."

print("Content-type: text/plain")
print()
print(body)
