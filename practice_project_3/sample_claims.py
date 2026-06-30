"""
Sample claims corpus used by the visible tests.

The hidden grader will run additional corpora — do not rely on
specific claim_ids or wording beyond what the spec requires.
"""

from typing import Any, Dict, List


SAMPLE_CLAIMS: List[Dict[str, Any]] = [
    {
        "claim_id":    "CL-001",
        "claim_type":  "auto",
        "status":      "open",
        "filed_date":  "2026-04-12",
        "description": "Rear-end collision on highway 101 during heavy rain. Front bumper and headlights damaged.",
        "amount":      4500.0,
    },
    {
        "claim_id":    "CL-002",
        "claim_type":  "home",
        "status":      "closed",
        "filed_date":  "2025-11-03",
        "description": "Roof damage from windstorm. Several shingles missing and minor water intrusion in the attic.",
        "amount":      8200.0,
    },
    {
        "claim_id":    "CL-003",
        "claim_type":  "auto",
        "status":      "pending",
        "filed_date":  "2026-02-21",
        "description": "Parked vehicle struck by a delivery truck. Driver-side door dented and side mirror broken.",
        "amount":      1900.0,
    },
    {
        "claim_id":    "CL-004",
        "claim_type":  "health",
        "status":      "open",
        "filed_date":  "2026-05-01",
        "description": "Emergency room visit for a fractured wrist after a bicycle accident. X-rays and cast required.",
        "amount":      3200.0,
    },
    {
        "claim_id":    "CL-005",
        "claim_type":  "home",
        "status":      "denied",
        "filed_date":  "2025-09-18",
        "description": "Basement flooding from a burst washing machine hose. Policy excludes appliance failures.",
        "amount":      6500.0,
    },
    {
        "claim_id":    "CL-006",
        "claim_type":  "auto",
        "status":      "closed",
        "filed_date":  "2025-07-04",
        "description": "Single-vehicle accident; driver hit a deer at dusk. Hood and grille replaced.",
        "amount":      5400.0,
    },
    {
        "claim_id":    "CL-007",
        "claim_type":  "health",
        "status":      "pending",
        "filed_date":  "2026-03-29",
        "description": "Outpatient surgery for a torn meniscus. Physical therapy expected over twelve weeks.",
        "amount":      11200.0,
    },
    {
        "claim_id":    "CL-008",
        "claim_type":  "life",
        "status":      "open",
        "filed_date":  "2026-01-10",
        "description": "Beneficiary claim filed after the policyholder's death. Death certificate and policy on file.",
        "amount":      250000.0,
    },
    {
        "claim_id":    "CL-009",
        "claim_type":  "home",
        "status":      "open",
        "filed_date":  "2026-04-30",
        "description": "Kitchen fire originating from a faulty toaster. Smoke damage throughout the first floor.",
        "amount":      18500.0,
    },
    {
        "claim_id":    "CL-010",
        "claim_type":  "auto",
        "status":      "open",
        "filed_date":  "2026-05-08",
        "description": "Hit-and-run in a parking lot. Rear bumper scraped; no witnesses but security footage available.",
        "amount":      2200.0,
    },
    {
        "claim_id":    "CL-011",
        "claim_type":  "health",
        "status":      "closed",
        "filed_date":  "2025-06-14",
        "description": "Routine annual physical and vaccinations. Covered in full under preventive care.",
        "amount":      350.0,
    },
    {
        "claim_id":    "CL-012",
        "claim_type":  "home",
        "status":      "pending",
        "filed_date":  "2026-04-22",
        "description": "Tree fell on garage during a thunderstorm. Garage roof collapsed; vehicle inside unharmed.",
        "amount":      14300.0,
    },
]
