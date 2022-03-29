""" test the main menu and content pages"""
def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li><a class="dropdown-item" href="/page1">Git</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page2">Docker</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page3">Python</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page4">CI/CD</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page5">Glossary</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page6">AAA Testing</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page7">OOP</a></li>' in response.data
    assert b'<li><a class="dropdown-item" href="/page8">SOLID and Factory pattern</a></li>'\
           in response.data

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

def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"Glossary" in response.data

def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data

def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/badpage")
    assert response.status_code == 404
