

def register_participant(*args, **kwargs):
    # Assuming the first three arguments are name, email, and event_type
    if len(args) < 3:
        raise ValueError("Name, email, and event type are required")

    print(args)
    name, email, event_type = args[:3]
    additional_info = args[3:]  # Additional positional arguments, if any

    participant = {
        'name': name,
        'email': email,
        'event_type': event_type,
        'additional_info': additional_info,
        'registration_details': kwargs
    }
    return participant

# Example of registering a participant with additional arguments
participant_info = register_participant(
    "Alice Smith",
    "alice@example.com",
    "Workshop",
    "Early Bird Registration",  # This is an additional positional argument
    date="2024-01-25",
    payment_method="Credit Card",
    special_requirements="Vegetarian meal",
    promo_code="DISCOUNT20"
)

print(participant_info)
