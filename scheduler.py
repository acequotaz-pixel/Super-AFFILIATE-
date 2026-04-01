from apscheduler.schedulers.asyncio import AsyncIOScheduler
def start_scheduler(app):
    scheduler = AsyncIOScheduler()
    scheduler.start()
