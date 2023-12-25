"""
This file contains code for the application "google-palm-cli".
Author: GlobalCreativeApkDev
"""


# Importing necessary libraries


import google.generativeai as palm
import os
from dotenv import load_dotenv


# Creating main function used to run the application.


def main() -> int:
    """
    This main function is used to run the application.
    :return: an integer
    """

    load_dotenv()
    palm.configure(api_key=os.environ['PALM_API_KEY'])

    response = palm.chat(messages="Hi there! How can I help you?")
    print(response.last)

    while True:
        prompt = input("User: ")
        if prompt == "":
            return 0
        response = response.reply(prompt)
        print("AI: " + str(response.last))


if __name__ == '__main__':
    main()
