"""
Agent object.
"""
from datetime import datetime, timedelta
from data.agents import agents
from data.customers import customers
from data import CARS

AGENT_COUNT = 5

class Agent(object):
    """
    Object that holds agents and returns the agent for the customer
    """

    def __init__(self, agent_count: int):
        """
        Create a list of n agents
        For this project it SHOULD be 5 agents
        """
        self.agent_list = Agent.create_agents_list(agent_count)
        self.wait_minutes = 0

    def __str__(self):
        """
        Creates a string to output for Agent object
        Puts it into a tabular format
        """
        pass

    def __getitem__(self, index):
        """
        Return an agent dictionary from agent_list index
        """
        def __str__(self):
            """
            Returns tabular format of agents
            """
            pass
        pass

    def __iter__(self):
        """
        Instead of accessing agents by index through __getitem__, you can iterate through
        the agents
        """
        pass
    
    def get_agent(self,customer):
        """
        Outputs the best agent based on the customer
        """
        #First test availability, and if none, return nearest agent
        available_agents = list(filter(lambda x: x['time'] <= customer['arrival_time'], self.agent_list))
        if not available_agents:
            soonest_agent = min(self.agent_list,key=lambda k: k['time'])
            minutes = (soonest_agent['time'] - customer['arrival_time']).total_seconds() / 60
            if minutes > 0: #Which should always be true at this point
                self.wait_minutes += minutes
            else:
                raise ValueError
            _time = soonest_agent['time'] + timedelta(
                    hours=soonest_agent['agent']['service_time'])
            self.set_agent_time(soonest_agent,_time)
            return soonest_agent
        #Second, return the best available agent
        _customer_car = customer['interest']
        best_agent = max(available_agents, key=lambda k: k['agent']['expertise'][_customer_car])
        _time = customer['arrival_time'] + timedelta(
                hours=best_agent['agent']['service_time'])
        self.set_agent_time(best_agent,_time)
        return best_agent

    def set_agent_time(self, agent, time):
        """
        Update the agent's time he's busy until
        """
        for index, agent_ in enumerate(self.agent_list):
            if agent_ == agent:
                self.agent_list[index]['time'] = time
                break


    @classmethod
    def get(cls, customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        # """
        # best_agent = None
        # #First find best agent, and if none, go next step
        # best_agent = max(cls.agent_list,)
        # #Second, find the soonest agent for the customer
        pass

    @staticmethod
    def create_agents_list(count: int):
        """
        Creates and returns a list of a dictionary
        -"agent":Holds the agent's dictionary (info)
        -'time':Holds the agent's (date)time that he's still busy. 
                If the time is in the past, he's not busy
        -'deals':Holds total deals earned  (10k per closed deal)
        -'revenue': revenue from each car sold
        """
        agents_list = []
        _today = datetime.today()
        for agent in agents(count):
            agents_list.append({
                'agent':agent,
                'time': datetime(_today.year, _today.month, _today.day, 8),
                'deals':0,
                'revenue':0,
            })
        return agents_list

