# HERMES: The Master Triage Glossary (v2.3 - Final Production Build)
SAMSUNG_TRIAGE_DATA = {
    "Display & Touch (Top Tier Issue)": {
        "triggers": [
            "lines", "unresponsive", "blurry", "touch", "sensing", "ghost", 
            "pixel", "color", "flicker", "dots", "black", "dim", "dark", "lcd",
            "screen", "display", "scren", "displey", "not showing", "bruised"
        ],
        "warranty_status": "Warranty Inspection Required (unless cracked)",
        "action_plan": [
            "1. CLEAN: Wipe screen with microfiber (prevents ghost touch).",
            "2. TEST: Dial *#0*# and run the 'TOUCH' grid test.",
            "3. CALIBRATION: Check if a screen protector is affecting sensitivity.",
            "4. PHYSICAL: Check for 'purple ink' spots (internal OLED bleed). [View Reference](https://bit.ly/samsung-oled-bleed)"
        ],
        "routing": "No Physical Damage -> TRANSTEL (ASC) | Cracked -> Paid Repair",
        "guidance": "Screen issues are our #1 volume. If hardware test fails without impact marks, reassure the client it is a manufacturing warranty matter."
    },
    "Power, Battery & Charging (Tier 1)": {
        "triggers": [
            "battery", "drain", "fast", "percentage", "power", "dead", "won't turn on", 
            "black screen", "logo", "restart", "charging", "charger", "not charging",
            "heating", "warm", "swollen", "boot", "batery", "chargng", "chaging", "vibrates but no display"
        ],
        "warranty_status": "L1 Triage Required",
        "action_plan": [
            "1. HARD RESET: Hold Vol Down + Power for 15-20 seconds.",
            "2. CABLE TEST: Use a known good 25W Watu charger/cable.",
            "3. PORT CHECK: Inspect for lint or bent pins in the Type-C port.",
            "4. USAGE: Check Settings > Battery > Usage for rogue apps."
        ],
        "routing": "Perform at Branch / If unresponsive -> SIMU HQ",
        "guidance": "Battery issues are high-volume. A hard reset or clearing background apps solves many 'dead' units immediately."
    },
    "Software Updates & Network (Tier 2)": {
        "triggers": [
            "update", "software", "failed", "download", "upgrade", "version", 
            "system", "error", "processing", "package", "internet", "wi-fi", 
            "network", "updat", "softwere", "firmware", "cannot update"
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
        "triggers": ["password", "lock", "pattern", "forgot", "google", "frp", "account", "pin", "locked"],
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

PROCEDURES = {
    "LDI Check": "Sticker in SIM slot: White = Dry. Red/Pink = Liquid contact confirmed.",
    "Hardware Test": "Dial *#0*# in the phone app to access the Samsung internal testing suite.",
    "Force Restart": "Hold Volume Down + Power simultaneously for 15 seconds until the logo appears."
}
