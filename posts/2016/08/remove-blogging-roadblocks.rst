6 things to make (my) blogging frictionless
###########################################

:slug: easier-blogging
:date: 2016-08-23 Tue 05:18
:category: thoughts
:tags: blogging
:author: Mandar Vaze

.. contents::


.. note:: These issues apply to **me**. If you find some of these useful, great.
          The post is not intended as an advice to **you**.


Background
----------

Recently I heard the talk python to me podcast where A. Jesse Davis was
interviewed. The topic was a bit different than usual python related topics. It
was about how to make blogging easy. Jesse talks about several nice things,
including the fact that why we should **not** feel guilty for not blogging
regularly.

You should listen to the podcast
`here <https://talkpython.fm/episodes/show/69/write-an-excellent-programming-blog>`_
if you have not.

So the idea was at the back of my mind for a while, and this post is sort of
brain dump of why I am unable to **publish** regularly inspite of having content
written.


Finalize the source format
--------------------------

I kept moving between ``org`` and ``rst``. I liked ``org`` when I started using
emacs. (In fact that was **the** reason to start using emacs) So few of my
initial posts are in ``org`` I had one post in ``asciidoc`` as well. But I think
I will stick to reStructuredText mainly because most of the static site
generators will have support for this format.

Even bigger number probably support ``markdown`` but then there is no
standardization, you have too many flavors out there. Also, I think ``rst`` is
bit more *richer* than ``markdown``

I had one post in ``asciidoc`` as well

Create/Use templates
--------------------

In order to get the thoughts on paper (so to speak) I start typing in an empty
file. By the time I am done, I have very unformatted text that requires
"formatting", and this is where the delay in "publishing" comes in.
I have so many written-but-unpublished posts.

Having templates with headers and categories/tags pre-populated would be good
way to reduce the friction. Jesse talks about how we mostly have about 5
different types of posts. May be create just 5 templates for 5 "types" of blogs,
and remove the decision making from choosing the categories and tags. (I never
remember the list of categories and tags I have used, and always have to search
the older posts to get the list, sorta)

On second thoughts, I think nikola already has a script to create a new posts.
May be I ought to use that ?

Write more frequently
---------------------

This may seem confusing. Let me explain. As I mentioned that I usually start
writing as a plain text, and later "format" the contents. One of reasons why
this happens is because I can't remember the syntax at the time of writing. (and
that happens when one keeps switching between ``org`` to ``rst`` to ``md``. See
the first point.)

If I write more often using only one platform, the "formatting" syntax will be
part of my memory. I already write the documentation (using sphinx) in ``rst`` -
another reason to finalize on ``rst`` over ``org`` or ``md``

Finalize the blogging platform
------------------------------

I have one blog in pelican. (This one. updated after a long time) and `other
blog <http://mandarvaze.bitbucket.io>`_ in nikola. Switching between them just
takes mental effort. If I were to standardize on it, there won't be "switching
trouble"

I also want to consider ``hugo``, but my initial attempts to get a blog rolling
with a theme-that-i-like hasn't worked well.

But irrespective of the blog generator, if I standardize on reStructuredText, I
don't have to worry about switching the blog generators (I think)

Finalize the blog home
======================

On a related note, having single home for my blogs also might be good idea. It
is always an effort to decide where should a specific post go. While with my
second blog, the idea is very clear - it is about "what I learnt", so things
like "thoughts" should not go there. Yet, sometimes it is not easy. May be just
have one blog with category as "wiltw" (short for "What I learnt this week")


Focus on the content
--------------------

I am never happy with the themes. I was almost happy with Material Design theme
for nikola, but it could not render bullets (can you imagine?) So I switched to
a simpler theme. But I am not happy.

But I should just pick one up, stick with it, and not worry about the "look"

I have read several great blogs that look down right ugly, but the contents are
worth in gold.


Publish now, refine later
-------------------------

Perfectionist in me wants to read-edit-read a LOT after my initial writing is
done. I spend a lot of time in this. May be I should just publish it first, and
then refine it.
