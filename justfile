set dotenv-load


@default:
    just -ul


# Build the Docker image
build:
    docker build -t reddit-soundgasm-rss .

# Start the application with Docker Compose
up service="":
    docker compose up -d {{ service }}

# Stop the application
down:
    docker compose down || true

# View logs
logs service="":
    docker compose logs -f {{ service }}

# Run a command in the app container
run *args:
    docker compose run --rm app {{args}}

# Run the application locally with uv
dev:
    uv run python main.py

# Install dependencies
install:
    uv sync

# Test the RSS feed endpoint
test:
    #!/usr/bin/env bash
    echo "Testing RSS feed endpoint..."
    curl -s http://localhost:$PORT/feed.rss | head -20

# Clean up Docker resources
clean:
    docker image prune -f
    docker container prune -f

# Pull, build, and deploy all services
deploy:
    -git pull
    @just down
    @just build
    @just up
