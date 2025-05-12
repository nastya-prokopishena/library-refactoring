from app.config import MongoConnection


def test_singleton_same_instance():
    conn1 = MongoConnection()
    conn2 = MongoConnection()
    assert conn1 is conn2  


def test_singleton_has_client_and_db():
    conn = MongoConnection()
    assert conn.client is not None
    assert conn.db.name == "library_db"


def test_singleton_db_same_across_instances():
    conn1 = MongoConnection()
    conn2 = MongoConnection()
    assert conn1.db is conn2.db
