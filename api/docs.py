define_responses = random_responses = {
    404: {
        "description": "Word not found",
        "content": {"application/json": {"example": {"message": "Not Found"}}},
    },
    200: {
        "description": "Word found.",
        "content": {
            "application/json": {
                "example": {
                    "Word": "Soulslike",
                    "Meanings": {
                        "0": {
                            "meaning": "A game that features elements similar to the game Dark Souls.\re.g. skill based, steep difficulty, focus on bosses, punishing deaths, rich enviroment.",
                            "contributor": "by ChineseHacker September 24, 2016",
                        }
                    },
                },
            },
        },
    },
}
