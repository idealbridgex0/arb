from setuptools import setup, find_packages

setup(
    name="arb_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ccxt==4.0.42",
        "colorama==0.4.6",
        "requests==2.31.0",
       " pytz==2023.3",
    ],
    entry_points={
        "console_scripts": [
            "arb_runner=arb_package.run:main",  # Optional CLI
        ],
    },
)
