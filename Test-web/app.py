from flask import Flask, render_template
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://test-web_redis_1:6379/0"  # Update with your Redis server details
redis = FlaskRedis(app)

@app.route('/')
def home():
    # Increment counter in Redis
    redis.incr('visit_count')

    # Get the current counter value
    visit_count = int(redis.get('visit_count').decode('utf-8'))

    return render_template('index.html', visit_count=visit_count)

if __name__ == '__main__':
    app.run(debug=True)
