'''
Helper functions common to all Spin components
'''

import json

# Formats inline styling for components
# <h1 {style("font-family: Avenir;"}>Hello World</h1>
def style(style):
  return "style='{}'".format(style.replace("\n", "").replace(" ", ""))

def load_cms(path):
  return json.load(open(path))