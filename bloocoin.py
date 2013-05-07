import cmd
import os
import socket
import json

import coins
import addr
import register
import send
import transactions

__version__ = "1.1.0-devel"


class BlooClient(cmd.Cmd):
    server = ("bloocoin.zapto.org", 3122)

    def preloop(self):
        self.prompt = "BLC $ "
        self.intro = "".join([
            "The official BlooCoin client (version {0})".format(__version__),
            "\nType 'help' or '?' for a list of commands\n"
        ])

    def _send_command(self, cmd, payload, buffer_size=1024):
        # Merge payload with command.
        payload = dict(cmd=cmd, **payload)
        try:
            s = socket.socket()
            s.connect(self.server)
            s.send(json.dumps(payload))
            data = ""
            while True:
                recv = s.recv(buffer_size)
                if recv:
                    data += recv
                else:
                    break
            data = json.loads(data)
            return data
        except IOError as e:
            # Ehhhhhhrrrrr, debugging maybe?
            return False
        except ValueError as e:
            # Invalid JSON returned, most likely
            return False

    def emptyline(self):
        """ We don't want to do anything given no command """
        pass

    def do_exit(self, line):
        return -1

    def do_EOF(self, line):
        """ So ^D will exit like in a normal shell """
        return self.do_exit(line)

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

    def help_coins(self):
        print "Prints the current amount of coins in your wallet."

    def help_addr(self):
        print "Prints your current address which can be used for transactions."

    def help_send(self):
        print "Can be used to send coins to a given address."
        print "usage: send <amount> <recipient>"

    def help_transactions(self):
        print "Lists all transactions both TO and FROM your address."

    def help_exit(self):
        print "Exits the BlooCoin shell."

if __name__ == "__main__":
    if not os.path.exists("bloostamp"):
        register.register()
    BlooClient().cmdloop()
