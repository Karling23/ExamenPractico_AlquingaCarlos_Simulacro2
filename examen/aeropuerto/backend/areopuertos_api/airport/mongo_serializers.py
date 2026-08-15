from rest_framework import serializers
#ServiceTypeSerializer
class AirlineSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)
    country = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField(default=True)

#VehicleServiceSerializer
class FlightEventSerializer(serializers.Serializer):
    flight_id = serializers.IntegerField()
    event_type = serializers.ChoiceField(choices=["CREATED", "BOARDING_STARTED", "DEPARTED", "DELAYED", "CANCELLED"])
    source = serializers.ChoiceField(choices=["WEB", "MOBILE", "SYSTEM"])
    note = serializers.CharField(required=False, allow_blank=True, allow_null=True)



#Colección airlines (aerolíneas registradas):
#_id ObjectId
#name string
#code string (ej: "AA")
#country string
#is_active bool
#created_at date
#----------------------------------------------------------------------------
#Colección flight_events (eventos operativos):
#_id ObjectId
#flight_id long (id SQL)
#event_type string (CREATED|BOARDING_STARTED|DEPARTED|DELAYED|CANCELLED)
#source string (WEB|MOBILE|SYSTEM)
#note string (texto simple, sin objeto)
#created_at date