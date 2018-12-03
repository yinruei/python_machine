import sys
try:
    f = open('mysql.pyo')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OSError: {0}",format(err))
except ValueError:
    print("could not convert data to an integer.")
except:
    print("unexpected error:", sys.exc_info()[0])