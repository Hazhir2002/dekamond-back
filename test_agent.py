import unittest
from main import build_agent


class TestAIAgent(unittest.TestCase):

    def test_summary_output(self):
        agent = build_agent()

        input_data = {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 600, "customers": 50},
        }

        result = agent.invoke({"input_data": input_data})
        summary = result["summary"]

        self.assertIn("profit", summary)
        self.assertIsInstance(summary["alerts"], list)
        self.assertIsInstance(summary["recommendations"], list)
        self.assertGreaterEqual(len(summary["recommendations"]), 1)


if __name__ == "__main__":
    unittest.main()
