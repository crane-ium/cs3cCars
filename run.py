"""
Car sales.
"""
from datetime import datetime
from dealer.agent import Agent
from data.customers import customers,create_customers_list

class Run(object):
    """
    Run the sales.
    """
    agent_list = Agent(5)
    customers_ = create_customers_list(100)

    def sales(self):
        """
    Loop through customers to determine how the agents did.
    Alter the agents object
    """
    for index, customer in enumerate(customers_):
        agent_list.get_agent(customer)
        #Alter the original list to reflect current agent availability
        for agent in agent_list:
            if best_agent == agent:
                agent['time'] = customer['arrival_time'] + timedelta(hours=agent['agent']['service_time'])
                break
        else:
            raise IndexError


    def print_(self):
        pass
        


if __name__ == "__main__":
    run = Run()
    run.sales()
    run.print_()