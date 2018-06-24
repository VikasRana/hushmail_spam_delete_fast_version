# hushmail_spam_delete_fast_version
A better version of my old script - https://github.com/VikasRana/hushmail_spam_delete

A simple Python script that uses Selenium WEBDriver to delete the spams from Hushmail.com Inbox

You all know how Hushmail manages our spam reports against emails. We continously see spam mails getting landing in our inboxes. For this, I've designed this simple script so that I can go and make myself a cup of coffee while the script does it's job.

This script uses Selenium WEBDriver. And it can be installed easily, pip install selenium -U

You need to change certain field before you can run the script.

In line 9, usr = '' ; put your email id within quotes

In line 10, pss = '' ; put your password within quotes

In line 45, assert assert_string2.text == ''; put your username in quotes that you see on the top right of the page in BOLD

In line 61, spam = ["", ""]; add spammers here within double quotes

To run the script: python hush_fast_spam_del.py
