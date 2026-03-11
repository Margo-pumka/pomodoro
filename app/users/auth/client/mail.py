class MailClient:

    @staticmethod
    def send_welcome_email(to: str) -> None:
        from worker.celery import send_email_task
        task_id = send_email_task.delay("Welcome email", "Welcome to pomodoro", to)
        print(f"task_id={task_id}")
        return task_id
