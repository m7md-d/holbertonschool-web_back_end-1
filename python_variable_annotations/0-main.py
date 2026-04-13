#!/usr/bin/env python3
"""Run simple checks for the typed add function implementation."""

add = __import__("0-add").add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
