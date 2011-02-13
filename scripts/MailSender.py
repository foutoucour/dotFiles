#!/usr/bin/python


import os
import sys
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

class MailSender:
    """
    """
    def setServer(self, sServer):
        self.sServer = sServer

    def setPort(self, iPort):
        self.iPort = iPort

    def setFrom(self, sFrom):
        self.sFrom = sFrom

    def setTo(self, sTo):
        self.sTo = sTo

    def setSubject(self, sSubject):
        self.sSubject = sSubject

    def setText(self, sText):
        self.sText = sText

    def setMessage(self):
        """
        Formating the message.
        """
        return """\
From: %s
To: %s
Subject: %s

%s
""" % (self.sFrom, self.sTo, self.sSubject, self.sText)

    def sendEmail(self):
        self.createMailServer()
        self.email()
        self.closeServer()
        self.success()

    def createMailServer(self):
        self.oServer = smtplib.SMTP(self.sServer,
                                     self.iPort)

    def email(self):
        self.oServer.sendmail(self.sUser,
                              self.sTo,
                              self.setMessage())

    def closeServer(self):
        self.oServer.close()

    def success(self):
        print ('sent to %s' %self.sTo)


class SecuredMailSender(MailSender):
    """
    """
    def __init__(self, sUser, sPassword):
        self.sUser = sUser
        self.sFrom = sUser
        self.sPassword = sPassword

    def sendEmail(self):
        self.createMailServer()
        self.oServer.ehlo()
        self.oServer.starttls()
        self.oServer.ehlo()
        self.oServer.login(self.sUser, self.sPassword)
        self.email()
        self.success()
        self.closeServer()
        self.closeServer()


class GMailSender(SecuredMailSender):
    """
    Class to send a message from my gmail account.
    """
    def __init__(self):
        SecuredMailSender.__init__('kender.jr@gmail.com',
                                   'Foo')
        self.setServer('smtp.gmail.com')
        self.setPort(587)


def getAttachment(attachmentFilePath):
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)
    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'
    mainType, subType = contentType.split('/', 1)
    file = open(attachmentFilePath, 'rb')
    if mainType == 'text':
        attachment = MIMEText(file.read())
    elif mainType == 'message':
        attachment = email.message_from_file(file)
    elif mainType == 'image':
        attachment = MIMEImage(file.read(),_subType=subType)
    elif mainType == 'audio':
        attachment = MIMEAudio(file.read(),_subType=subType)
    else:
        attachment = MIMEBase(mainType, subType)
    attachment.set_payload(file.read())
    encode_base64(attachment)
    file.close()
    attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))
    return attachment


