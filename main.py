from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
OUTPUT = Path("reports")
OUTPUT.mkdir(exist_ok=True)

print("AI Client Manager")
print("-" * 40)

while True:
    client_name = input("Client name: ").strip()
    request = input("Client request: ").strip()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""You are an AI client-management assistant.
Client: {client_name}
Request: {request}

Return:
## Client Summary
## Request Category
## Priority
## Recommended Response
## Next Action
Keep the response practical and concise."""
    )

    text = f"Client: {client_name}\n\n{response.output_text}\n"
    print("\n" + text)
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in client_name)
    (OUTPUT / f"{safe}.txt").write_text(text, encoding="utf-8")

    if input("Analyze another client? (yes/no): ").lower() != "yes":
        break
