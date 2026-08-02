import uvicorn
import argparse
import sys
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="🌐 omni-gateway-local")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    
    args = parser.parse_args()
    
    print(f"Starting Omni Gateway on {args.host}:{args.port}")
    uvicorn.run("omni_gateway.main:app", host=args.host, port=args.port, reload=False)

if __name__ == "__main__":
    main()
