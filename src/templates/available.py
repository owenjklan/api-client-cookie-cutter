API_CLIENTS = {
    "logic_monitor": {
        "name": "LogicMonitor REST API client",
        "click_options": {
            "lm_access_id": {
                "long": "--lm-access-id",
                "short": None,
                "type": str,
            },
        }
    }
}

SWITCH_FLAGS = {
    "debug_flag": {
        "var_name": "debug_flag",
        "long": "--debug",
        "short": None,
        "help": "Add more debugging output"
    },
    "verbose_flag": {
        "var_name": "verbose_flag",
        "long": "--verbose",
        "short": None,
        "help": "Be more verbose in output"
    },
    "quiet_flag": {
        "var_name": "quiet_flag",
        "long": "--quiet",
        "short": None,
        "help": "Reduce output, ideal for scripts"
    }
}
