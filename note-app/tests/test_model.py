import pytest
from bson import ObjectId
from mongomock import MongoClient
from src.models import get_notes, save_note, get_note_by_id, update_note_by_id, delete_note_by_id


class TestModels:
    @pytest.fixture(autouse=True)
    def setup_class(self, mocker):
        self.mock_client = MongoClient()
        self.mock_db = self.mock_client.db
        mocker.patch('src.models.mongo.db', self.mock_db)

    def test_get_notes(self):
        # Add test data
        self.mock_db.notes.insert_many([
            {"title": "Note 1", "description": "Desc 1", "createdAt": "2021-01-01"},
            {"title": "Note 2", "description": "Desc 2", "createdAt": "2021-01-02"}
        ])

        notes = list(get_notes())
        assert len(notes) == 2
        assert notes[0]['title'] == 'Note 2'  # Assuming the sort order is correct

    def test_save_note(self):
        save_note("Test Note", "Test Description", "2021-01-03")
        saved_note = self.mock_db.notes.find_one({"title": "Test Note"})
        assert saved_note is not None
        assert saved_note['description'] == "Test Description"

    def test_get_note_by_id(self):
        note_id = self.mock_db.notes.insert_one({"title": "New Note", "description": "New Desc"}).inserted_id
        note = get_note_by_id(str(note_id))
        assert note is not None
        assert note['title'] == "New Note"

    def test_update_note_by_id(self):
        note_id = self.mock_db.notes.insert_one({"title": "Old Title", "description": "Old Desc"}).inserted_id
        update_note_by_id(str(note_id), "Updated Title", "Updated Desc")
        updated_note = self.mock_db.notes.find_one({"_id": note_id})
        assert updated_note['title'] == "Updated Title"
        assert updated_note['description'] == "Updated Desc"

    def test_delete_note_by_id(self):
        note_id = self.mock_db.notes.insert_one({"title": "Note to Delete", "description": "Desc"}).inserted_id
        delete_note_by_id(str(note_id))
        deleted_note = self.mock_db.notes.find_one({"_id": note_id})
        assert deleted_note is None
