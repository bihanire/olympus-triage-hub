# HERMES: The Master Triage Glossary (v2.1 - Transtel & Battery Optimized)
SAMSUNG_TRIAGE_DATA = {
    "Display & Touch (Top Tier Issue)": {
        "triggers": [
            "lines", "unresponsive", "blurry", "touch", "sensing", "ghost", 
            "pixel", "color", "flicker", "dots", "black", "dim", "dark", "lcd",
            "screen", "display", "not showing"
        ],
        "warranty_status": "Warranty Inspection Required (unless cracked)",
        "action_plan": [
            "1. CLEAN: Wipe screen with microfiber (prevents ghost touch).",
            "2. TEST: Dial *#0*# and run the 'TOUCH' grid test.",
            "3. CALIBRATION: Check if a screen protector is affecting sensitivity.",
            "4. PHYSICAL: Check for 'purple ink' spots (indicates internal OLED bleed)."
        ],
        "routing": "No Physical Damage -> TRANSTEL (ASC) | Cracked -> Paid Repair",
        "guidance": "Screen issues are the #1 complaint. If hardware test fails without impact marks, reassure the client it is a warranty matter."
    },
    "Power, Battery & Charging (Tier 1)": {
        "triggers": [
            "battery", "drain", "fast", "percentage", "power", "dead", "won't turn on", 
            "black screen", "logo", "restart", "charging", "charger", "not charging",
            "heating", "warm", "swollen", "boot", "vibrates but no display"
        ],
        "warranty_status": "L1 Triage Required",
        "action_plan": [
            "1. HARD RESET: Hold Vol Down + Power for 15-20 seconds.",
            "2. CABLE TEST: Use a known good 25W Watu charger/cable.",
            "3. PORT CHECK: Inspect for lint or bent pins in the Type-C port.",
            "4. USAGE: Check Settings > Battery > Usage for rogue apps."
        ],
        "routing": "Perform at Branch / If unresponsive -> SIMU HQ",
        "guidance": "Battery drain is often software-related. A hard reset or clearing background apps solves many 'dead' units."
    },
    "Software Updates & Network (Tier 2)": {
        "triggers": [
            "update", "software", "failed", "download", "upgrade", "version", 
            "system", "error", "processing", "package", "internet", "wi-fi", "network"
        ],
        "warranty_status": "Software Triage (In-Warranty)",
        "action_plan": [
            "1. NETWORK RESET: Settings > General Management > Reset > Reset Network Settings.",
            "2. STORAGE: Verify at least 10GB of free space.",
            "3. FACTORY RESET: If update persists in failing, perform a 'Reset to Factory Settings' (Back up data first!)."
        ],
        "routing": "Perform at Branch / Escalate to SIMU HQ",
        "guidance": "Most update failures are Network-related. Always reset network settings before attempting the download again."
    },
    "Security & Account Access": {
        "triggers": ["password", "lock", "pattern", "forgot", "google", "frp", "account", "pin"],
        "warranty_status": "L1 Software Service (HQ)",
        "action_plan": [
            "1. VERIFY: Check Watu loan status and client ID.",
            "2. GSPN: Use authorized flashing tools for FRP/Lock removal.",
            "3. MAINTENANCE: Enable Maintenance Mode to protect client privacy."
        ],
        "routing": "SIMU HQ (Software Specialist)",
        "guidance": "This is a standard software resolution. It is not a hardware fault."
    }
}

RESOURCES = {
    "Samsung Support": "https://www.samsung.com/africa_en/support/",
    "G-Mail Recovery": "https://accounts.google.com/signin/recovery",
    "Support Email": "simurepairs@watu.africa" 
}
