#!/usr/bin/python

import os
import sys
sys.path.append( os.path.dirname( os.path.realpath( __file__ ) ) )


import MailSender
reload(MailSender)

class CGSM_MailSender(MailSender.MailSender):
    def __init__(self):
        MailSender.MailSender.__init__(self)
        self.setFrom("contact@CGStudiomap.com")
        self.setServer("")

class AssistanceCampagn(MailSender.GMailSender):
    def __init__(self):
        MailSender.GMailSender.__init__(self)
        self.setSubject("CGStudioMap needs your assistance.")
        self.setText("""
Hello,

CGStudioMap is close to a new step in giving assistance to job seekers.
After giving a tool to find easily a place to work at all around the world, the team wants now to work on the other side of the coin.

Our aim of last months was to think about how to help you again but this time with spreading informations about employees, so we worked on the main tool of recruitment :
the Resume and how to set the perfect template for our field.

We got the technology for it but we need to be sure to answer all your needs.
For that, we would need your feedbacks about resumes you already filled in other websites, like LinkedIn, Monsters, CreativeHeads., etc...

What did you miss from these resumes ?
What would you except from a resume template dictated to CG industry ?

By giving us your needs, you will help us to build resumes that will be your best help to find a job.

Regards,
CGStudioMap Team.

--
- Jordi Riera
-- Public Relation - CGStudioMap ( http://www.CGStudioMap.com )""")


if __name__ == '__main__':
    AC = AssistanceCampagn()
    listTo = ['kender.jr@gmail.com',
              'c1max@hotmail.com'
             ]

    for element in listTo:
        AC.setTo(element)
        AC.sendEmail()

