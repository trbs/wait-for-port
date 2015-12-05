
def test_import():
    import wait_for_port
    assert hasattr(wait_for_port, 'wait_for_port')

    import wait_for_port.main
    assert hasattr(wait_for_port.main, 'main')
