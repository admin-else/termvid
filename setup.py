from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='termvid',
    version='0.1.0',
    packages=find_packages(),
    author='Admin Else',
    author_email='adman.else@gmail.com',
    description='a tool to play videos in the command line.',
    url='https://github.com/admin-else/termvid',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL-3 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'termvid=termvid:main'
        ],
    },
)
