class Ctrire:
    def __init__(self , nums):
        self.status = nums
    def needs_service(self):
        for it in self.status:
            if it < 0.9:
                return False
        return True