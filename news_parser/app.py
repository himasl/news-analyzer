import time

from parsers.kod.parser import kodru_parser
from parsers.habr.parser import habr_parser
from parsers.rbc.parser import rbc_parser
from parsers.hi_tech.parser import hi_tech_parser


def main():
    habr_parser()
    rbc_parser()
    hi_tech_parser()
    kodru_parser()


if __name__ == "__main__":
    while True:
        time.sleep(20)
        main()
        print("Sleeping for 5 minutes")
        time.sleep(5 * 60)  # 5 minutes
