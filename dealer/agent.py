"""
Agent object.
"""
from data.agents import *
from data.customers import *
from data import CARS
from datetime import datetime

class Agent(object):
    """
    Car sales agent.
    """
    def __init__(self, agents_count):
        """
        Create a list of n agents
        For this project it SHOULD be 5 agents
        """
        self.agent_list = createAgentsList(agents_count)

    def __str__(self):
        """
        Creates a string to output for Agent object
        Puts it into a tabular format
        """
        pass
    
    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """
        pass
    @staticmethod
    def createAgentsList(count):
        """
        Creates and returns a list of a dictionary
        -"agent":Holds the agent's dictionary (info)
        -'time':Holds the agent's (date)time that he's still busy. If the time is in the past, he's not busy
        -'deals':Holds total deals earned  (10k per closed deal)
        -'revenue': revenue from each car sold
        """
        agents_list = []
        today = datetime.today()
        for agent in agents(count):
            agents_list.append({
                'agent':agent,
                'time': datetime(today.year, today.month, today.day, 8)
                'deals':0
                'revenue':0
            })
        return agents_list

