import unittest
from tool import snapshot


class SnapshotTests(unittest.TestCase):
    def test_is_order_independent_for_identical_records(self):
        first = snapshot([{"id": "b", "x": 2}, {"id": "a", "x": 1}])
        second = snapshot([{"id": "a", "x": 1}, {"id": "b", "x": 2}])
        self.assertEqual(first["sha256"], second["sha256"])
        self.assertEqual(first["records"][0]["id"], "a")


if __name__ == "__main__":
    unittest.main()
