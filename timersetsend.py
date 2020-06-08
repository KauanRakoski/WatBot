from apscheduler.schedulers.blocking import BlockingScheduler
from mom_send import send_text


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_text, 'interval', hours=2)

sched.start()
