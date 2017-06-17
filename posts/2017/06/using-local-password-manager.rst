:title: Using local password manager
:slug: using-local-password-manager
:date: 2017-06-17 12:57:48 UTC+05:30
:tags: security, gpg, gpg2, password, how-to
:category: tutorial
:type: text

Bit of history
--------------

Long time ago I was using LastPass. and it worked well for me for a long time,
till it was acquired. I heard some "bad" things, which honestly I do not
remember, but it was probably like the "free" option will go away.

I started looking for options, and chanced upon Dashlane.

Honestly it worked really well, but there is this inkling that I can't explain,
that I need to move out.

I tried KeePass - but honestly, it just doesn't compare. It is a just a storage.
Without ability to autofill the login pages, it is just too cumbersome.

I've been hearing great things about `pass <https://www.passwordstore.org/>`_

I had tried it earlier in Feb 2017, but the companion browser addons did not
work (at that time) So I went back to Dashlane (I never stopped)

Import the data from Dashlane
-----------------------------

One of the issue was I wanted to import my existing data from Dashlane to
:code:`pass`. But this is **not** natively supported. (For various valid
reasons) But there was an importer that worked with KeePass2 CSV file.

This is a python script - very well written - I might add.

It clearly documents the columns.

Dashlane has "unsecure" export option, which exports the passwords in "normal"
CSV file.

The sequence of the columns required by the importer wasn't far off.

I manually fixed this issue, and populated the title column.

Upgrade. Issues
---------------

Since my :code:`pass` was old, I decided to upgrade. Bunch of extensions also
required relatively newer version.

.. code-block:: shell

   brew upgrade pass

This upgraded :code:`gpg` as well. Warning says "backup ~/.gnupg"

.. code-block:: shell

   mv .gnupg .gnupg.back

Now that :code:`.gnupg` was backed up, time to use the upgraded software.

.. code-block:: shell

    brew link --overwrite gnupg
    pass init <PassStore Key>
    python keepass2csv2pass.py dashlane-new.csv

Most import failed because there was no gpg key

So ..

.. code-block:: shell

   gpg2 --full-generate-key

Now :code:`python keepass2csv2pass.py dashlane-new.csv` worked.

confirm using

.. code-block:: shell

   pass about.me

Autofill aka Integration with the Browser
-----------------------------------------

But :code:`pass` is a command line tool. It is just a backend for storage and
retrieval for the data.

For autofill, there is  `browserpass <https://github.com/dannyvankooten/browserpass>`_

There is some bug, which prevents autofill from working.

The workaround was to unlock the passstore using :code:`pass` command from the
terminal first. I was asked for the passphrase interactively in the terminal.

Once it was "unlocked", I had to (re) start firefox from the terminal using
:code:`open -a firefox`

As of this writing, see this open bugs related to gpg passphrase:

* Firefox doesn't show gpg passphrase dialog `#87 <https://github.com/dannyvankooten/browserpass/issues/87>`_
* Firefox doesn't show gpg passphrase dialog `#23 <https://github.com/dannyvankooten/browserpass/issues/23>`_
* `Unable to install chrome extension <https://github.com/dannyvankooten/browserpass/issues/80>`_

Keep the passstore up to date
-----------------------------

One time import is never enough when switching password manager. Ability to update existing entries and creating new ones is equally important.

:code:`pass` falls short here.

Inserting new entry is not easy as using Dashlane (which is very well integrated
with the browser)

But "extension" are supposed to take care of that. There is already a `feature
request <https://github.com/dannyvankooten/browserpass/issues/24>`_ on the
browserpass

None the less, here is how you do it.

.. code-block:: shell

   pass insert group/username
   Enter password for group/username:
   Retype password for group/username:


I had a bit of a problem, since I had imported my old GPG keys from gpg1 to gpg2

When I used :code:`pass insert` for the first time I saw the following error:

.. code-block:: shell

   There is no assurance this key belongs to the named user

Since the working has changed a LOT (use of trustdb, as opposed to secring) I
need to explicitly trust the imported keys.

The way to do this is "edit" the key and set the trust level explicitly.

.. code-block:: shell

   # Get the list of keys
   gpg2 --list-keys
   # Edit the key(s) you just imported
   gpg2 --edit-key <KEYID>
   # When asked, choose the trust level (5) being maximum, called ultimate
   # confirm with "y"

-------

On a related note, `KeePassXC <https://keepassxc.org/>`_, along with `PassIFox
<https://addons.mozilla.org/en-us/firefox/addon/passifox/>`_ looks promising.
I'm waiting for `this <https://github.com/pfn/passifox/issues/634>`_ issue to be
fixed so that I can continue to enable multiprocess support in Firefox.

-------

*Cross-posted from my other* `blog <https://mandarvaze.bitbucket.io/>`_
