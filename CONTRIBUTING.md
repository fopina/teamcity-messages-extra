## Development

This project uses [uv](https://docs.astral.sh/uv/). Install the project and its development dependencies with:

```sh
uv sync --dev
```

Run tests and check formatting before pushing:

```sh
make test
make style-check
```

Use `make style` to apply formatting, and `uv build` to build the source distribution and wheel.

After changing dependencies in `pyproject.toml`, run `uv lock` and commit the updated `uv.lock`.
