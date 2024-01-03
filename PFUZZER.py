import requests
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="URL to fuzz")
    parser.add_argument("-type", "--type", required=True, help="Type of fuzzing: num or file")
    parser.add_argument("-start", "--start", type=int, default=0, help="Start number for num fuzzing")
    parser.add_argument("-step", "--step", type=int, default=1, help="Step for num fuzzing")
    parser.add_argument("-end", "--end", type=int, default=1000, help="End number for num fuzzing")
    args = parser.parse_args()

    if args.type == "num":
        for i in range(args.start, args.end+1, args.step):
            fuzzed_url = args.url.replace("PFUZZ", str(i))
            response = requests.get(fuzzed_url)
            data_size = len(response.content)
            print(f"URL: {fuzzed_url}, Response status code: {response.status_code}, Data Size: {data_size} bytes")

    elif args.type.endswith(".txt"):
        with open(args.type, 'r') as f:
            lines = [line.strip() for line in f]
            for line in lines:
                fuzzed_url = args.url.replace("PFUZZ", line)
                response = requests.get(fuzzed_url)
                data_size = len(response.content)
                print(f"URL: {fuzzed_url}, Response status code: {response.status_code}, Data Size: {data_size} bytes")

if __name__ == '__main__':
    main()