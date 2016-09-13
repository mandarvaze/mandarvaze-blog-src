xonsh : python-ish BASHward looking shell
#########################################

:slug: xonsh-python-shell
:date: 2016-08-29 Mon 09:30
:category: explore
:tags: python, shell
:author: Mandar Vaze

.. contents::


Getting started
---------------

Easiest way to get started on Mac is :

``brew install xonsh``

This installed older version than one released. It was good to try ``xonsh`` for
the first time. But the documentation was **newer** than the software (imagine
that) So I removed it.

But in the process it installed python 3.5.1 (as a dependency) I still have
python 3.4.2 from earlier brew installation, but now it was "orphan"

Problem
-------

Now that I had python 3.5.1. as my default python, it caused a bit of problem,
(it felt like a big problem in the beginning) since lot of stuff that was
installed on 3.4 was not available anymore.

Main problem was virtualenvwrapper - which had references in my ``.zshrc`` but
"new" python site packages did not have it installed.

So I had to

.. code-block:: bash

    pip3 install virtualenv
    pip3 install virtualenvwrapper

Now virtualenvwrapper errors went away.

Getting started .. again
------------------------

Since ``brew`` had older version, I decided to use ``pip`` instead

.. code-block:: bash

    pip3 install xonsh
    $ xonsh --version
    xonsh/0.4.4

Next step was configuring ``xonsh`` via the wizard.

When I had run ``xonfig wizard`` earlier, I had selected a few of the *xontribs*
but they were not installed, so when I started ``xonsh`` I got ``ImportWarning``

It would be good if the wizard offered only the xontribs that are available,
better still, offer to invoke ``pip`` to install the missing xontribs that user
has selected to use. Off course, xonsh team is aware of this.

Anyway, way to install these are via pip.

.. code-block:: bash

    pip3 install xonsh-autoxsh
    pip3 install xontrib-avox
    pip3 install xontrib-prompt-ret-code

Better Prompt
-------------

Default toolkit (Is that the right term?) used by ``xonsh`` is ``gnureadlines``
but the alternative is way superior.


.. code-block:: bash

    pip3 install prompt_toolkit

Now my prompt was pimped "up" - nice autocompletions ala ``fish`` (I forgot to
mention that I had ``brew install bash-completion`` earlier) But I got an error
that ``pygments`` was missing, so

.. code-block:: bash

    pip3 install pygments

Now all is well :)

Some tips
---------

Colour Style
^^^^^^^^^^^^

Now that I got a nicer shell, ensure that you set the color style of your
choice.

``xonfig styles`` will all the "themes" available.

I started with ``monokai`` since I use it elsewhere as well. But trying new
theme is as simple as changing the variable name is **running** ``xonsh`` shell
!!!!

.. code-block:: python

   $XONSH_COLOR_STYLE='native'

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

If you have seen the pycon 2016 `video
<https://www.youtube.com/watch?v=uaje5I22kgE>`_, about xonsh or read the
documentation throughly you probably know about ``${...}``

This command lists all the environment variables

For useful environment variables, see http://xon.sh/envvars.html

History
^^^^^^^

The documentation boasts of rich history, but
I had problem related to ``history`` command not working

In the process, I upgraded to version ``0.4.5`` where there were several history
related fixes/improvements. But the problem did not go away. But there **is** a
workaround. See the details and the workaround `here
<https://github.com/xonsh/xonsh/issues/1577#issuecomment-240600295>`_

See update_.

Concluding thoughts
-------------------

I am still not ready to make ``xonsh`` my default shell (yet) There are certain
problems that prevent me from switching, but out of (say) 10 terminal tabs I
have open, at least 8 are running ``xonsh`` - That is not bad :)

I encourage you to try ``xonsh`` especially if you are python developer. I'm
sure you will **not** be disappointed.

------

.. _update:

*Update: Sept 13, 2016*
xonsh version ``0.4.6`` prevents this problem by not allowing to
overwrite the built-in aliases like ``history`` and ``ls``
