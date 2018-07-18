"""
Unit tests for agent module.
"""
import unittest
from data.agents import *

class TestAgent(unittest.TestCase):
    """
    Tests for agent.
    """

    def setUp(self):
        pass
    def testAgents(self):
        agents = create_agents_list(10)
        self.assertEqual(len(agents),10)
        self.assertEqual(len(agents[0].items()),4)


if __name__ == "__main__":
    unittest.main()
