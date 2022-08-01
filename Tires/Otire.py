class Ctrire:
    def __init__(self , nums):
        self.status = nums
    def needs_service(self):
        sum = 0
        for it in self.status:
            sum += it
        return sum < 3