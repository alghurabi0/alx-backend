import { createQueue } from 'kue';

const kueClient = createQueue();
const jobObj = { phoneNumber: '+254111222', message: 'Your order is on its way. Thank you for shopping with us.' };
const job = kueClient.create('push_notification_code', jobObj).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
