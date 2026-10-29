import pytest
from main import InventoryInspector

@pytest.fixture
def inspector():
    return InventoryInspector(threshold=0.80)

def test_passed_item(inspector):
    item = {"item_id": "TEST-001", "score": 0.90, "density": 2.5}
    status = inspector.inspect_item(item)
    assert status == "PASSED"
    assert inspector.passed_items == 1

def test_defective_item(inspector):
    item = {"item_id": "TEST-002", "score": 0.65, "density": 1.2}
    status = inspector.inspect_item(item)
    assert "REJECTED" in status
    assert inspector.defective_items == 1

def test_yield_summary(inspector):
    inspector.inspect_item({"item_id": "TEST-003", "score": 0.95, "density": 2.0})
    summary = inspector.generate_summary()
    assert summary["Total Processed"] == 1
    assert summary["Yield Rate"] == "100.00%"
