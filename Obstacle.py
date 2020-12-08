class Obstacle:
    def __init__(self, carry):
        self.carry = dict(carry)
        self.x = 1
        self.y = 1
                
    def player_Move(self):
        self.start = input("Ready? [Yes/No]")
        self.start = self.start.lower()
        print(f"{self.start}\n")
        
        if self.start == "yes":
            while self.x and self.y != 15:


                self.move = input()
                self.move = self.move.lower()
                
                if self.move == str("w"):
                    self.y += 1
                    print(f"front step({self.x},{self.y})")
                    self.move
                elif self.move == str("s"):
                    self.y -= 1
                    print(f"back step ({self.x},{self.y})")
                    self.move
                elif self.move == str("d"):
                    self.x += 1
                    print(f"right step ({self.x},{self.y})")
                    self.move
                elif self.move == str("a"):
                    self.x -= 1
                    print(f"left step ({self.x},{self.y})")
                    self.move
                elif self.move == str("i"):
                    print(f"{self.carry}")
                    self.move
                elif self.move == str("q"):
                    if self.x == int(3) and self.y == int(14):
                        print('you found a pair of "Bunny Slippers!"')
                        self.carry["Bunny Slippers"] = 10
                        print('Hm, comfy."')
                    elif self.x == int(7) and self.y == int(14):
                        print('Nerf or Nuffin! "Nerf Gun!"')
                        self.carry["Nerf Gun"] = 100
                        print('My arm is complete.')
                    elif self.x == int(12) and self.y == int(1):
                        print('Wow, you picked up a hairy "Mc Muffin!"')
                        self.carry["McMuffin"] = 1000
                        print('Mmm- crunchy.')
                else:
                    print("")
                    
                if self.y < int(1) or self.y >= int(15):
                    print(f"oof!({self.x},{self.y})")
                    break
                elif self.x < int(1) or self.x >= int(15):
                    print(f"oof!({self.x},{self.y})")
                    break

                if int(10) in self.carry.values():
                    if int(100) in self.carry.values():
                        if int(1000) in self.carry.values():
                            print("You win!")
                            break
                
        else:
            print("Bye.")
