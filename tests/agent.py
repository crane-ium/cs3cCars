"""
Unit tests for agent module.
"""
import unittest
import copy
from data.agents import *
from data.customers import *
from dealer.agent import *

class TestAgent(unittest.TestCase):
    """
    Tests for agent.
    """

    def setUp(self):
        pass
    def testAgents(self):
        agents = create_agents_list(5)
        self.assertEqual(len(agents),5)
        self.assertEqual(len(agents[0].items()),4)
    def testCustomers(self):
        customers = create_customers_list(100)
        self.assertEqual(len(customers),100)
        self.assertEqual(len(customers[0].items()),3)
    def testAgent(self):
        agents = Agent.create_agents_list(5)
        self.assertEqual(len(agents),5)
        self.assertEqual(len(agents[0].items()),7)
        self.assertEqual(len(agents[0]['agent'].items()),4)
    def testGetAgent(self):
        agents = Agent(5)
        customers = create_customers_list(100)
        print("Testing get agent")
        print(customers[0])
        best_agent = agents.get_agent(customers[0])
        # print(best_agent)
        self.assertIn(best_agent,agents.agent_list,msg='best_agent not in agent_list')
    def testSetAgentTime(self):
        agents = Agent(1)
        customer = create_customers_list(1)
        print(f"\nOriginal time: {agents.agent_list[0]['time']}")
        today = datetime.today()
        agents.set_agent_time(agents.agent_list[0],datetime(today.year,today.month,today.day,12))
        print(f"New time {agents.agent_list[0]['time']}")
        agent = agents.get_agent(customer[0])
        arrival_time = customer[0]['arrival_time']
        print(arrival_time)
        print(f"Newest time {agents.agent_list[0]['time']}")
        self.assertEqual(agent['agent'],agents.agent_list[0]['agent'])
    def testCheckDeal(self):
        agents = Agent(5)
        agents_copy = copy.deepcopy(agents)
        customers = create_customers_list(100)
        current_agent = agents.get_agent(customers[0])
        updated_agent = agents.check_deal(current_agent, customers[0])
        self.assertIn(updated_agent,agents.agent_list)
    def testStr(self):
        agents = Agent(5)
        self.assertIsInstance(str(agents),str)

if __name__ == "__main__":
    unittest.main()
