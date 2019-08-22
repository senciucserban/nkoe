=================
Nkoe core package
=================

    Nkoe means tiger in `Sesotho`_ :tiger:

|python| |flake8| |poetry|

A basic `aiohttp` server which implement few endpoints. This project was made with educational purpose so those are some basic things.

Installation
------------
First you need some tools:
    1. A dependency manager: `Poetry`_.
    2. For presentation you will need `Postman`_ to perform requests.

Installation:
    1. Clone project locally;
    2. Install dependencies with ``poetry install``;
    3. Take a look at ``.example.env`` to see if you must configure something;
    4. Now run server with the following command: ``poetry run server``;

.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language
.. _Poetry: https://github.com/sdispater/poetry
.. _Postman: https://www.getpostman.com

.. |python| image:: https://img.shields.io/badge/python-3.7.x-blue.svg
    :alt: Python 3.7.x
.. |flake8| image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg
    :alt: Flake8
.. |poetry| image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg
    :alt: Poetry
