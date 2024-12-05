from flask import Flask
from flask_caching import Cache
import redis

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0

# Initialize Flask-Caching with Redis
cache = Cache(app=app)
cache.init_app(app)

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/items', methods=['GET'])
@cache.cached(timeout=60, key_prefix='items')
def get_items():

      cached_response = redis_client.get('items')
      print(cached_response)



if __name__ == "__main__":
    app.run(debug=True)