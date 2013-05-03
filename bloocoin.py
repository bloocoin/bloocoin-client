import cmd
import os
import coins
import addr
import register
import send
import transactions

__version__ = 0.01

class BlooClient(cmd.Cmd):
    prompt = "BlooCoin$ "
    intro = "The BlooCoin Official Client version " + str(__version__)
    def do_coins(self, line):
        print coins.coins()
    def do_addr(self, line):
        print addr.addr()
    def do_send(self, line):
        line = line.split()
        amt = int(line[0])
        to = line[1]
        print send.send(amt, to)
    def do_transactions(self, line):
        transactions.transactions()

if __name__ == "__main__":
    if not os.path.exists("bloostamp"):
        register.register()
    BlooClient().cmdloop()
