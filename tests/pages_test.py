def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/page1" class="nav-link">Git</a>' in response.data
    assert b'<a href="/page2" class="nav-link">Docker</a>' in response.data
    assert b'<a href="/page3" class="nav-link">Python</a>' in response.data
    assert b'<a href="/page4" class="nav-link">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"About me" in response.data



def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python 3.10." in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404