import os

a=str(os.system('pip list'))

if 'github-contents' not in a:
    os.system('pip install github-contents')

if 'keyboard' not in a:
    os.system('pip install keyboard')
