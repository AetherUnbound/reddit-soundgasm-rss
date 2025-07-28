# Build the Docker image
build:
    docker build -t reddit-soundgasm-rss .

# Start the application with Docker Compose
up service="":
    #!/usr/bin/env bash
    if [ ! -f compose.yml ]; then
        echo "compose.yml not found, running with docker run..."
        docker run --rm -p 8000:8000 reddit-soundgasm-rss
    else
        if [ -n "{{service}}" ]; then
            docker compose up {{service}}
        else
            docker compose up
        fi
    fi

# Stop the application
down:
    docker compose down || true

# View logs
logs service="":
    #!/usr/bin/env bash
    if [ -n "{{service}}" ]; then
        docker compose logs -f {{service}}
    else
        docker compose logs -f
    fi

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
    curl -s http://localhost:8000/feed.rss | head -20

# Clean up Docker resources
clean:
    docker image prune -f
    docker container prune -f