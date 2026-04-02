# HERMES v6.1 - THE MASTER REPOSITORY (SOP + SAMSUNG L1)
SAMSUNG_TRIAGE_DATA = {
    "Theft & Replacement SOP": {
        "triggers": ["stolen", "theft", "lost", "police", "abstract", "replacement", "mifos", "nin"],
        "status": "ASSET REPLACEMENT PROTOCOL",
        "action_plan": [
            "POLICE ABSTRACT: Confirm A4 size with Client Name, Phone, and IMEI.",
            "STATUS CHECK: Verify 10+ weekly payments in MIFOS. Ensure status is 'Stolen'.",
            "REPLACEMENT ELIGIBILITY: If abstract is missing, log 'Stolen w/o Abstract' ticket.",
            "OBS LOGGING: Create 'Repossessed' loan type > Capture IMEI > Upload KYC & ID.",
            "HANDOVER: Handover only after Back Officer approval and Agreement signing."
        ],
        "routing": "Branch Officer -> SIMU Admin -> Back Officer",
        "guidance": "Verify the 'Thefts Tab' in the Master Queries using NIN if status isn't updated."
    },
    "Samsung L1 Service Essentials": {
        "triggers": ["greeting", "customer care", "best practice", "fcr", "etiquette", "process", "flow", "interaction"],
        "status": "SAMSUNG SERVICE STANDARD",
        "action_plan": [
            "GREET & ID: Confirm ownership and capture device Model/IMEI.",
            "PROBING: Ask 'What happened? When did it start?' to identify user vs hardware issues.",
            "L1 TRIAGE: Check Battery, SIM/Network, Storage, and Physical Damage.",
            "RESOLUTION: Restart, Update Software, or Clear Cache before escalating.",
            "COMMUNICATION: Explain the 'Why' behind every action to the client."
        ],
        "routing": "Frontline Agent (L1 Support)",
        "guidance": "First Contact Resolution (FCR) is the goal. Do not escalate simple software glitches."
    },
    "Hardware & Connectivity Triage": {
        "triggers": ["screen", "display", "lines", "freezing", "water", "liquid", "fell down", "software", "update", "internet", "battery", "charge", "maintenance mode", "safe mode"],
        "status": "TECHNICAL DIAGNOSIS",
        "action_plan": [
            "LIQUID: Check LCI (Liquid Contact Indicator) in SIM tray. Pink/Red = Out of Warranty.",
            "SCREEN: Dial *#0*# for hardware test. Check for impact marks/dents (Voids Warranty).",
            "FREEZE: Hold Vol Down + Power (15s) for Forced Reboot. Test in Safe Mode.",
            "POWER: Inspect port for lint. Test with known-good 25W Watu charger.",
            "PRIVACY: Always enable 'Maintenance Mode' before taking the device for repair."
        ],
        "routing": "In-Warranty -> Transtel (ASC) | Out-Warranty -> Paid Repair",
        "guidance": "Check Column V in Master Queries for specific repair delays (parts/approval)."
    },
    "Device Recovery & Unlocking": {
        "triggers": ["recovered", "third party", "unlock", "pin", "nexus", "tmp", "offline", "relock"],
        "status": "RECOVERY & ACCESS PROTOCOL",
        "action_plan": [
            "STANDARD RECOVERY: Log 'Standard Recovery' ticket > Request 'Remove LS'.",
            "3RD PARTY: Collect ID/Phone of finder. Ship to HQ. Reward: UGX 25,000.",
            "NEXUS UNLOCK: Use 'TMP Unlock' if online. Use 'Unlock PIN' if offline.",
            "AUTO-UNLOCK: Guide client to pay via Watu App (One SIM only, Data ON, VPN OFF)."
        ],
        "routing": "Branch Officer -> Simu Admin -> Nexus",
        "guidance": "Ensure relock timestamp in MIFOS shows 7 days since agreement started."
    }
}

ADMIN_KEY = "WATU777"
PRICING_SHEET_URL = "https://docs.google.com/spreadsheets/d/11iQdRXqFWxeNWVnscJ44bCF2sNK4jLLUfsQJO75509Y/edit"
