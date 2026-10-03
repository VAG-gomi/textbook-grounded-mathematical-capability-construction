

## 10. Additional recovered source-analysis directories

The restored workspace also contains small historical artifacts from the textbook inspection phase:

- `book_ocr_opening/page-014.txt` — OCR text extracted from an opening textbook page during source inspection.
- `chapter_samples/page-640.txt` — OCR/sample text from a later textbook chapter page.
- `full_ocr/hm-014.txt` — another preserved OCR extract from the supplied textbook.
- `book_samples/page-003.jpg` — sampled textbook page image used during visual source inspection.
- `book_samples/page-006.jpg` — sampled textbook page image used during visual source inspection.
- `book_samples/page-008.jpg` — sampled textbook page image used during visual source inspection.

These files document how the scanned textbook was inspected and are included as historical source-analysis evidence. They are not additional mathematical sources.

The recovered `__pycache__/` directory contains generated Python bytecode. It is intentionally excluded from the public Git repository and refreshed ZIP because it is reproducible build output, not source history.

## 11. Newly recovered historical attachments

The `historical_attachments/` directory preserves two later context files without overwriting the original tracked `pasted_content.txt`.

- `historical_attachments/2026-10-03_pasted_content_repository_guidance.txt` — repository-design guidance emphasizing forensic documentation, boundary tests, the distinction between implementation and experiment, the formal/degenerate status of Order 3, and freezing Orders 1–8 before further expansion.
- `historical_attachments/2026-10-03_pasted_content_session_recovery.txt` — session-recovery context explaining that the next possible branch was an agentic-pipeline-to-cognitive-style architecture, to be reconstructed and independently audited rather than silently inserted into Orders 1–8.

These files are historical context, not new verified Orders. The architecture branch remains separate until its explicit mathematical primitives, state, learning rule, capability claim, and falsification tests are supplied.


## 12. Current contract corrections

The current implementation revision makes two contract boundaries explicit. Order 7 uses a finite **numeric** codomain because its correction computes `e=y-ŷ`; its unknown state is an explicit `UNKNOWN` sentinel and cannot collide with a legal codomain value. Order 8 does not claim a separately declared admissible domain; it evaluates scalar inputs through the selected affine expression, leaving domain-management machinery for a future experiment.

The repository also includes a GitHub Actions workflow at `.github/workflows/test-orders.yml`. CI is implementation/reproducibility evidence only; it does not prove the mathematical theory.

## 13. Additional forensic review attachments

- `historical_attachments/2026-10-03_repository_construction_instructions.txt` — current repository-maintenance instructions, epistemic labels, contract requirements, CI requirements, and the prohibition on premature Order 9.
- `historical_attachments/2026-10-03_repository_forensic_review.txt` — independent file-by-file forensic review identifying the Order 7 numeric-codomain issue, Order 8 domain mismatch, stale metadata, checksum wording, and the need for CI.
- `docs_status_ledger.md` — current flat-repository status ledger corresponding to the recommended frozen status table.
