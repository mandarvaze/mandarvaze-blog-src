:title: Support for pelican style metadata format in nikola
:slug: support-for-pelican-style-metadata-format-in-nikola
:date: 2017-06-11 05:24:58 UTC+05:30
:tags: nikola
:category: misc

Few years ago, python.__init__ podcast had invited creators of two most popular
static site generators written in python i.e. `pelican
<http://getpelican.com/>`_ and `nikola <http://getnikola.com/>`_

In that episode, they were asked why do these two SSGs have different meta data
format (aka front matter). While I don't remember "why" but Roberto Alsina of
Nikola had suggested that he would support other metadata formats for better
compatibility.

This was back in 2015.

Fast forward to 2017.

Nikola has delivered on that promise.

Latest `version <https://github.com/getnikola/nikola/releases/tag/v7.8.7>`_ of
nikola now supports pelican style among other formats. It also supports YAML and
TOML style front matters used by other non-pythonic SSGs like Hugo and Jekyll

This is a BIG deal.

This allows me to easily share the same source between variety of SSGs without
having to port the posts.

I can easily cross-post the exact same content between pelican and nikola, like
I just `did <http://mandarvaze.github.io/2017/06/pynev-and-virtualenv.html>`_
(See footer)

I can "move" from nikola to hugo (which I have been thinking about a lot, since
Hugo has lot of nicer themes. Nikola - not so much) I can continue to use
nikola, but use YAML/TOML style front matter, and one day BOOM, just run hugo
compiler to generate the entire site in hugo. Off course, this is easier said
than done. But at least there won't be any "porting"

I can use tools like :code:`nikola new_post` across the SSGs. In fact I just did
that for **this** post. pelican doesn't have such command, AFAIK, so created the
skeleton using nikola's new_post command, moved over the generated file to
pelican blog area, and started writing.
