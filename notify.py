#!/usr/bin/env python3

import smtplib
import ssl
import credentials


def email(content):
    replyto = credentials.replyto
    sendto = [credentials.sendto]
    subject = 'New IP Address'
    sendtoShow = 'raspberrypi@home'
    mailtext = 'From: '+replyto+'\nTo: '+sendtoShow+'\n'
    mailtext = mailtext+'Subject: '+subject+'\n'+content+'\n'

    s = smtplib.SMTP('smtp.gmail.com', 587)
    context = ssl.create_default_context()
    s.ehlo()
    s.starttls(context=context)
    s.ehlo()
    username = credentials.username
    password = credentials.password
    s.login(username, password)
    s.sendmail(replyto, sendto, mailtext)
    s.quit()
