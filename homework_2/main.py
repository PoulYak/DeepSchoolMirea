from tests import test_sanity_check, test_more_ops
try:
    test_sanity_check()
    print("First test passed")
except:
    print("Error in first test")

try:
    test_more_ops()
    print("Second test passed")
except:
    print("Error in second test")
