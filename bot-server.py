from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from bot_server_channel import BotServerInputChannel


import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer,
    BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from train import HospitalPolicy

# Creating the Interpreter and Agent
def load_agent():
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    #if serve_forever:
    #   agent.handle_channel(ConsoleInputChannel())
    return agent

# Creating the server
def main_server():
    agent = load_agent()
    channel = BotServerInputChannel(agent)
    agent.handle_channel(channel)

main_server()