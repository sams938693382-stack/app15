class Pubg:
    def __init__(self, nick, uc):
        self.nick = nick
        self.uc = uc

    def add_uc(self, miqdor):
        self.uc += miqdor
        print(f"🎮 {miqdor} UC qoshildi")

    def info(self):
        print(f"👤 Nick: {self.nick}")
        print(f"💎 UC: {self.uc}")


player = Pubg("X_Sniper", 60)

player.add_uc(325)
player.add_uc(660)

player.info()