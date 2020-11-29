from apscheduler.schedulers.blocking import BlockingScheduler
from main import brno_part_budget

sched = BlockingScheduler()
sched.add_job(brno_part_budget, 'cron', hour=21, minute=15)

sched.start()
