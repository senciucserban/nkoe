====
Nkoe
====

    Nkoe means tiger in `Sesotho`_ :tiger:

|python| |flake8| |poetry|

A basic `aiohttp`_ server which implement few endpoints. This project was made with educational purpose so those are some basic things.

About
-----
Here it's a `presentation`_ about what about what you can find in this repository.

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

Postman Setup
-------------
    I assume you already have installed and setup postman locally; **Note** I recommend to create a new workspace to avoid overwriting existing things!

For **collection**: Open postman and from left upper corner select ``import`` and then ``Import from link`` and put this link: https://www.getpostman.com/collections/33c1efb9969544146bf9.

For **environment**: In this repository you will find a folder named ``docs``. Open postman select from left upper corner ``import`` and then ``Import folder`` and just drag and drop that folder.

For **globals**: From right upper corner click on that ``eye``, go with mouse on globals row and press edit, in that table add a new row with: Variable = username, Initial value = [your name], Current Value = [leave it blank], and press **save**.

    For ``local`` environment I suppose you will run your server on port ``8080`` and for ``qa`` on port ``8081``.

Endpoints
---------
=====================================  ========  ============================================
  ENDPOINT                              METHOD                   DESCRIPTION
=====================================  ========  ============================================
  Base
---------------------------------------------------------------------------------------------
  ``.../``                               GET             overview :notebook:
  Auth
---------------------------------------------------------------------------------------------
  ``.../login/``                         POST          Create token :heavy_plus_sign:
  ``.../logout/``                        POST         Delete token :heavy_minus_sign:
  Cats
---------------------------------------------------------------------------------------------
  ``.../cats/``                         GET             Get all cats :smile_cat:
  ``.../cats/``                         POST         Create new cat :heart_eyes_cat:
  ``.../cats/{cat_pk}/``                GET          Get info for a specific cat :cat:
  ``.../cats/{cat_pk}/``                PUT        Update information about a cat :smirk_cat:
  ``.../cats/{cat_pk}/``                DELETE       Delete a cat :crying_cat_face:
  ``.../cats/{cat_pk}/vaccine``         POST        Add a vaccine to a cat :scream_cat:
=====================================  ========  ============================================

.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language
.. _Poetry: https://github.com/sdispater/poetry
.. _Postman: https://www.getpostman.com
.. _presentation: https://docs.google.com/presentation/d/1RbkpSnGvNpZUGb_rxZrdXsWu4NoraZtWeLaq7KSQMlg/edit
.. _aiohttp: https://aiohttp.readthedocs.io/en/stable/

.. |python| image:: https://img.shields.io/badge/python-3.7.x-blue.svg
    :alt: Python 3.7.x
.. |flake8| image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg
    :alt: Flake8
.. |poetry| image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg
    :alt: Poetry
