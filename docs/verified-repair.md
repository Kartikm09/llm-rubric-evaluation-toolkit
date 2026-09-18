# Verified repair scope

The starting source was `d8adf53e3411e13070dc045824b5e041caeb8125`. The bundled example commands completed,
but there was no automated assertion suite. Bounded synthetic input probes
exposed the defect addressed here.

Enforce documented1–5 dimensions across all three scoring reports.

New regression tests failed before the repair. After the change, `make verify`
passed 3 test methods, including independent result oracles and negative
command-line cases. Every original documented sample command was rerun. Test
counts are methods; parameterized inputs are not inflated into separate tests.

The tests use the standard library and synthetic fixtures. They do not claim
comprehensive schema validation, real model quality, external evidence quality,
or production readiness. CI repeats the discoverable verification command.
