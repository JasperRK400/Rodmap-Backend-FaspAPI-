

def get_ai_roadmap(prompt):
    return requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
        params={"key": os.getenv("GEMINI_API_KEY")},
        json={"contents":[{"parts":[{"text":prompt}]}]}
    ).json()
