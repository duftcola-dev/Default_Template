
def test_factory(app):
    assert app is not None
    assert app.config["SECRET_KEY"] is not None 
    assert app.secret_key is not None

