from distutils.core import setup
from ranquote.version import __version__

setup(
    name="ranquote",
    version=__version__,
    description="Random quotes on Terminal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/ranquote",
    license="MIT",
    scripts=["./bin/ranquote"],
    packages=["ranquote"],
    install_requires=["requests==2.25.1"],
)
