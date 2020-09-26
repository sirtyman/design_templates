from setuptools import setup, find_packages


setup(
    name='design_templates',
    version='1.0.0',
    url='https://github.com/sirtyman/design_templates.git',
    author='Marcin Tyman',
    author_email='marcin.tyman@gmail.com',
    description='Templates and documentation generated base on autodoc',
    packages=find_packages(),
    install_requires=['sphinx', 'recommonmark'],
)
