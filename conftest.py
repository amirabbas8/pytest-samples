from test_8repr import Foo
# sys.dont_write_bytecode = True


def pytest_report_header(config):
    return "---------------Salam Salam-----------------"


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "webtest: mark test to run in web server"
    )


# command controlls for test discovery and management
