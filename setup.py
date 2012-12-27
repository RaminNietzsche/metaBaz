from distutils.core import setup
from setuptools import  find_packages

if __name__ == '__main__':

    setup(	
        name = "metaBaz",
        version = "0.0",
        author = "Ramin Najjarbashi",
        author_email = "Ramin.Najarbashi@gmail.com",
        #packages = find_packages() + ['lib'],
        package_dir = {'':'lib'},
        packages = [''],
        scripts=['bin/badtag'],
        description = "metaBaz is a script to remove images metatags ;)",
        license = "GPL",
        url = "http://RaminNietzsche.github.com/metaBaz",
 	keywords=['metatag','Persian','editor','python'],
 	data_files = [('share/doc/metabaz',['README', 'COPYING', 'CHANGES'])],
 	classifiers=[
 	'Development Status :: 0 - Beta',
 	'Intended Audience :: Persian Users',
 	'Intended Audience :: Persian Programmers',
	'License :: OSI Approved :: GNU General Public License v3',
 	'Operating System :: POSIX',
 	'Programming Language :: Python',
 	'Topic :: Editor',
 	'Topic :: Persian',
 	'Topic :: Meta Tags'
 	],    
    )


