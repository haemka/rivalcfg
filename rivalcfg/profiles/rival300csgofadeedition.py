rival300csgofadeedition = {
    "name": "SteelSeries Rival 300 CS:GO Fade Edition",

    "vendor_id": 0x1038,
    "product_id": 0x1394,
    "interface_number": 0,

    "commands": {

        "set_sensitivity1": {
            "description": "Set sensitivity preset 1",
            "cli": ["-s", "--sensitivity1"],
            "command": [0x03, 0x01],
            "value_type": "range",
            "range_min": 50,
            "range_max": 6500,
            "range_increment": 50,
            "value_transform": lambda x: int(x / 50),
            "default": 800,
        },

        "set_sensitivity2": {
            "description": "Set sensitivity preset 2",
            "cli": ["-S", "--sensitivity2"],
            "command": [0x03, 0x02],
            "value_type": "range",
            "range_min": 50,
            "range_max": 6500,
            "range_increment": 50,
            "value_transform": lambda x: int(x / 50),
            "default": 1600,
        },

        "set_polling_rate": {
            "description": "Set polling rate in Hz",
            "cli": ["-p", "--polling-rate"],
            "command": [0x04, 0x00],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },

        "set_logo_light_effect": {
            "description": "Set the logo light effect",
            "cli": ["-e", "--logo-light-effect"],
            "command": [0x07, 0x01],
            "value_type": "choice",
            "choices": {
                "steady": 0x01,
                "breathslow": 0x02,
                "breathmed": 0x03,
                "breathfast": 0x04,
                1: 0x01,
                2: 0x02,
                3: 0x03,
                4: 0x04,
            },
            "default": "steady",
        },

        "set_wheel_light_effect": {
            "description": "Set the wheel light effect",
            "cli": ["-E", "--wheel-light-effect"],
            "command": [0x07, 0x02],
            "value_type": "choice",
            "choices": {
                "steady": 0x01,
                "breathslow": 0x02,
                "breathmed": 0x03,
                "breathfast": 0x04,
                1: 0x01,
                2: 0x02,
                3: 0x03,
                4: 0x04,
            },
            "default": "steady",
        },

        "set_logo_color": {
            "description": "Set the logo backlight color",
            "cli": ["-c", "--logo-color"],
            "command": [0x08, 0x01],
            "value_type": "rgbcolor",
            "default": "#FF5200"
        },

        "set_wheel_color": {
            "description": "Set the wheel backlight color",
            "cli": ["-C", "--wheel-color"],
            "command": [0x08, 0x02],
            "value_type": "rgbcolor",
            "default": "#FF5200"
        },

        "set_btn6_action": {
            "description": "Set the action of the button under the wheel",
            "cli": ["-b", "--btn6-action"],
            "command": [0x0B],
            "value_type": "choice",
            "choices": {
                "default": 0x00,
                "os": 0x01,
            },
            "default": "default",
        },

        "save": {
            "description": "Save the configuration to the mouse memory",
            "cli": None,
            "command": [0x09, 0x00],
            "value_type": None,
        },

    },

}