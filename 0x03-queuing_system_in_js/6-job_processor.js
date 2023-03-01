import kue from 'kue';

const queue = kue.createQueue();
const queueName = 'push_notification_code';

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

queue.process(queueName, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});

