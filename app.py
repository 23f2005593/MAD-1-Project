from flask import Flask, render_template, redirect, request, jsonify, flash
from config import Config
from database import init_db, db
from models import Entry
from forms import EntryForm

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

# post route - create
@app.route('/', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(name=form.name.data) # create new entry
        db.session.add(entry)
        db.session.commit()
        flash('Entry created successfully!', "success")
        return redirect('/')
    
    entries = Entry.query.order_by(Entry.timestamp.desc()).all()
    return render_template('index.html', form=form, entries=entries)


# delete route - delete
@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = Entry.query.get_or_404(id) # get id value
    db.session.delete(entry) # detete entry
    db.session.commit() # commit
    flash('Entry deleted successfully!', "success")
    return redirect('/')

# get route - read
@app.route('/search', methods=["GET"])
def search_entry():
    entry_id = request.args.get("id")  # get id from query params
    search_result = None
    search_error = None

    if entry_id:
        entry = Entry.query.get(entry_id)  # fetch entry by ID
        if entry:
            search_result = entry  # pass the entry to the template
        else:
            search_error = f"Entry with ID {entry_id} not found."  # set error message
    else:
        search_error = "Please provide a valid Entry ID."

    # Fetch all entries for display
    form = EntryForm()
    entries = Entry.query.order_by(Entry.timestamp.desc()).all()
    return render_template('index.html', form=form, entries=entries, search_result=search_result, search_error=search_error)
    

# put route - update
@app.route('/update/<int:id>', methods=['POST'])  # or PUT if using JS
def update_entry(id):
    entry = Entry.query.get_or_404(id)  # fetch entry by ID
    new_name = request.form.get('name')  # get data from form
    if new_name:
        entry.name = new_name  # update name
    entry.timestamp = db.func.now()  # update timestamp

    db.session.commit()  # Save changes
    flash('Entry updated successfully!', 'success')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
