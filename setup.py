from setuptools import setup, find_packages

version = __import__('signedforms').__version__

setup(
    name = 'django-signedforms',
    version = version,
    description = 'A signed Django form',
    author = 'Benjamin Wohlwend',
    author_email = 'benjamin.wohlwend@divio.ch',
    url = 'http://github.com/piquadrat/django-signedforms',
    packages = find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>1.3',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
)
