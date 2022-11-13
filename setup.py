import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_hello",
    version="0.0.1",
    author="Abhijeet Talele",
    author_email="abhijeet.talele@gmail.com",
    description="A function that returns 'hello Artifactory'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhijeettalele/python-hello",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'python_world@git+https://github.com/abhijeettalele/python_world#egg=python_world-0.0.1',
    ]
)