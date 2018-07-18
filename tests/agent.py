"""
Unit tests for agent module.
"""
import unittest
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
        agents = createAgentsList(5)
        self.assertEqual(len(agents),5)
        self.assertEqual(len(agents[0].items()),4)
    def testCustomers(self):
        customers = createCustomersList(100)
        self.assertEqual(len(customers),100)
        self.assertEqual(len(customers[0].items()),3)
    def testAgent(self):
        agents = Agent.createAgentsList(5)
        self.assertEqual(len(agents),5)
        self.assertEqual(len(agents[0].items()),3)
        self.assertEqual(len(agents[0]['agent'].items()),4)
    


if __name__ == "__main__":
    unittest.main()
