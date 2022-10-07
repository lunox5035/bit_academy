# class Log:
# def __init__(self.side)->None:
#     print("다리")
#     self.side=side
#     pass


from body.human import Humman


class Leg(Humman):
    def __init__(self,side,name)->None:
        print("다리")
        self.side=side
        super().__into__(name) 
        pass