#!/usr/bin/env python
from flask import Flask
import subprocess

app = Flask(__name__)
@app.route("/disk")

def hello():
  cmd = ["df","-lh"]
  p = subprocess.Popen(cmd,
			stdout = subprocess.PIPE,
			stderr = subprocess.PIPE,
			stdin = subprocess.PIPE)
  out,err = p.communicate()
  return out
if __name__ == '__main__':
  app.run(host='0.0.0.0')

