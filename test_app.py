from app import app

# Small change to trigger CI/CD pipeline

# Attempt to trigger pylint
def bad_code():
    

def test_get_message():
    with app.test_client() as client:
        response = client.get('/api/message')
        assert response.status_code == 200
        assert response.json == {'message': 'Hello from Flask!'}
