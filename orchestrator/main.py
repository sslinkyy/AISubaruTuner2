# main.py
import argparse
from agents.parser.parser import parse_rom
from agents.suggester.suggester import suggest_changes
from agents.exporter.exporter import apply_changes


def main():
    parser = argparse.ArgumentParser(description='AISubaruTuner2 CLI')
    parser.add_argument('--rom', required=True)
    parser.add_argument('--defs', required=True)
    parser.add_argument('--log', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    parsed = parse_rom(args.rom, args.defs)
    # TODO: integrate Datalog Reader Agent: read_log(args.log)
    changes = suggest_changes(parsed, None)
    apply_changes(args.rom, changes, args.out)
    print(f"Generated tuned ROM at {args.out}")

if __name__ == '__main__':
    main()
