from flask import Flask, render_template, redirect
from config import Config
from database import init_db, db
from models import Entry
from forms import EntryForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(name=form.name.data)
        db.session.add(entry)
        db.session.commit()
        return redirect('/')
    
    entries = Entry.query.order_by(Entry.timestamp.desc()).all()
    return render_template('index.html', form=form, entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
