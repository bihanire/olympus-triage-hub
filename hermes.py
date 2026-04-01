# HERMES: v2.9 - High-Readability Logic
SAMSUNG_TRIAGE_DATA = {
    "Display & Touch Module": {
        "triggers": [
            "lines", "unresponsive", "blurry", "touch", "sensing", "ghost", 
            "pixel", "color", "flicker", "dots", "black", "dim", "dark", "lcd",
            "screen", "display", "scren", "displey", "not showing", "bruised",
            "cracked", "broken", "glass", "shattered", "ink", "bleeding", "patch"
        ],
        "warranty_status": "Warranty Inspection Required (unless cracked)",
        "action_plan": [
            "CLEAN: Wipe screen with microfiber (prevents ghost touch).",
            "TEST: Dial *#0*# and run the 'TOUCH' grid test.",
            "CALIBRATION: Check if a screen protector is affecting sensitivity.",
            "PHYSICAL: Check for 'purple ink' spots (internal OLED bleed)."
        ],
        "routing": "No Physical Damage -> TRANSTEL (ASC) | Cracked -> Paid Repair",
        "guidance": "Screen issues are the #1 volume. If the hardware test fails without impact marks, it is a warranty matter."
    },
    "Power & Charging Module": {
        "triggers": [
            "battery", "drain", "fast", "percentage", "power", "dead", "won't turn on", 
            "black screen", "logo", "restart", "charging", "charger", "not charging",
            "heating", "warm", "swollen", "boot", "batery", "chargng", "chaging", 
            "vibrates", "off", "shutdown", "cable", "port", "plugin"
        ],
        "warranty_status": "L1 Triage Required",
        "action_plan": [
            "HARD RESET: Hold Vol Down + Power for 15-20 seconds.",
            "CABLE TEST: Use a known good 25W Watu charger/cable.",
            "PORT CHECK: Inspect for lint or bent pins in the Type-C port.",
            "USAGE: Check Settings > Battery > Usage for rogue apps."
        ],
        "routing": "Perform at Branch / If unresponsive -> SIMU HQ",
        "guidance": "Most charging issues are just dust in the port or a frozen software boot. Reset first."
    },
    "Software & Network Module": {
        "triggers": [
            "update", "software", "failed", "download", "upgrade", "version", 
            "system", "error", "processing", "package", "internet", "wi-fi", 
            "network", "updat", "softwere", "firmware", "cannot update", "slow", "hanging"
        ],
        "warranty_status": "Software Triage (In-Warranty)",
        "action_plan": [
            "NETWORK RESET: Settings > General Management > Reset > Reset Network Settings.",
            "STORAGE: Verify at least 10GB of free space.",
            "FACTORY RESET: If update persists in failing, reset to factory settings."
        ],
        "routing": "Perform at Branch / Escalate to SIMU HQ",
        "guidance": "Always check the Wi-Fi signal before blaming the software."
    },
    "Security & Accounts Module": {
        "triggers": [
            "password", "lock", "pattern", "forgot", "google", "frp", 
            "account", "pin", "locked", "bypass", "gmail", "email", "signin"
        ],
        "warranty_status": "L1 Software Service (HQ)",
        "action_plan": [
            "VERIFY: Check Watu loan status and client ID.",
            "GSPN: Use authorized flashing tools for FRP/Lock removal.",
            "MAINTENANCE: Enable Maintenance Mode to protect client privacy."
        ],
        "routing": "SIMU HQ (Software Specialist)",
        "guidance": "Standard software resolution. Verify the loan status before performing a bypass."
    }
}

PRICING_SHEET_URL = "https://docs.google.com/spreadsheets/d/11iQdRXqFWxeNWVnscJ44bCF2sNK4jLLUfsQJO75509Y/edit?gid=1000331453#gid=1000331453"
