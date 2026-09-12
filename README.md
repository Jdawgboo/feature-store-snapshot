# feature-store-snapshot

Create deterministic in-memory feature snapshots and SHA-256 content fingerprints.

Records are sorted by a caller-supplied key before canonical JSON hashing, making equivalent record orderings comparable.

```bash
python -m unittest -v
```

MIT licensed.