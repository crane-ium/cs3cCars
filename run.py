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

    def sales(self):
        """
        Loop through customers to determine how the agents did.
        Alter the agents object
        """
        agent_list = Agent(5)
        customers_ = create_customers_list(100)
        for customer in customers_:
            agent = agent_list.get_agent(customer)
            agent_list.check_deal(agent,customer)
        print(__name__)
        print(agent_list)
        


if __name__ == "__main__":
    run = Run()
    run.sales()