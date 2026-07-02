import os
import pytest
import app as app_module
import models

@pytest.fixture
def client(monkeypatch):
    test_db = "test_tasks.db"
    monkeypatch.setattr(models, "DB_NAME", test_db)
    models.init_db()

    app_module.app.config['TESTING'] = True
    test_client = app_module.app.test_client()

    yield test_client

    if os.path.exists(test_db):
        os.remove(test_db)