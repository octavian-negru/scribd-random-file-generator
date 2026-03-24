# Install dependencies using uv
install:
    uv sync

# Run the random file generator
run:
    uv run random_file_generator.py

# Install deps and run
all: install run
