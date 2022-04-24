#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def generate_paragraph(dir):
    contents = ""

    files = os.listdir(dir)
    for filename in files:
        path = os.path.join(dir, filename)
        with open(path, 'r') as f:
            lines = f.readlines().strip()
            sentence = "name: {}<br/>weight: {}<br/><br/>".format(lines[0], lines[1])
            contents+=sentence

    return contents

if __name__ == "__main__":
    desc_dir = 'supplier-data/descriptions'
    attachment = '/tmp/processed.pdf'

    title = "Processed Update on {}".format(datetime.datetime.now().date())
    paragraph = generate_paragraph(desc_dir)

    reports.generate_reports(attachment, title, paragraph)

    # Send email
    sender = "automation@example.com"
    recipient = "student-03-5a1f1d893fce@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    msg = emails.generate_email(sender, recipient, subject, body, attachment_path=attachment)
    emails.send(msg)