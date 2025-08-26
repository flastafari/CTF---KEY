import os

def process_payment(amount, currency):
    """
    Simulates processing a payment using a fictional API.
    """
    # This is a highly sensitive API key used for payment processing.
    # NEVER hardcode a key like this in a real application!
    # This is an example of what to look for in a CTF.
    IDWALL_API_KEY = "sk_live_fictional_42k3j4n5m6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3g4h5i6j7k7l"

    print(f"Processing a payment of {amount} {currency}...")
    print(f"Using API key: {IDWALL_API_KEY}")

    # In a real scenario, this would call a payment API.
    # Example: api_client.process(amount, currency, IDWALL_API_KEY)
    
    print("Payment processed successfully!")

if __name__ == "__main__":
    process_payment(150.00, "USD")
