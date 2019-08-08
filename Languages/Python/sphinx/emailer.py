"""
Description:
    A set of utilities to allow for sending emails with attachments easily through SMTP.
Testing:
    If you are testing the file assumes you're calling from root directory (..), to test\
    call the file by cd'ing out one directory and using: python utilities/emailer.py
Example:
    from emailer import send_mail()
    or for testing
    $ python utilities/emailer.py
TODO:
    * Password integration
"""

import getpass # For entering in passwords without terminal echo
import logging # Used for the logging of errors, and debuging info
import json,os # Used for path and file handling
import yagmail # Handles the majority of the heavy lifting for sending messages through SMTP



def import_smtp_from_json(path,test=False):
    """A helper function to set the SMTP configuration for send_email from a json file
    Args:
        test (bool): Indicates whether this is just a test run (True), or (False) in prod
        path (str): The path to the smtp configuration json file
    Returns:
        Tuple[str,str,str,str]: A tuple of configuration values (email to send from, smtp domain/host, port, recipients)
    """

    if test:
        print("loading SMTP settings")
        path = os.path.join("configuration","test", "smtp.json")

    with open(path, 'r') as smtp_config:
        config = json.load(smtp_config)

    logging.info("SMTP Configuration found:\n\tFrom Email: {}\n\tHost/Domain: {}\n\tPort: {}\n\tRecipients {}".format(config["sending_email"],
        config["host"],
        config["port"],
        config["send_to"]))

    return config["sending_email"], config["host"], config["port"], config["send_to"]


def configure_attachment(attachment_path):
    """A helper function for send_mail that properly configures attachments for sending
    Args:
        attachment_path (str): A string with path of an attachment
    Returns:
        Dict[str, str]: Properly formatted dictionary of attachments for use with yagmail
    """

    attachment = {}
    attachment[attachment_path] = os.path.basename(attachment_path)
    return attachment


def send_email(smtp_config_path="",
    subject="A test email from the emailer file",
    message="Hello World! \nI am a test email!",
    attachment=os.path.join("configuration", "test", "sema.png"),
    test=False):
    """Function to send email based on configuration provided in JSON file
    Args:
        smtp_config_path (str): Path to the SMTP configuration JSON file
        message (str): The body of the email, accepts inline HTML or string formatting
        attachment (str): Path to attachment, keep in mind this must have an extension
        test (bool): Indicates whether this is just a test run (True), or (False) in prod
    Returns:
        bool: True if email is sent without issues, if there is an issue returns False and logs+prints error
    """
    attachment = configure_attachment(attachment)

    if test:
        logging.debug("Prompting User for Password")
        smtp_config_path = os.path.join("configuration", "test", "smtp.json")
        # Manual password entry if doing a test
        passwd = getpass.getpass(prompt="Please enter configured emails' password: ", stream=None) 

    logging.info("Begin SMTP configuration parsing on: " + smtp_config_path)
    from_email, smtp_domain, port, recipients = import_smtp_from_json(smtp_config_path) # Import variables from file


    logging.info("Beginning SMTP connection")
    # Connect to smtp server
    yag_smtp_connection = yagmail.SMTP(user=from_email, password=passwd, port=port, host=smtp_domain) 

    contents = [message, attachment] # Create list of content to send in email

    print("Preparing to send email")
    logging.info("Preparing to send email \n\tRecipients: {} \n\tSubject: {} \n\tContents: {}".format(recipients,
        subject,
        contents))
    try:
        yag_smtp_connection.send(recipients, subject, contents) # send the email
        logging.info("Email sent successfully")
        print("Email sent successfully")
        return True

    except Exception as identifier:
        logging.error("Error occurred during sending, see below for details\n" + identifier)
        return False


if __name__ == "__main__":
    logging.basicConfig(filename='emailer.log', level=logging.DEBUG)
    print("Loading config settings")
    send_email(test=True)