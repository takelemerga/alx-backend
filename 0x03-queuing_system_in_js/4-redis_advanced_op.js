import redis from 'redis';

//create redis client
//use default 127.0.0.1 and port 6379 if
//not specified as parameter of createClient()
//e.g const client = redis.createClient(6379, '192.168.10.87');
const client = redis.createClient();

//print a message to the console
//if we are unable to connect to the Redis server
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

//print a message to the console
//if we can connect to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const KEY = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
    client.hset(KEY, key, values[index], redis.print);
});

client.hgetall(KEY, (err, value) => {
    console.log(value);
});
