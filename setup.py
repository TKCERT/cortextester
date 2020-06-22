from setuptools import setup
import os.path

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        with open(filepath, 'r') as fh:
            return fh.read()
    except IOError:
        return ''

setup(
    name='cortextester',
    version='0.0.5',
    description='A set of Python tools for testing and validation of Cortex analyzers and responders',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='thyssenkrupp CERT',
    author_email='tkag-cert@thyssenkrupp.com',
    license='AGPL-V3',
    url='https://github.com/TKCERT/cortextester',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    py_modules=[
        'cortextester.analyzer.config',
        'cortextester.analyzer.input',
        'cortextester.analyzer.output',
        'cortextester.analyzer.schema',
        'cortextester.pipe',
        'cortextester.responder.config',
        'cortextester.responder.input',
        'cortextester.responder.output',
        'cortextester.responder.schema',
        'cortextester.schema',
    ],
    entry_points = {
        'console_scripts': [
            'analyzer-config=cortextester.analyzer.config:main',
            'analyzer-input=cortextester.analyzer.input:main',
            'analyzer-output=cortextester.analyzer.output:main',
            'responder-config=cortextester.responder.config:main',
            'responder-input=cortextester.responder.input:main',
            'responder-output=cortextester.responder.output:main',
        ]
    },
    install_requires=read_file('requirements.txt').splitlines(),
    include_package_data=True,
)
