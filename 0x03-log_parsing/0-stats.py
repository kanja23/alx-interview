#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            tokens = line.split(" ")
            if len(tokens) > 2:
                status_code = tokens[-2]
                if status_code in status_codes:
                    total_size += int(tokens[-1])
                    status_codes[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
