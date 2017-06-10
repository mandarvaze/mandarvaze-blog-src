:title: How to use multiple versions of python at the same time
:slug: pynev-and-virtualenv
:date: 2017-06-10 20:34:24 UTC+05:30
:tags: python, micro
:category: TIL
:type: text

If you install python via the package manager for your OS (:code:`brew`,
:code:`apt-get`, :code:`yum`) you can have only one version of python at the
same time.

At best one python2 and one python3

But if you want to have (and want ability to easily switch between) say 3.5.2
and 3.6.0 (and 2.7.2) then you should definitely consider using :code:`pyenv`

:code:`pyenv` is not platform specific. It installs all the versions in your
home directory under :code:`~/.pyenv`

Some useful commands:

.. code-block:: shell

   pyenv versions  # Lists the various versions on your system
   pyenv install -l # Lists available versions you can install
   pyenv install 2.7.0 # Install Python 2.7.0


Off course there is lot more `on the pyenv page <https://github.com/pyenv/pyenv>`_

There is a :code:`pyenv` plugin that helps manager virual environments.
See `here <https://github.com/pyenv/pyenv-virtualenv/blob/master/README.md>`_

-------

*Cross-posted from my other* `blog <https://mandarvaze.bitbucket.io/>`_
