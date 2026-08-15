from django.db import models

#Tabla gates (puertas de embarque):
#id BIGSERIAL PK
#code VARCHAR(10) NOT NULL UNIQUE
#terminal VARCHAR(20) NOT NULL
#is_available BOOLEAN NOT NULL DEFAULT TRUE
#created_at TIMESTAMP NOT NULL DEFAULT NOW()

class Gate(models.Model):
    code = models.CharField(max_length=10, unique=True)
    terminal = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gate {self.code} ({self.terminal})"

#Tabla flights (vuelos):
#id BIGSERIAL PK
#gate_id BIGINT NOT NULL REFERENCES gates(id)
#flight_number VARCHAR(20) NOT NULL (ej: "AA1234")
#destination VARCHAR(100) NOT NULL
#status VARCHAR(20) NOT NULL (SCHEDULED|BOARDING|DEPARTED|DELAYED|CANCELLED)
#departure_time TIMESTAMP NOT NULL
#created_at TIMESTAMP NOT NULL DEFAULT NOW()

class Flight(models.Model):
    STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("BOARDING", "Boarding"),
        ("DEPARTED", "Departed"),
        ("DELAYED", "Delayed"),
        ("CANCELLED", "Cancelled"),
    ]

    gate = models.ForeignKey(Gate, on_delete=models.CASCADE, db_column="gate_id", related_name="flights")
    flight_number = models.CharField(max_length=20)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="SCHEDULED")
    departure_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vuelo {self.flight_number} -> {self.destination} ({self.status})"