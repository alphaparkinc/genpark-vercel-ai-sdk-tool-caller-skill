class VercelAiSdkToolCallerClient:
    def validate_args(self, tool_arguments: str, schema_keys: list[str]) -> dict:
        import json
        try:
            data = json.loads(tool_arguments)
            return {"is_valid": all(k in data for k in schema_keys)}
        except:
            return {"is_valid": False}