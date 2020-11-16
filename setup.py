import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='i-posty',
    version='1.0.0',
    author='Ivan Zlatanov',
    author_email='i_zlatanov@protonmail.com',
    description='A lightweight command-line link shortening tool for Linux.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/not-so-cool-anymore/posty/',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'posty = posty.posty:main' 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0'   
)