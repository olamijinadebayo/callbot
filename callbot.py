import os
import phonenumbers
import time
import uuid
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

#setting up  the environment variables
BOT_ID = os.environ.get("BOT_ID")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

#constants
AT_BOT = "<@" + BOT_ID + ">:"
CALL_COMMAND = "call"
TWIMLET = "https://twimlets.com/echo?Twiml=%3CResponse%3E%0A%20%20%3CDial%3E%3CConference%3E{{name}}%3C%2FConference%3E%3C%2FDial%3E%0A%3C%2FResponse%3E&"


#instantiate Slack & Twilio clients
slack_client= SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
twilio_client = TwilioRestClient()

def handle_command(command,channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "not sure what you mean *" +\
                CALL_COMMAND + "* command with numbers, delimited by spaces."
    if command.startswith(CALL_COMMAND):
        response = 
    slack_client.api_call("chat.postMessage", channel= channel,text=response,as_user=True)

def parse_slack_output(slack_rtm_output):
    '''
    this  will get the commands directed at the bot and determines if they are valid commands.if
    they are directed at the bot it acts on the command else it returns back what it needs
    for the command to be verified
    '''
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(),\
                output['channel']

    return None,None

if __name__ =="__main__":
    READ_WEBSOCKET_DELAY = 1 # this will give a second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Callbot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID")
