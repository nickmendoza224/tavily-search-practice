"""Search the web with Tavily and print a few readable results."""

import argparse
import os
import sys

from tavily import TavilyClient


def main() -> int:
    parser = argparse.ArgumentParser(description="Try a Tavily web search")
    parser.add_argument("query", nargs="?", default="recent EEG seizure detection research")
    args = parser.parse_args()

    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        print("Set TAVILY_API_KEY before running this script.", file=sys.stderr)
        return 1

    response = TavilyClient(api_key=api_key).search(args.query, max_results=5)
    for number, result in enumerate(response.get("results", []), start=1):
        print(f"\n{number}. {result.get('title', 'Untitled')}")
        print(result.get("url", ""))
        print(result.get("content", ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
