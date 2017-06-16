===============================================
Writing Pelican blog post using Nikola new_post
===============================================

:type: text
:slug: writing-pelican-blog-post-using-nikola-new_post
:date: 2017-06-16 20:53:49 UTC+05:30
:tags: blogging, nikola
:category: misc

In my `last post
<{filename}./support-for-pelican-style-metadata-format-in-nikola.rst>`_, I
mentioned that Nikola can use the pelican/resT docinfo style metadata.

I had also mentioned that, now can I use the same post in both the places
without any change. But if I used nikola's :code:`new_post` command, the
metadata generated would be in "reST comments" style, which would work only for
Nikola.

That means, I needed to modify the metadata, before I can use the exact same
post at both the places. This wasn't too much effort, yet it involved additional
efforts.

Just days later, Nikola released another minor version, and here they have added
functionality that :code:`new_post` would generate the skeleton in the correct
format, based on the configuration setting.

In my particular case, I have added the following like to :code:`conf.py`

.. code-block:: python

   METADATA_FORMAT = "Pelican"

For more details see `documentation
<https://getnikola.com/handbook.html#metadata-formats>`_

Currently for this format, only limited metadata headers are generated : Title
(reST style), :code:`type`, :code:`slug` and :code:`date`

The "default" on the other hand have a lot more headers like :code:`tags`,
:code:`category` and more (which I don't use)

So it would be nice if all the metadata headers were generated.

The way Nikola is making improvements, who knows, this functionality might just
be available in the next release

------

*In case it is not clear, I have done exactly what the title says.*
