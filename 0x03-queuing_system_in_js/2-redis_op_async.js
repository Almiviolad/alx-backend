import {createClient} from 'redis';
const client = createClient();
const redis = require('redis');
const { promisify } = require('util');
client
    .on('connect', () => {console.log('Redis client connected to the server')})
    .on('error', (err) => {console.log(`Redis client not connected to the server: ${err}`)});
const asyncGet = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
}
async function displaySchoolValue(schoolName) {
    try {
	const value = await asyncGet(schoolName);
	console.log(value);
    } catch(error) {
	console.log(`Error getting ${schoolName}: ${error}`)}
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
