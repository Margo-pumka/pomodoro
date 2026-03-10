


class MailClient:

    @staticmethod
    def send_welcome_email(to: str) -> None:
        from worker.celery import send_email_task
        return send_email_task.delay("Welcome email", "Welcome to pomodoro", to)
