from client import VercelAiSdkToolCallerClient
client = VercelAiSdkToolCallerClient()
print(client.validate_args('{"location": "SF"}', ["location"]))