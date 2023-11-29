import {createClient} from 'redis';
const client = createClient();
const redis = require('redis');
const { promisify } = require('util');
client
    .on('connect', () => {console.log('Redis client connected to the server')})
    .on('error', (err) => {console.log(`Redis client not connected to the server: ${err}`)});
client.hset('HolbertonSchools', 'Portland,', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools',  'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, hashValues) => {
      if (err) {
        console.error('HGETALL Error:', err);
      } else {
        console.log(hashValues);
      }
});
