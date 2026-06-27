import requests
from typing import Dict, Any

class SolanaSecurityAgentSkill:
    """
    A professional AI Agent skill that evaluates the security and rug-risk 
    of any Solana token mint address.
    """
    
    def __init__(self, rpc_url: str = "https://api.mainnet-beta.solana.com"):
        self.rpc_url = rpc_url
        self.headers = {"Content-Type": "application/json"}

    def fetch_account_info(self, mint_address: str) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [mint_address, {"encoding": "jsonParsed"}]
        }
        try:
            response = requests.post(self.rpc_url, json=payload, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            return {"error": "RPC failed"}
        except Exception as e:
            return {"error": str(e)}

    def analyze_token_safety(self, mint_address: str) -> Dict[str, Any]:
        raw_data = self.fetch_account_info(mint_address)
        if "result" not in raw_data or not raw_data["result"]["value"]:
            return {"status": "error", "message": "Invalid address"}

        parsed_info = raw_data["result"]["value"]["data"]["parsed"]["info"]
        mint_authority = parsed_info.get("mintAuthority")
        freeze_authority = parsed_info.get("freezeAuthority")
        
        is_mint_renounced = mint_authority is None
        is_freeze_renounced = freeze_authority is None
        
        return {
            "token_address": mint_address,
            "is_mint_renounced": is_mint_renounced,
            "is_freeze_renounced": is_freeze_renounced,
            "risk_level": "LOW" if (is_mint_renounced and is_freeze_renounced) else "HIGH"
        }

if __name__ == "__main__":
    agent_skill = SolanaSecurityAgentSkill()
    print("Agent Skill Initialized Successfully.")
