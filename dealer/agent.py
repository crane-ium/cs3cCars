"""
Agent object.
"""
import statistics
from datetime import datetime, timedelta
from data.agents import agents
from data import CARS
from dealer import COLUMNS, SPACING

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
        self.wait_minutes = []

    def __str__(self):
        """
        Creates a string to output for Agent object
        Puts it into a tabular format
        """
        output = ''
        for string in COLUMNS:
            output += string.ljust(SPACING)
        output += "\n"
        for agent in self.agent_list:
            deal_ratio = (str(agent['deals']).ljust(2)
                        + " of " 
                        + str(agent['deals_attempted']).ljust(2))
            bonus = "100000" if agent['bonus'] else "0"
            output += f"{agent['agent']['agent_id']:<{SPACING}}"
            output += f"{deal_ratio:<{SPACING}}"
            output += f"{agent['revenue']:<{SPACING}}"
            output += f"{agent['commission']:<{SPACING}}"
            output += f"{bonus:<{SPACING}}\n"
        output += f"{'-' * 10}Wait Time{'-' * 10}\n"
        output += f"Mean: {statistics.mean(self.wait_minutes):.4}\n"
        output += f"Median: {int(statistics.median(self.wait_minutes))}\n"
        output += f"Std deviation: {statistics.stdev(self.wait_minutes):.4}\n"
        return output
    
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
                self.wait_minutes.append(int(minutes))
            else:
                raise ValueError
            _time = soonest_agent['time'] + timedelta(
                    hours=soonest_agent['agent']['service_time'])
            soonest_agent = self.set_agent_time(soonest_agent,_time)
            return soonest_agent
        #Second, return the best available agent
        _customer_car = customer['interest']
        best_agent = max(available_agents, key=lambda k: k['agent']['expertise'][_customer_car])
        _time = customer['arrival_time'] + timedelta(
                hours=best_agent['agent']['service_time'])
        best_agent = self.set_agent_time(best_agent,_time)
        return best_agent

    def set_agent_time(self, agent, time):
        """
        Update the agent's time he's busy until
        """
        for index, agent_ in enumerate(self.agent_list):
            if agent_ == agent:
                self.agent_list[index]['time'] = time
                return self.agent_list[index]

    def check_deal(self,agent,customer):
        """
        Changes Agent's deal statistics according to the customer
        """ 
        if customer['sale_closed'] == True:        
            agent['commission'] += 10000
            agent['deals'] += 1
            agent['revenue'] += CARS[customer['interest']]['price']
            if agent['commission'] >= 100000:
                agent['bonus'] = True
        agent['deals_attempted'] += 1
        updated_agent = self.set_agent(agent)
        return updated_agent

    def set_agent(self,agent):
        """
        Updates the agent with most recent statistics
        """
        for index, agent_ in enumerate(self.agent_list):
            if agent['agent']['agent_id'] == agent_['agent']['agent_id']:
                self.agent_list[index] = agent
                return self.agent_list[index]
        raise IndexError

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
                'commission':0,
                'revenue':0,
                'bonus':False,
                'deals':0,
                'deals_attempted':0,
            })
        return agents_list
