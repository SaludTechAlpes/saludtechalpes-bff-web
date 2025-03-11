import os

class Config:
    def __init__(self):
        self.MEDICAL_HISTORY_MS_URL = os.getenv(
            "MEDICAL_HISTORY_MS_URL", default="localhost"
        )
        self.ENVIRONMENT = os.getenv("FLASK_ENV")
        self.APP_NAME = os.getenv("APP_NAME", "saludtech-bff-web")

        self.PULSAR_HOST = os.getenv("PULSAR_HOST", "pulsar")
        self.BROKER_HOST = os.getenv("BROKER_HOST", "broker")
        self.BROKER_PORT = os.getenv("BROKER_PORT", "6650")
