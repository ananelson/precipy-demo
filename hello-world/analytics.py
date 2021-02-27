from datetime import datetime

def hello(af, x):
    return -1 * x

def make_a_file(af, name):
    for f in af.generate_file("%s.txt" % name):
        f.write("this file created at %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
