#!/bin/bash

# Ignoring autogenerated files
#  -- Migration directories
# Ignoring error codes
#  -- E128 continuation line under-indented for visual indent
#  -- E402 module level import not at top of file
#  -- E501 line too long

pycodestyle --exclude=build,migrations,.tox --ignore=E128,E402,E501 .
