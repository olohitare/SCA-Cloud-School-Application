import platform
import subprocess
import argparse
import sys

from shutil import which

#Creates the parser
my_parser = argparse.ArgumentParser(prog='install-cli', description='CLI for installing three applications')

#Add the arguements
my_parser.add_argument('Application', choices=['wget', 'node', 'curl'], type=str, help='Install the specified application')

#execute the parsed_args() method
args = my_parser.parse_args()

#extract the app that is to be installed
app = args.Application

def install_app(app):
    print(f"Commencing Installation of {app}")
    os = platform.system()
    if os == 'Linux':
        c = f'apt install {app}'
        subprocess.call(c, shell=True)
    elif os == 'Darwin':
        c = f'brew install {app}'
        subprocess.call(c, shell=True)
    elif os == 'Windows':
        c = f'apt install {app}'
        subprocess.call(c, shell=True)
    print(f'{app} has been installed on your computer')

def check_app_installed(app):
    if which(app) is not None:
        print(f'{app} is already installed')
        sys.exit()
    else:
        install_app(app)

check_app_installed(app)

# def main():
#     applications = [
#         'wget',
#         'curl',
#         'node'
#     ]

#     for app in applications:
#         # Check if installed
#         if is_installed(app):
#             print(f'{app} is already installed.')

#             continue



#     return


# def is_installed(name):
#     return which(name) is not None


# main()
