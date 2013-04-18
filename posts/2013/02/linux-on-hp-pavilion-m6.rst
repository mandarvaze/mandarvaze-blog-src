Installing linux on HP Pavilion m6
##################################

:date: 2013-02-17
:tags: linux, how-to, hp-m6
:category: tutorial
:slug: linux-on-hp-pavilion-m6
:author: Mandar Vaze
:summary: Main problem that needs solving is that machine comes preinstalled with four partitions, thus not allowing to create a new partition to boot from.

After my trusty? Lenovo Thinkpad R400 developed problems (immediately after the 3 year warranty expired) I had to buy a new laptop. After initially thinking of ultrabook, I finally bought HP Pavilion m6.

Since I needed this laptop for my work, I needed linux on it. I had *tried* a live USB on linux mint 13 before I paid for the machine, so I was sure that linux support would not be an issue. Live boot confirmed that display and Wireless worked without problems.

Before I decided to make changes, I created the rescue disk (Just to be safe) I ended up needing those not long after :( - By the way, as an aside, it is important to note that rescue disk creator program does **not** accept DVR+RW the ones that can be used to write multiple times. So I had to go back to the shop to get them replaced.

The main problem is that the machine already has 4 primary partitions. Thus linux installer is unable to create a new partition to boot from.
After looking thru forums, I realized that HP_tools partition can be easily removed. Way to do is :

1. First assign a drive letter to HP_TOOLS partition 
2. Copy the files to recovery partition
3. Delete the HP_TOOLS partition - 
4. Recreate if needed, recreated as logical - thus solving max primary partitions problem.

Once the max partition problem is resolved, installing linux isn't difficult.

One other thing I did differently was to use Windows boot loader as default instead of GRUB (Felt safe at the time) I used EasyBCD_ 
So now I first get Windows bootloader which lets me choose between windows and Linux mint 14 (which is the default) But once I select Linux mint, I get GRUB bootloader (which also consists on Windows 7 entry) So may be I didn't need EasyBCD_ after all. YMMV.



.. _EasyBCD: http://neosmart.net/EasyBCD/
