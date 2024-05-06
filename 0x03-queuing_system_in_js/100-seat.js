import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

const app = express();
const client = createClient();
const kueClient = createQueue();
const HOST = '127.0.0.1';
const PORT = 1245;
let reservationEnabled = true;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const getAsync = promisify(client.get).bind(client);
  const mawjood = await getAsync('available_seats');
  return Number(mawjood);
}

app.get('/available_seats', async (req, res) => {
  const mawjood = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: mawjood });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }
  res.send({ status: 'Reservation in process' });
  const ehjiz = kueClient.create('reserve_seat').save();
  ehjiz.on('complete', () => {
    console.log(`Seat reservation job ${ehjiz.id} completed`);
  });
  ehjiz.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${ehjiz.id} failed ${errorMessage}`);
  });
});

app.get('/process', (_req, res) => {
  kueClient.process('reserve_seat', async (_job, done) => {
    let mawjood = await getCurrentAvailableSeats();
    if (!mawjood) {
      done(new Error('Not enough seats available'));
      return;
    }
    mawjood -= 1;
    reserveSeat(mawjood);
    if (!mawjood) reservationEnabled = false;
    done();
  });
  res.send({ status: 'Queue processing' });
});

app.listen(PORT, HOST, () => {
  console.log(`Server is live at ${HOST}:${PORT}`);
});
