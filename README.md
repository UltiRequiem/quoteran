# quoteran

![CodeQL](https://github.com/UltiRequiem/quoteran/workflows/CodeQL/badge.svg)
![Pylint](https://github.com/UltiRequiem/quoteran/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/quoteran)](https://pypi.org/project/quoteran)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/quoteran?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/quoteran?color=blue&label=Total%20Lines)

Get random quotes in terminal.

This project fetch the [Quotable.io API](https://api.quotable.io/random).

![Screenshot](./assets/new_screenshot.png)

## Install

You can install [Quoteran](https://pypi.org/project/quteran) from PyPI:

```bash
pip install quoteran
```

To get the last version:

```bash
pip install git+https:/github.com/UltiRequiem/quoteran
```

If you use Linux, you may need to install this with sudo to
be able to access the command throughout your system.

## Usage

```bash
quoteran
```

### License

This project is Licensed under the [MIT](./LICENSE) License.

### Alternative

I also developed this in Nodejs: [UltiRequiem/ranmess](https://github.com/UltiRequiem/ranmess)

![Benchmark Screenshot](./assets/benchmark.png)

The version written in Nodejs is significantly faster,
and it was even easier to develop and publish than this.

**Update**: Thanks to [Poetry](https://python-poetry.org) now it's just as easy
to publish as an npm package, maybe a bit more.
