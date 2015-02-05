How to convert posterous blog to Markdown
#########################################

:date: 2013-04-23
:category: tutorial
:tags: how-to, ruby, learning
:slug: posterous-to-markdown

:summary: This post should be helpful (if only for next few days) for those who want to *save* their posterous blogs.


.. contents::
..
   1  Option 1
   2  Option 2
   3  Fun Begins
   4  Modifying posterous gem
   5  Getting the images
   6  This is just the beginning


As I have written in a previous_ post, I recently consolidated all of various blogs into this one.
Big one was posterous, especially because it is going away in a few days time, and I had two separate blogs (spaces as they used to call it) with them.
While the other posts talked about *why* this one talks about *How*

Option 1
--------
Posterous provides a backup of all your articles, in XML format. while initially I thought this format may not be useful for importing into pelican, looking back, it might be. I haven't tried it, so I don't know whether it helps. For more details  refer to the `pelican documentation`_
Hopefully this is easier of the two routes.

Option 2
--------

First you need to "get" your postreous posts from their server to your local machine.
You can use this original_ script.

I had to make some changes_ to the script, to make it work for me. I suggest you keep both of them handy.
*I am not a ruby developer. so my changes are rudimentary, not the way ruby developer would do. But based on the logic, some old style debugging, and stackover help for ruby syntax, I was able to get it to work.*

Fun Begins
----------

For the script to work, you need (ruby off course) posterous "gem". Consider this as a library or a package, if you aren't familair with Ruby.
not being a ruby programmer, I didn't know this, so I got the following error:

.. code-block:: bash

   $ sudo gem install posterous
   [sudo] password for mandar:
   Fetching: ffi-1.7.0.gem (100%)
   Building native extensions.  This could take a while...
   ERROR:  Error installing posterous:
       ERROR: Failed to build gem native extension.

       /usr/bin/ruby1.9.1 extconf.rb
    /usr/lib/ruby/1.9.1/rubygems/custom_require.rb:36:in `require': cannot load such file -- mkmf (LoadError)
	from /usr/lib/ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
	from extconf.rb:4:in `<main>'

    Gem files will remain installed in /var/lib/gems/1.9.1/gems/ffi-1.7.0 for inspection.
    Results logged to /var/lib/gems/1.9.1/gems/ffi-1.7.0/ext/ffi_c/gem_make.out


Some googline revealed that this is a know problem which can be fixed by

.. code-block:: bash

   sudo apt-get install ruby1.9.1-dev

Now I was successfully able to install the posterous gem.

Modifying posterous gem
-----------------------

Original error went away, the script moved forward till the next error.

.. code-block:: bash

   The option: username is invalid. (Ethon::Errors::InvalidOption)
   Please try userpwd instead of username.

Found the workaround_ on github posterous gem issues list

Now that initial problem went away, I started getting the problems in the script itself. Good thing was I learnt debugging_ ruby script via printf method.
Realized there was problem w/ save_media. So at first I commented this function call, and then eveything was OK. I successfuly downloaded all my posts from one of the blogs.

Getting the images
------------------

Now that I was partially successful, I wanted to make sure I get the images as well. So I added further debug/printf like statements, and in the process learnt about "if my_object.nil? " idiom_
With that I was able to get the images as well from my second blog. (and then another pass at my first blog, with images)

This is just the beginning
--------------------------

Now that you have your posts from posterous secured, the "deadline" pressure of posterous going away on April 30th, 2013 is removed. But I coulnd't just use the converted files as is.

#. Markdown files didn't work with pelican directly, even after installing Markdown python module in my virtual environment. I ran into this_ error. (*BTW, you should totally boormark the article on which the comment is made*) So I *hand converted* the md files to rst. It didn't take that long, but was a manual process.
#. Links from posterous don't work, especially for images that were uploaded to posterous. These links point to posterous' own Amazon S3 (which will also go away soon) But you have the images downloaded by the ruby script, so all the links need to be fixed (manually)
#. I also did some editing. Not all my posts were moved. e.g. One of my posts "Why posterous rocks" didn't make it to this blog :)

I am still learning the rst and pelican, so reference to local images folder works "partially" Luckily, most other places, I was already referring to third party image URL, so it didn't matter.


.. _previous: http://mandarvaze.github.io/2013/04/why-move-to-static-blog.html
.. _pelican documentation : http://docs.getpelican.com/en/3.1.1/importer.html
.. _original : https://github.com/bmann/posterous-export/blob/master/posterous-export.rb
.. _changes : https://github.com/mandarvaze/posterous-export/blob/master/posterous-export.rb
.. _workaround : https://github.com/posterous/posterous-gem/issues/5#issuecomment-13539354
.. _debugging : http://stackoverflow.com/questions/3955688/how-do-i-debug-ruby-scripts
.. _idiom : http://lukaszwrobel.pl/blog/ruby-is-nil
.. _this : http://martinbrochhaus.com/2012/02/pelican.html#comment-726961261
