def test_example(client):
    response = client.get('/')
    assert response.status_code == 200

def test_hello(client):
    response = client.get('/')
    assert b'<h2>Hello World!</h2>' in response.data
