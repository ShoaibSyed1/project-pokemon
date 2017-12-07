import site

site.addsitedir("d:\\python\\lib\\site-packages")

from game.game import Game

gm = Game()
gm.run()