# HERMES: The Predictive Triage Logic Core
# Focused on accurate warranty validation and regional routing.

SAMSUNG_TRIAGE_DATA = {
    "Physical & Liquid Damage": {
        "triggers": [
            "crack", "broken", "water", "liquid", "fell", "dropped", "shattered", 
            "dent", "moisture", "screen", "sink", "rain", "smash", "glass", "display", "leak"
        ],
        "warranty_status": "Out of Warranty (Physical/Liquid)",
        "action_plan": [
            "Inspect the Liquid Damage Indicator (LDI) in the SIM slot.",
            "Document all impact points or moisture signs with clear photos.",
            "Refer to the Repair Pricing Chart for out-of-warranty costs."
        ],
        "routing": "Refer to TRANSTEL (ASC) - Paid Repair",
        "guidance": "Acknowledge the situation with empathy. Explain that physical/liquid ingress voids the warranty and provide the estimated cost from the pricing chart."
    },
    "Power & Software Triage": {
        "triggers": [
            "power", "charging", "charger", "dead", "logo", "restart", "hang", 
            "password", "lock", "frp", "pattern", "google", "account", "frozen", "slow", "off"
        ],
        "warranty_status": "Software Triage (In-Warranty Service)",
        "action_plan": [
            "Attempt a Force Restart: Hold Vol Down + Power for 15 seconds.",
            "Inspect the Type-C port for lint, dust, or bent pins.",
            "Verify device ownership and loan status in the finance system."
        ],
        "routing": "Perform at Branch / Escalate to SIMU HQ",
        "guidance": "Assure the client we are performing a technical reset. This is often a software-related issue that can be resolved on-site to save them time."
    },
    "Component & Technical Failure": {
        "triggers": [
            "lines", "touch", "sensing", "mic", "speaker", "network", "signal", 
            "sim", "vibration", "camera", "volume", "earpiece", "bluetooth", "wi-fi", "pixel"
        ],
        "warranty_status": "Warranty Inspection Required",
        "action_plan": [
            "Enter the Samsung Test Menu by dialing *#0*#.",
            "Test the specific hardware component (Touch, Sensor, Speaker).",
            "Verify the IMEI (*#06#) to ensure no system corruption."
        ],
        "routing": "Refer to TRANSTEL (ASC) - Warranty Claim",
        "guidance": "Inform the customer we need a hardware diagnostic. If no physical damage is found, this is a standard manufacturing warranty claim."
    }
}

PROCEDURES = {
    "LDI Check": "Sticker in SIM slot: White = Dry. Red/Pink = Liquid contact confirmed.",
    "Hardware Test": "Dial *#0*# in the phone app to access the Samsung internal testing suite.",
    "Force Restart": "Hold Volume Down + Power simultaneously for 15 seconds until the logo appears.",
    "Safe Mode": "Power Off > Hold Power > When 'Samsung' appears, hold Volume Down until boot."
}