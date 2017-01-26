import pygal
import psycopg2
import yaml
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


def connect():
    return psycopg2.connect(user=config['user'], password=config['password'], host=config['host'], port=config['port'], database=config['database'])


def get_users(cur):
    query = open(config['users-query-web'],'r').read()
    cur.execute(query)
    return cur.fetchall()


def get_user_rank(cur, user_id, time):
    query = open(config['get-rank'], 'r').read()
    query = query.format(user_id, time)
    cur.execute(query)
    return cur.fetchall()


@app.route("/")
def hello():
    conn = connect()
    cur = conn.cursor()
    users = get_users(cur)
    conn.close()
    return render_template('users.html', users=users, str=str)


@app.route('/ranks', methods=['GET','POST'])
def ranks():
    id = request.form['user'].split('-')[0]
    user = request.form['user'].split('-')[1]
    time = request.form['time']
    if (int(time) < 1):
        time = 1000
    conn = connect()
    cur = conn.cursor()
    ranks = get_user_rank(cur, id, time)
    xs = []
    ys = []
    for rank in ranks:
        xs += [rank[0]]
        ys += [rank[1]]
    l = pygal.Line()
    l.x_labels = xs
    l.add(user, ys)
    conn.close()
    return l.render(is_unicode=True)


def main():
    app.run()

if __name__ == "__main__":
    config = yaml.load(open('config-web.yaml', 'r').read())
    main()
