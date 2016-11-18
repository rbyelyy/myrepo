from setuptools import setup, find_packages
from os.path import join, dirname
from setuptools.command.install import install
import os


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    version  = '0.11.1'
    def run(self):
        os.system("curl -O -L "
                  "https://github.com/mozilla/geckodriver/releases/download/v" + self.version +
                  "/geckodriver-v" + self.version + "-macos.tar.gz "
                  "&& tar -xvf geckodriver-v" + self.version + "-macos.tar.gz && "
                                                               "rm geckodriver-v" + self.version + "-macos.tar.gz")
        install.run(self)

setup(
    name='pom_example',
    description='Python POM example',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts':
            ['pom_example = pom_example.core:print_message']
    },
    install_requires=[
        'selenium', 'pytest'
    ]
)