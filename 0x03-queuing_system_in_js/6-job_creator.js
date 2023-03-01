import kue from 'kue';

const queue = kue.createQueue();

const queueName = 'push_notification_code';
const obj = {
  phoneNumber: '011147829',
  message: 'you are succesfully registered!',
};
 

const job = queue.create(queueName, obj) 

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
})
  .on('completed', () => {
    console.log('Notification job completed');
  })

    .on('failed', () => {
      console.log('Notification job failed');
});
job.save();
