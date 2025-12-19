class NSFWClassifierOutput:
    """
    Represents the output of the NSFW classifier.
    """
    def __init__(self, drawings: float, hentai: float, neutral: float,
                 porn: float, sexy: float):
        self.drawings = drawings
        self.hentai = hentai
        self.neutral = neutral
        self.porn = porn
        self.sexy = sexy

    def to_dict(self):
        return {
            "drawings": self.drawings,
            "hentai": self.hentai,
            "neutral": self.neutral,
            "porn": self.porn,
            "sexy": self.sexy
        }

    def __repr__(self):
        return (f"NSFWClassifierOutput(drawings={self.drawings}, "
                f"hentai={self.hentai}, neutral={self.neutral}, "
                f"porn={self.porn}, sex={self.sexy})")
