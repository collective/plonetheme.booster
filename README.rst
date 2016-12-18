.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
Booster
==============================================================================

Booster is a clean and elegant free Plone Theme that is suitable for landing pages and other related businesses.

.. image:: https://github.com/collective/plonetheme.booster/blob/master/src/preview.png?raw=true

See additional screenshots below.

Installation
------------

Zip
~~~~~~~~
In zip version you don't get the slider but only a static banner due to limitations.

#. Download the `zip file`_
#. Import the theme from the Diazo theme control panel.

Buildout
~~~~~~~~

Install ``plonetheme.booster`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonetheme.booster


and then running ``bin/buildout``

Documentation
-------------

Full documentation for end users can be found `here`_

Contribution
-------------

- Clone the repo.
- Run ``bin/buildout``
- next, install the local dependencies theme requires
    ``$ npm install``
- Watch For Changes & Automatically Refresh
    ``$ grunt watch``
- Build & Optimize(This will create a ``dist`` folder with optimized files and a zip of theme)
    ``$ grunt dist``

License
-------

MIT License

Credit
------

Based on `Booster`_ Provided by `FREEHTML5.co`_

.. _zip file: https://github.com/collective/plonetheme.booster/blob/master/plonetheme.booster.zip?raw=true
.. _Booster: https://freehtml5.co/booster-free-html5-bootstrap-template/
.. _FREEHTML5.co: https://freehtml5.co/
.. _here: https://github.com/collective/plonetheme.booster/blob/master/docs/index.rst

Screenshots
-----------

Full size screenshot:

.. image:: https://raw.githubusercontent.com/collective/plonetheme.booster/master/docs/plonetheme.booster-screenshot.jpg

iPhone Plus screenshot:

.. image:: https://raw.githubusercontent.com/collective/plonetheme.booster/master/docs/plonetheme.booster-screenshot-iphone-plus.jpg
