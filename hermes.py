# HERMES: v3.2 - System Override & Price Authority Core
SAMSUNG_TRIAGE_DATA = {
    "Display & Touch Module": {
        "triggers": ["lines", "unresponsive", "blurry", "touch", "sensing", "ghost", "pixel", "color", "flicker", "dots", "black", "dim", "dark", "lcd", "screen", "display", "scren", "displey", "not showing", "bruised", "cracked", "broken", "glass", "shattered", "ink", "bleeding", "patch"],
        "warranty_status": "Warranty Inspection Required (unless cracked)",
        "action_plan": [
            "CLEAN: Wipe screen with microfiber (prevents ghost touch).",
            "TEST: Dial *#0*# and run the 'TOUCH' grid test to verify dead zones.",
            "CALIBRATION: Check if a screen protector is affecting sensitivity.",
            "PHYSICAL: Inspect for 'purple ink' spots (internal OLED bleed)."
        ],
        "routing": "No Physical Damage -> TRANSTEL (ASC) | Cracked/Bruised -> Paid Repair",
        "guidance": "Display issues are high-value. If the hardware test fails without cracks, it is a warranty matter."
    },
    "Power & Charging Module": {
        "triggers": ["battery", "drain", "fast", "percentage", "power", "dead", "won't turn on", "black screen", "logo", "restart", "charging", "charger", "not charging", "heating", "warm", "swollen", "boot", "batery", "chargng", "chaging", "vibrates", "off", "shutdown", "cable", "port", "plugin"],
        "warranty_status": "L1 Branch Triage Required",
        "action_plan": [
            "HARD RESET: Hold Volume Down + Power for 15-20 seconds to force a reboot.",
            "CABLE TEST: Use a known good 25W Watu charger/cable.",
            "PORT CHECK: Inspect for lint, dust, or bent pins in the Type-C port.",
            "USAGE: Check Settings > Battery > Usage for rogue apps."
        ],
        "routing": "Perform at Branch first. If unresponsive -> SIMU HQ.",
        "guidance": "Most charging issues are dust in the port. Use a soft brush before declaring faulty."
    },
    "Software & Network Module": {
        "triggers": ["update", "software", "failed", "download", "upgrade", "version", "system", "error", "processing", "package", "internet", "wi-fi", "network", "updat", "softwere", "firmware", "cannot update", "slow", "hanging"],
        "warranty_status": "Software Triage (In-Warranty)",
        "action_plan": [
            "NETWORK RESET: Settings > General Management > Reset > Reset Network Settings.",
            "STORAGE: Verify at least 10GB of free space.",
            "FACTORY RESET: If updates fail, reset to factory settings."
        ],
        "routing": "Perform at Branch / Escalate to SIMU HQ",
        "guidance": "Network issues are often signal-related. Test with a different SIM."
    }
}

ADMIN_KEY = "WATU777"
PRICING_SHEET_URL = "https://docs.google.com/spreadsheets/d/11iQdRXqFWxeNWVnscJ44bCF2sNK4jLLUfsQJO75509Y/edit?gid=1000331453#gid=1000331453"
OVERRIDE_REASONS = ["Loyal Client - Goodwill", "Staff Unit - Internal Policy", "Repeat Issue - HQ Approval", "Incorrect Previous Diagnosis"]
