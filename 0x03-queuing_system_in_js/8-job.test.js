import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw("Jobs is not an array");

    expect(() => {
      createPushNotificationsJobs("Test", queue);
    }).to.throw("Jobs is not an array");

    expect(() => {
      createPushNotificationsJobs(56, queue);
    }).to.throw("Jobs is not an array");
  });

  it('adds jobs to the queue with the correct type', (done) => {
    expect(queue.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: '5672345910',
        message: 'this is the code 2312 to verify your account',
      },
      {
        phoneNumber: '4367893212',
        message: 'this is the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    done();
});
});
