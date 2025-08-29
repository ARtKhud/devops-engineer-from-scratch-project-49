install:
	uv sync

brain-even:
	uv run brain-even

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	 uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check brain_games --fix