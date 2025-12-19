class NSFWClassifierOutput:
    """
    Represents the output of the NSFW classifier.
    """
    drawings: float
    hentai: float
    neutral: float
    porn: float
    sex: float

    def __init__(self, drawings: float, hentai: float, neutral: float,
                 porn: float, sex: float):
        self.drawings = drawings
        self.hentai = hentai
        self.neutral = neutral
        self.porn = porn
        self.sex = sex

    def to_dict(self):
        return {
            "drawings": self.drawings,
            "hentai": self.hentai,
            "neutral": self.neutral,
            "porn": self.porn,
            "sex": self.sex
        }

    def __repr__(self):
        return (f"NSFWClassifierOutput(drawings={self.drawings}, "
                f"hentai={self.hentai}, neutral={self.neutral}, "
                f"porn={self.porn}, sex={self.sex})")
