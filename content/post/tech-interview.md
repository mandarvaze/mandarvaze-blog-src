---
title: "Tech Interview"
date: 2018-11-01T08:10:49+05:30
tags:
- career
- funny
---

*These are actual exchanges from a technical interview I conduced recently. The
person had 2 years experience in an MNC, in what they described as DevOps*

<!--more-->

------

Me: You have mentioned "Troubleshooting problems on unix platform. Which
platforms have you worked on ?"

Candidate: Unix

Me: Which one ?

Candidate: SunOS. I think Solaris. It was UNIX.

------

Me: Why are you leaving this job ?

Candidate: I want to grow technically.

Me: What steps have you taken to do that.

Candidate: I learnt Django on my own. I created a small app. (*Goes on to
describe, album cover art, music file, songwriter etc.*)

Me: Which database did you use ?

Candidate: SQL

Me: Which one ?

Candidate: NoSQL

Me: Which one ?

Candidate: I don't remember. I think it was mongodb.

Me: Did you have to use any plugin, or was it supported "out of the box" (*From
what I remember, Django ORM does not support NoSQL, hence the question*)

Candidate: No plugin or extension

Me: ...

Candidate: I don't remember.

-----

Me: Can you explain kind of automation you did, as part of your job ?

Candidate: We have 100s of servers each with different authentication. We deploy
via ansible playbooks. We do not store the username password in the playbook.

Me: Since you mentioned 100s of servers, where do you keep all the auth details
? (*I expected them to say "Spreadsheet"*)

Candidate: It is stored in git

Me: ... (*Wha....*)

Me: Isn't this a security risk ?

Candidate: No, this repo has "read-only" permission.

Me: I hacker only needs to "read" the password, isn't it ?

Candidate: Only my team has access. Developers do not have access to this repo
at all.

------
