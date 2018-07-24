"""
Car sales.
"""
from dealer.agent import Agent
from data.customers import create_customers_list

class Run(object):
    """
    Run the sales.
    """

    def sales(self):
        """
        Loop through customers to determine how the agents did.
        """
        agent_num = 5
        customer_num = 100
        agents = Agent(agent_num)
        customers_ = create_customers_list(customer_num)
        for customer in customers_:
            agent = agents.get_agent(customer)
            agents.check_deal(agent, customer)
        print(agents)
        print(agents.wait_minutes)


if __name__ == "__main__":
    run = Run()
    run.sales()
    