import subprocess
import os

co1 = "git add ."
co2 = "git commit -m 'adding module'"
co3 = "git push origin master"
os.popen(co1).read()
os.popen(co2).read()
os.popen(co3).read()
