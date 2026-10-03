# Public GitHub Repository Release Notes

## Repository

Planned public repository name: `higher-mathematics-orders`

Purpose: preserve and explain the textbook-grounded Order 1–8 historical build in an outsider-readable public repository.

## Included in Git history

The Git repository includes all ordinary project files:

- all Order reports, specifications, source findings, audits, and plans;
- all pure-Python mechanisms, tests, and recorded outputs;
- the detailed `REPOSITORY_GUIDE.md`;
- OCR text extracts in `book_ocr_opening/`, `chapter_samples/`, and `full_ocr/`;
- sampled textbook images in `book_samples/`;
- the supplied task material and repository manifests.

Generated Python bytecode in `__pycache__/` is intentionally excluded because it is reproducible build output rather than historical source material.

## Large-file handling

GitHub's ordinary Git file limit is below the size of two historical artifacts:

- `HigherMath1stKetabuddin2026.pdf` — approximately 129 MB;
- `HigherMath_Orders_Historical_Repository_End_to_End.zip` — approximately 129 MB.

These exact files are preserved as public GitHub Release assets rather than being silently removed or altered. The repository documentation and checksum manifest identify them. The release assets can be downloaded independently of a normal Git clone.

## Verification policy

Before publication:

1. all Python test suites must pass;
2. repository inventory and archive inventory must match for the archive scope;
3. SHA-256 checksums must validate;
4. the public repository must contain the outsider guide and historical caveats;
5. large files must be uploaded as release assets with their exact filenames.

## Historical interpretation

Order 3 remains preserved as a formal control-flow experiment but is not overstated as a new black-box numerical capability. The current frozen work ends at Order 8, and future Orders require a separate mathematical specification and boundary test.
