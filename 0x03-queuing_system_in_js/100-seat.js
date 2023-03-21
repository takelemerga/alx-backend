import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();
const app = express();
const queue = kue.createQueue();
const getAsync = promisify(client.get).bind(client);
const PORT = 1245;
let reservationEnabled;
const queueName = 'reserve_seat';

const Key = 'available_seats';

/**
 * Modifies the number of available seats.
 * @param {number} number - The new number of seats.
 */
const reserveSeat = (number) => {
  client.set(Key, number);
}
/* 
 * Retrieves the number of available seats
 */
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync(Key);
  return availableSeats;
}

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  reserveSeat(50);
  reservationEnabled = true;
});

app.listen(PORT, () => {
  console.log(`app listening at http://localhost:${PORT}`);
});

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const jobFormat = {};

  const job = queue.create(queueName, jobFormat);
  job.save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  queue.process(queueName, async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    console.log(availableSeats);
    availableSeats <= 0 ? done(Error('Not enough seats available')) : reserveSeat(Number(availableSeats) - 1);
    

    if (availableSeats <= 0) {
      reservationEnabled = false;
    }

    done();
  });
  res.json({ status: 'Queue processing' });
});
