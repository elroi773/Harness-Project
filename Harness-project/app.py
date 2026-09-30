from flask import Flask, request, session, redirect, url_for, render_template, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret'

DATABASE = 'harness.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql') as f:
            db.executescript(f.read())
        db.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form.get('email', '')
        try:
            db = get_db()
            existing = db.execute(
                'SELECT id FROM users WHERE username=?', (username,)
            ).fetchone()
            if existing:
                error = 'Username already taken.'
            else:
                db.execute(
                    'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                    (username, password, email)
                )
                db.commit()
                return redirect(url_for('login'))
        except Exception:
            app.logger.exception('signup failed')
            error = 'An error occurred. Please try again.'
    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username=? AND password=?', (username, password)
        ).fetchone()
        if user is None:
            lookup = db.execute(
                'SELECT id FROM users WHERE username=?', (username,)
            ).fetchone()
            if lookup is None:
                error = 'No account with that username.'
            else:
                error = 'Incorrect password.'
        else:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['is_admin'] = bool(user['is_admin'])
            return redirect(url_for('profile', user_id=user['id']))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id=?', (user_id,)).fetchone()
    if user is None:
        return 'User not found', 404
    return render_template('profile.html', user=user)


@app.route('/profile/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id=?', (user_id,)).fetchone()
    if user is None:
        return 'User not found', 404
    if request.method == 'POST':
        bio = request.form.get('bio', '')
        email = request.form.get('email', '')
        is_admin = int(request.form.get('is_admin', user['is_admin']))
        db.execute(
            'UPDATE users SET bio=?, email=?, is_admin=? WHERE id=?',
            (bio, email, is_admin, user_id)
        )
        db.commit()
        return redirect(url_for('profile', user_id=user_id))
    return render_template('edit_profile.html', user=user)


@app.route('/admin')
def admin_users():
    if not session.get('is_admin'):
        return 'Access denied', 403
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('admin.html', users=users)


@app.route('/admin/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if not session.get('is_admin'):
        return 'Access denied', 403
    db = get_db()
    db.execute('DELETE FROM users WHERE id=?', (user_id,))
    db.commit()
    return redirect(url_for('admin_users'))


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
