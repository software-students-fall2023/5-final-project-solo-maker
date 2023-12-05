from datetime import datetime

from flask import jsonify, render_template, Blueprint, request, flash, redirect, url_for, Response, make_response
from .models import get_notes, save_note, get_note_by_id, update_note_by_id, delete_note_by_id
import requests

main = Blueprint('main', __name__)


@main.route("/")
def home():
    # get the notes from the database
    notes = get_notes();

    # render a view
    return render_template("/pages/home.html", homeIsActive=True, addNoteIsActive=False, notes=notes)


@main.route("/add-note", methods=['GET', 'POST'])
def addNote():
    if (request.method == "GET"):

        return render_template("pages/add-note.html", homeIsActive=False, addNoteIsActive=True)

    elif (request.method == "POST"):

        # get the fields data
        title = request.form['title']
        description = request.form['description']
        createdAt = datetime.now()

        # save the record to the database
        save_note(title, description, createdAt)

        # redirect to home page
        return redirect("/")


@main.route('/edit-note', methods=['GET', 'POST'])
def editNote():
    if request.method == "GET":

        # get the id of the note to edit
        noteId = request.args.get('form')

        # get the note details from the db
        note = get_note_by_id(noteId)

        # direct to edit note page
        return render_template('pages/edit-note.html', note=note)

    elif request.method == "POST":

        # get the data of the note
        noteId = request.form['_id']
        title = request.form['title']
        description = request.form['description']

        # update the data in the db

        update_note_by_id(noteId, title, description)

        # redirect to home page
        return redirect("/")


@main.route('/delete-note', methods=['POST'])
def deleteNote():
    # get the id of the note to delete
    noteId = request.form['_id']

    # delete from the database
    delete_note_by_id(noteId)

    # redirect to home page
    return redirect("/")

@main.route('/search', methods=['GET','POST'])
def search():
    search_query = None
    if request.method == 'POST':
        search_query = request.form.get('search')
        print(search_query)
        return redirect(url_for('main.datasource', query = search_query))
    return render_template('pages/search-bilibili.html')

@main.route('/api/v1/datasource/<query>', methods=['GET', 'POST'])
def datasource(query):
    return render_template('pages/scrapy-bilibili.html', uid = query)
