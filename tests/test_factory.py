from app import App 

def test_config():
    print("Testing ")
    assert App().init_app() != None
