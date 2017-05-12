#/usr/bin/env python
import os
 
def main():
PREFIX = '' if os.environ.get('PREFIX') is None else os.environ.get('PREFIX')
print(PREFIX)

if __name__ == '__main__':
   main()
