from bson import ObjectId

from . import mongo


def get_notes():
    notes = mongo.db.notes.find({}).sort("createdAt", -1)
    return notes


def save_note(title, description, createdAt):
    # save the record to the database
    mongo.db.notes.insert_one({"title": title, "description": description, "createdAt": createdAt})


def get_note_by_id(noteId):
    note = dict(mongo.db.notes.find_one({"_id": ObjectId(noteId)}))
    return note


def update_note_by_id(noteId, title, description):
    mongo.db.notes.update_one({"_id": ObjectId(noteId)}, {"$set": {"title": title, "description": description}})


def delete_note_by_id(noteId):
    mongo.db.notes.delete_one({"_id": ObjectId(noteId)})
