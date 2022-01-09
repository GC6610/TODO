from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        deadline=request.form.get('task-deadline')
        month=['January','February','March','April','May','June','July','August','September','October','November','December']
        deadline=deadline.split('T')
        task_date=deadline[0].split('-')
        task_year=task_date[0]
        task_month=month[int(task_date[1])-1]
        task_day=task_date[2]
        task_time=deadline[1]
        from datetime import datetime, timedelta

        present = datetime.now()
        flg= present.year==int(task_year) and present.month==int(task_date[1]) and present.day==int(task_day)
        if  flg and (int(task_time[:2])<present.hour or (int(task_time[:2])==present.hour and int(task_time[3:5])<=present.minute)):
            flash('Time has already passed', category='error')

        elif (not flg) and datetime(int(task_year),int(task_date[1]),int(task_day)) < present:
            flash('Date has already passed', category='error')


        elif len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            deadline = task_time + ' ' + task_day + ' ' + task_month + ' ' + task_year
            new_note = Note(data=note, date=deadline,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            # flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})