# Copyright (c) 2018 Hinojosa, Daniel <dhinojosa@evolutionnext.com>
# Author: Hinojosa, Daniel <dhinojosa@evolutionnext.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


name = 'Albert Einstein'
age = 76

# To do an interpolation, surround the string with a backtick.
# It can be interpolated in the string with a surrounding {}
# replaces the values from what is in the context */

print(f'His name was {name} and he lived until he was {age}')

# If there is a method that needs to be called or some kind of
# You can place that inside the braces.

print(f'His name was {name[::-1]} and he lived until he was {age + 1}')
