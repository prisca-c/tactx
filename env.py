from dotenv import load_dotenv, dotenv_values
import getpass

# Load environment variables from .env file
load_dotenv()

# Access variables as dictionary
config = dotenv_values(".env")

# Access variables as environment variables
PLAYER_ID = config['PLAYER_ID'] if 'PLAYER_ID' in config else input("👾 robotId: ")
ARENA = config['ARENA'] if 'ARENA' in config else input("🎲 arena: ")
USERNAME = config['USERNAME'] if 'USERNAME' in config else input("👤 username: ")
PASSWORD = config['PASSWORD'] if 'PASSWORD' in config else getpass.getpass("🔑 password: ")
SERVER = config['SERVER'] if 'SERVER' in config else input("🌐 server: ")
