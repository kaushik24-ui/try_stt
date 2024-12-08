import setuptools

setuptools.setup(
    name='try_stt',  # Use a valid package name, avoid using <> or other special characters
    version='0.1',
    author="Kaushik",  # Remove the angle brackets
    author_email="kaushikyadavm857@gmail.com",  # Ensure proper email format
    description="This code is for speech to text created by me",  # Proper description format
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
