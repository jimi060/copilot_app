import unittest
from plugins.types.feat_observer import FeatObserver

class DummyFeatPlugin:
    name = "Dummy"
    @classmethod
    def apply(cls, context, result):
        result.setdefault("notes", []).append("Dummy feat applied")

class FeatObserverTestCase(unittest.TestCase):
    def test_register_and_notify(self):
        observer = FeatObserver()
        observer.register(DummyFeatPlugin)
        result = {"notes": []}
        observer.notify(["Dummy"], {}, result)
        self.assertIn("Dummy feat applied", result["notes"])

    def test_notify_with_no_registered_plugin(self):
        observer = FeatObserver()
        result = {"notes": []}
        observer.notify(["Nonexistent"], {}, result)
        self.assertEqual(result["notes"], [])

    def test_multiple_plugins(self):
        class AnotherFeatPlugin:
            name = "Another"
            @classmethod
            def apply(cls, context, result):
                result.setdefault("notes", []).append("Another feat applied")
        observer = FeatObserver()
        observer.register(DummyFeatPlugin)
        observer.register(AnotherFeatPlugin)
        result = {"notes": []}
        observer.notify(["Dummy", "Another"], {}, result)
        self.assertIn("Dummy feat applied", result["notes"])
        self.assertIn("Another feat applied", result["notes"])

if __name__ == "__main__":
    unittest.main()
