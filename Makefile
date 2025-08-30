install:
	uv sync

brain-progression:
	uv run brain-progression

brain-gcd:
	uv run brain-gcd

brain_calc:
	uv run brain-calc

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