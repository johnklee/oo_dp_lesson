def pytest_configure(config):
    marker_list = ["container", "network", "image"]

    for m in marker_list:
        config.addinivalue_line("markers", m)
