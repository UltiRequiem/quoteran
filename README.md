# quoteran

![CodeQL](https://github.com/UltiRequiem/quoteran/workflows/CodeQL/badge.svg)
![Pylint](https://github.com/UltiRequiem/quoteran/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/quoteran)](https://pypi.org/project/quoteran)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/quoteran?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/quoteran?color=blue&label=Total%20Lines)

Get random quotes in terminal.

This project fetches random quotes from a [Quotable](https://github.com/lukePeavey/quotable) API server.

## Use your own API server

The public `api.quotable.io` host is no longer available, so point quoteran at a Quotable server you run (the
project is open source). The base URL is read, in this order, from:

1. the `--api-url` flag,
2. the `QUOTABLE_API_URL` environment variable,
3. the public default, `https://api.quotable.io`.

Give the server address only, without `/random` (a path prefix such as `https://example.com/quotes-api` is fine).

![Screenshot](https://raw.githubusercontent.com/UltiRequiem/quoteran/main/assets/new_screenshot.png)

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
QUOTABLE_API_URL=https://quotes.example.com quoteran
quoteran --api-url https://quotes.example.com
```

### License

This project is Licensed under the [MIT](./LICENSE) License.

### Alternative

I also developed this in Nodejs: [UltiRequiem/ranmess](https://github.com/UltiRequiem/ranmess)

![Benchmark Screenshot](https://raw.githubusercontent.com/UltiRequiem/quoteran/main/assets/benchmark.png)

The version written in Nodejs is significantly faster,
and it was even easier to develop and publish than this.

**Update**: Thanks to [Poetry](https://python-poetry.org) now it's just as easy
to publish as an npm package, maybe a bit more.
