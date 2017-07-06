:title: Sending Rich Text emails with mu4e
:date: 2017-07-03 19:32:07 UTC+05:30
:tags: emacs, how-to
:category: tutorial
:slug: sending-rich-text-emails-with-mu4e
:modified: Thu Jul 6 11:22:38 2017

.. contents::

Rich text in emails
-------------------

I recently started using :code:`mu4e` exclusively for emails. I haven't opened
the browser based email client in more than a week.

I almost never use "rich text" emails, so I didn't miss sending "rich" emails much.

But sometimes it is nice (useful?) to make certain word(s) bold for the impact.

and if one is using "rich text", marking code/commands in fixed width font is always nice.
I always used to manually change the font in such cases, when using browser based email client.

Since my needs were relatively low, using org-mode's mark-up was sufficient.

How
---

To quickly summarize, how I was able to do that, here are the steps :

(Note : My keybindings are spacemacs default. They may be different for you)

* Start new email using "C"
* After entering to/subject etc, and switching to body section, do :code:`org-mu4e-compose-org-mode`
* Write email using org mode. When done, :code:`org-mime-htmlize`
* Switch to headers area (This may not be needed, but I read reports somewhere that attempting to send email when in "body" part leads to some errors)
* Send using :code:`C-c C-c`

Trouble
-------

During my first few "Test" emails, I (naturally) tried bullets, sub-bullets
(like one expects to have in an org file)

This caused emails with TOC, and section numbers. It might be OK (even
desirable) when exporting an org-mode file to HTML file. But in an email, that
looks "odd"

Solution
--------

This was easily cured by adding :code:`#+OPTIONS: toc:nil num:nil` to the "email body"

But I don't want to (remember to) add this each time I want "rich text" email.

So these were created as global (?) settings in my :code:`.spacemacs` file as follows :

.. code:: elisp

  (setq org-export-with-section-numbers nil)
  (setq org-export-with-toc nil)

You can read about other export related settings `here <http://orgmode.org/manual/Export-settings.html#Export-settings>`_

Another problem
---------------

I did run into a little problem (still unresolved as of this writing)
See `this <https://www.reddit.com/r/emacs/comments/6ldthb/bug_in_exporting_source_block_from_orgmode_to_html/>`_ reddit thread

Partial Solution
----------------

*Update : July 6th, 2017*

I found a workaround, that "works for me, for now"

Instead of :code:`#+BEGIN_SRC` if I use :code:`#+BEGIN_EXAMPLE` - I don't get "bad characters"

Off course, no syntax highlighting, but at least for my use cases - I didn't need it

More over, if I were using standard browser-based email client, I do not get syntax highlighting any way.

The email (bodies) were never meant to share "code snippets"

-------

*Cross-posted from my other* `blog <https://mandarvaze.bitbucket.io/>`_
