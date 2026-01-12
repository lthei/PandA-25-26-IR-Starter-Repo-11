#!/usr/bin/env python3
"""
Part 11 starter.

WHAT'S NEW IN PART 11. A positional Index. It's almost done, only the finishing touches remain.
"""
from typing import List
import time

from .constants import BANNER, HELP
from .models import SearchResult, Searcher, SettingCommand

from .file_utilities import load_config, load_sonnets, Configuration


def print_results(
    query: str | None,
    results: List[SearchResult],
    highlight_mode: str,
    query_time_ms: float | None = None,
    total_docs: int | None = None # new parameter for number of total docs (FIX)
) -> None:
    total_docs = total_docs or len(results) # use total_docs unless the value is not passed, then use len(results) (FIX)
    matched = [r for r in results if r.matches > 0]

    line = f'{len(matched)} out of {total_docs} sonnets contain "{query}".'
    if query_time_ms is not None:
        line += f" Your query took {query_time_ms:.2f}ms."
    print(line)

    for idx, r in enumerate(matched, start=1):
        r.print(idx, highlight_mode, total_docs)

# ---------- CLI loop ----------
def main() -> None:
    print(BANNER)
    config = load_config()

    # Load sonnets (from cache or API)
    start = time.perf_counter()
    sonnets = load_sonnets()

    elapsed = (time.perf_counter() - start) * 1000
    print(f"Loading sonnets took: {elapsed:.3f} [ms]")

    print(f"Loaded {len(sonnets)} sonnets.")

    searcher = Searcher(sonnets)

    # ToDo 0 (use three instances of the new class for the setting commands)
    # create three instances, one for each setting (replaces original if-blocks)
    setting_commands = [
        SettingCommand(":highlight"),
        SettingCommand(":search-mode"),
        SettingCommand(":hl-mode"), ]

    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not raw:
            continue

        # commands
        if raw.startswith(":"):
            if raw == ":quit":
                print("Bye.")
                break

            if raw == ":help":
                print(HELP)
                continue

            # ToDo 0 (handle setting commands with new class)
            # this block checks whether the input is a setting command
            handled = False
            for cmd in setting_commands:  # loop over each command until one matches and handles the input
                if cmd.handle(raw, config):
                    handled = True
                    break  # if command was handled, the rest of the (inner) loop is skipped
            if handled:
                continue  # if setting command was processed, the input should not be processed as a search query, so we skip the outer loop
            # if no command matched (handled is still False) , we can run the search logic below

        # ---------- Query evaluation ----------

        words = raw.split()
        if not words:
            continue

        start = time.perf_counter()

        results = searcher.search(raw, config.search_mode)

        # Initialize elapsed_ms to contain the number of milliseconds the query evaluation took
        elapsed_ms = (time.perf_counter() - start) * 1000

        highlight_mode = config.hl_mode if config.highlight else None

        print_results(raw, results, highlight_mode, elapsed_ms, len(sonnets)) # add len(sonnets) to get total number of sonnets (otherwise not displayed correctly) (FIX)

if __name__ == "__main__":
    main()
