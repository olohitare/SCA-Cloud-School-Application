import platform
import subprocess

from shutil import which


def main():
    applications = [
        'wget',
        'curl',
        'node'
    ]

    for app in applications:
        # Check if installed
        if is_installed(app):
            print(f'{app} is already installed.')

            continue

        os = platform.system
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

    return


def is_installed(name):
    return which(name) is not None


main()
