from setuptools import setup, find_packages

setup(
    name="advanced-calculator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'advanced-calculator=advanced_calculator.calculator_usage:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An advanced calculator with GUI interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="calculator, gui, mathematics",
    url="https://github.com/yourusername/advanced-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 