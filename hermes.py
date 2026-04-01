# HERMES: v3.1 - Master Diagnostic Logic
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
            "CLEAN: Use a microfiber cloth to wipe the screen (prevents ghost touch).",
            "TEST: Dial *#0*# and run the 'TOUCH' grid test to verify dead zones.",
            "CALIBRATION: Check if a screen protector or dirt is affecting sensitivity.",
            "PHYSICAL: Inspect for 'purple ink' spots which indicate internal OLED bleed."
        ],
        "routing": "No Physical Damage -> TRANSTEL (ASC) | Cracked/Bruised -> Paid Repair",
        "guidance": "Display issues are high-value. If the hardware test fails but there are NO cracks, reassure the client it's a warranty matter."
    },
    "Power & Charging Module": {
        "triggers": [
            "battery", "drain", "fast", "percentage", "power", "dead", "won't turn on", 
            "black screen", "logo", "restart", "charging", "charger", "not charging",
            "heating", "warm", "swollen", "boot", "batery", "chargng", "chaging", 
            "vibrates", "off", "shutdown", "cable", "port", "plugin"
        ],
        "warranty_status": "L1 Branch Triage Required",
        "action_plan": [
            "HARD RESET: Hold Volume Down + Power for 15-20 seconds to force a reboot.",
            "CABLE TEST: Use a known good 25W Watu charger and cable to rule out accessories.",
            "PORT CHECK: Inspect for lint, dust, or bent pins in the Type-C port.",
            "USAGE: Check Settings > Battery > Usage for rogue background apps."
        ],
        "routing": "Perform at Branch first. If totally unresponsive -> SIMU HQ.",
        "guidance": "Most charging issues are caused by dust in the port. Use a soft brush before declaring the port faulty."
    },
    "Software & Network Module": {
        "triggers": [
            "update", "software", "failed", "download", "upgrade", "version", 
            "system", "error", "processing", "package", "internet", "wi-fi", 
            "network", "updat", "softwere", "firmware", "cannot update", "slow", "hanging"
        ],
        "warranty_status": "Software Triage (In-Warranty)",
        "action_plan": [
            "NETWORK RESET: Go to Settings > General Management > Reset > Reset Network Settings.",
            "STORAGE: Verify at least 10GB of free space for system stability.",
            "FACTORY RESET: If updates persist in failing, reset to factory settings."
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
