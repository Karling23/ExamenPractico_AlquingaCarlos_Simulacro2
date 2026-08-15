from rest_framework import serializers
from .models import Gate, Flight

class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ["id", "code", "terminal", "is_available", "created_at"]

class FlightSerializer(serializers.ModelSerializer):
    gate_code = serializers.ReadOnlyField(source="gate.code")

    class Meta:
        model = Flight
        fields = [
            "id",
            "gate",
            "gate_code",
            "flight_number",
            "destination",
            "status",
            "departure_time",
            "created_at",
        ]

#Tabla gates (puertas de embarque):
#id BIGSERIAL PK
#code VARCHAR(10) NOT NULL UNIQUE
#terminal VARCHAR(20) NOT NULL
#is_available BOOLEAN NOT NULL DEFAULT TRUE
#created_at TIMESTAMP NOT NULL DEFAULT NOW()
#------------------------------------------------
#Tabla flights (vuelos):
#id BIGSERIAL PK
#gate_id BIGINT NOT NULL REFERENCES gates(id)
#flight_number VARCHAR(20) NOT NULL (ej: "AA1234")
#destination VARCHAR(100) NOT NULL
#status VARCHAR(20) NOT NULL (SCHEDULED|BOARDING|DEPARTED|DELAYED|CANCELLED)
#departure_time TIMESTAMP NOT NULL
#created_at TIMESTAMP NOT NULL DEFAULT NOW()
