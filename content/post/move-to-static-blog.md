---
title: "Why I moved to Static Blog ?"
date: 2013-04-18
categories:
- meta
tags:
- blogging
coverImage: "https://source.unsplash.com//1CrN-IbvtH0/750x350"
coverSize: "partial"
---
Little bit of a histoy of my blog at various platforms.
<!--more-->

This is my third attempt at blogging.

### Wordpress.com

[First](http://mandarvaze.wordpress.com) one is still on hosted
wordpress site. In a way, that is nice. Pretty much no administration
needed. One can install the plugins that are tested by wordpress.com
They also upgrade the platform for you. Great for testing the waters for
the first time blogger. I think it is better than blogspot (*I can't
remember if I had one of those, and moved to wordpress*)

### Self-hosted Wordpress

But after a while one (*at least, I*) becomes ambitious. I had my own
wordpress blog hosted on my own domain. It was a great experience. I got
to try my hands at setting my blog *just the way I want*. But after
initial excitement was over, it started to become burden. One had to
spend a lot more time administering the blog (upgrade to latest version
of wordpress, and the plugins) and less focus on writing. I never
upgrade the blog to wordpress 3 (*which by now is very mature*) I always
kept postponing it because upgrade might *break* things, so I would do
it when I have enough time.

Unfortunately, after a while I wasn't writing much, and stopped paying
attention to the blog. I had also used my *non-standard* email ID with
the hosting provider.

The cascading effect was recently I lost access to my blog and the
domain. It was completely my fault. My hosting provider did send
multiple reminders for renewal, but I wasn't checking that account
often enough, and when I finally did, they had probably given up. (*I
did contact them later, but they ignored my emails*)

But I definitely learnt a lot.

### Posterous

Then while I still had my self-hosted wordpress blog, along came
posterous. What I liked about them was I could post via email. I really
liked the concept. They didn't great themes like wordpress, but if the
focus was writing, then it shouldn't matter.

.... and then they were acquired by twitter. As everyone had predicted,
twitter shut them down.

This was kinda the last straw. I had two blows back to back (One was my
own fault, other not so much) But the result was in both cases, I had
lost access to my blog.

### Finally, Static website ...

This was the time, static website generators were picking up. Over at
[HN](https://news.ycombinator.com/) I came across several options like
[Octopress](http://octopress.org/),
[Jekyll](https://github.com/mojombo/jekyll),
[Pelican](https://github.com/getpelican) . (*I chose Pelican because it
is written in Python, language which I am comfortable with, as opposed
to Jekyll and Octopress.*)

It is easy to host the static website anywhere, include the Free Heroku
plan (Which I might do in future) But hosting it on github seemed like
an easy and popular choice.

BTW, I did get a backup of all my posterous posts, but they were in XML
format. Format which was not useful to me as-it-is. There is a ruby
script that "downloads" all your posterous posts and converts them to
markdown. It was not without problems, but it worked. But it is a topic
for another post.

### Securing the source

Based on my recent experience, I am aware that github might one fine day
decide to stop supporting this feature. But if they did, that is OK too,
because I will still have access to my contents in the [git
repo](https://github.com/mandarvaze/mandarvaze-blog-src) in the form of
"source code" With Pelican I can re-generate the pages, and host it
someplace else (like Heroku)

What if github shuts down (or makes all accounts paid, or bought over my
big company, and the parent company shuts it down, whatever..) I have
already thought of contingency plan for that as well. I push the same
"code" to [bitbucket
repo](https://bitbucket.org/mandarvaze/mandarvaze-blog-src) as well.

While I think chances of both github **and** bitbucket going away at the
same time are slim to none, One can always have the copy of local git
repo in the dropbox folder, for additional security, Can you not ? :)

---------

*Photo by [Gareth Davis](https://unsplash.com/@gdfoto)*
