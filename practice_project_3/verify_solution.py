"""
Run the visible test suite against `claim_search_solution.py`.

This does NOT touch your practice file (`claim_search.py`). It works
by aliasing the solution module as `claim_search` in sys.modules
BEFORE importing the test file, so the test file's
`from claim_search import ...` resolves to the reference solution.

Run:
    python verify_solution.py
"""

from __future__ import annotations

import importlib
import sys


def main() -> None:
    sys.modules["claim_search"] = importlib.import_module("claim_search_solution")

    # Import after the alias is in place so the test file binds against
    # the solution module.
    import test_claim_search  # noqa: E402

    failures = []
    for t in test_claim_search.ALL_TESTS:
        # Skip the WRITTEN_ANSWER.md check — that file is the practice
        # surface and is expected to still contain a TODO placeholder.
        if t.__name__ == "test_written_answer_is_filled_in":
            print(f"  SKIP  {t.__name__}  (verify_solution does not check the practice WRITTEN_ANSWER.md)")
            continue
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except AssertionError as e:
            failures.append(f"{t.__name__}: {e}")
            print(f"  FAIL  {t.__name__}  -> {e}")
        except Exception as e:
            failures.append(f"{t.__name__}: {type(e).__name__}: {e}")
            print(f"  ERROR {t.__name__}  -> {type(e).__name__}: {e}")

    print()
    if failures:
        print(f"{len(failures)} failing test(s) against the reference solution.")
        raise SystemExit(1)
    print("Reference solution passes all visible implementation tests.")


if __name__ == "__main__":
    main()
