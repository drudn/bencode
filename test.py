#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      danru
#
# Created:     13-09-2019
# Copyright:   (c) danru 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import bencode

def main():
    print bencode.convert('d7:eredftgi56ei4576ei454ee')
    print bencode.toInteger('i56e')
    print bencode.convert('l15:345sadagfasdgd4i5678ei5234e5:eretye')
    pass

if __name__ == '__main__':
    main()
