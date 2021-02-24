from django.apps import AppConfig


class IssueTrackerConfig(AppConfig):
    name = 'issue_tracker'

    def ready(self):
        import issue_tracker.signals
