Ghost on Openshift
##################

:date: 2013-12-31
:category: tutorial
:tags: troubleshooting, blogging, ghost, openshift
:slug: ghost-on-openshift

:summary: `Openshift <https://openshift.redhat.com>`_ is PAAS from redhat, `Ghost <https://ghost.org/>`_ is a new blogging platform built using node.js and supports writing the posts in Markdown format

Installing Ghost wasn't difficult at all, especially with all the `great documentation <https://www.openshift.com/quickstarts/ghost-on-openshift>`_ supplied by Openshift community

Email Setup
-----------
As soon as I did initial deployment, I got a notification that I need to fix the email configuration. I went with default setup using the Mailgun setup recommended by `the documentation <http://docs.ghost.org/mail/>`_

Theme Setup
-----------
Next thing was to change the default casper theme. This turned surprisingly difficult (here is where intuition that one builds due to the experience comes in handy .. more on that a little later)

As listed on the `ghost documentation <http://docs.ghost.org/themes/>`_ I went to the `marketplace gallary <http://marketplace.ghost.org/>`_ and liked Vapor and Ghostium themes.

I assumed (not completely incorrect though) that I need to clone the theme projects into ../content/themes folder, along side the casper folder that came by default. I did the same for both the themes.

Next thing was to "apply" these to my installation. After having these two theme folders, I thought all I needed was to restart the application using

.. code-block:: shell

   rhc app-restart appname


So I went the settings page, but no new themes .. Hmm ..

But I quickly realized that the way openshift deployments work (not unlike heroku, which I haven't used) is by pushing any changes to the git repo. So added both the theme folders to git (along with previous changes for the mail setup I did earlier.

Restarted the app

OK, now two new themes appeared in the drop down.
Selected one, clicked "Save", went on to the main page, and ...

.. code-block:: shell

   Failed to lookup view "index"

OK, so this theme may be bad, let me try another one. Same error. What could be wrong ?

Google search revealed that this errors shows up when index.hbs and post.hbs files are missing (They were not for either of the themes)

Luckily, I could go back to default casper theme. (But then I didn't like it so much, that is why I needed a different theme)

So I tried another theme from the forums. This one was available only as a zip file.. and guess what - this worked.

Hmm ..

One of the theme I chose was a "Featured" theme, so it can't have wrong code ..

I downloaded the ZIP file of the same repo from the github (contents would be same, except I won't be able to update the theme easily)
As suggested somewhere - I had also checked the file permissions (all were 644/rw-r--r--) same as in the ZIP file.

Intuition helps
---------------

I'm not sure what made me use the ZIP files (from github) in place of the cloned repo. The previous theme that worked may have something to do with it. 

I think it is intuition from troubleshooting various problems over the years.

But it worked. I got the zip file, and placed it at the same place, git commit/push/restart later, I was successfully able to apply the new theme.

I am still not sure what is the difference, may be I'll troubleshoot more, but that would be the topic for another post.

2013 ended with a Bang !!!

2014 will be equally fulfilling and challenging.

-----

*This article was originally published on the newly deployed ghost blog on openshift - Duh !! The reason to reproduce it here is because I haven't (yet) spent time to figure out if and how I can backup my posts. I've been bitten twice, so I am being careful. Plus this will remain my primary blog anyway, although publishing on Ghost was a pleasure, more on that later, in another post perhaps.*

*Since I used reStructuredText format instead of markdown for this blog, it took a little more effort than I had expected*