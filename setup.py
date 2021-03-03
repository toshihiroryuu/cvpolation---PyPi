import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvpolation", # Replace with your own username
    version="1.0.2",
    author="Athul Mathew Konoor",
    author_email="athulmathewkonoor@gmail.com",
    description="A package to get perform different interpolation techniques on an Image.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toshihiroryuu/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "prettytable >= 2.1.0", "Pillow >=8.1.1"
   ],
    python_requires='>=3.6',
)