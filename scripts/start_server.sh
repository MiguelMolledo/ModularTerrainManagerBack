# Get the directory where the script is located
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_DIR="$SCRIPTDIR/.."
CONFIG_FILE="$MAIN_DIR/config.toml"
echo "Main Dir: $MAIN_DIR"
echo "Config File: $CONFIG_FILE"
# Function to extract values from TOML file
get_toml_value() {
    grep "^$1" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d ' "'
}
# Read values from the TOML file
HOST=$(get_toml_value "host")
PORT=$(get_toml_value "port")
RELOAD=$(get_toml_value "reload")
WORKERS=$(get_toml_value "workers")
LOG_LEVEL=$(get_toml_value "log_level")

# Check if RELOAD is true and set the flag accordingly
RELOAD_FLAG=""
if [[ "$RELOAD" == "true" ]]; then
    RELOAD_FLAG="--reload"
fi

# Navigate to the script directory
cd "$MAIN_DIR"
# Activate virtual environment (if using one)
source env/bin/activate

# Print extracted values (for debugging)
echo "Starting Uvicorn with:"
echo "Host: $HOST, Port: $PORT, Reload: $RELOAD, Workers: $WORKERS, Log Level: $LOG_LEVEL"


# Start Uvicorn server
uvicorn app.main:app --host "$HOST" --port "$PORT" --workers "$WORKERS" --log-level "$LOG_LEVEL" $RELOAD_FLAG







