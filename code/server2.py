from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
    count = redis.incr('hits')
    return '<h1>Hello AWS Wroclaw Meetup #1</h1><h3>I have been seen {} times</h3>'.format(count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
