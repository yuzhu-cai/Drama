from openai import OpenAI
from config.varibles import OPENAI_API_KEY, OPENAI_BASE_URL

class OpenAILLM:
    def __init__(
            self,
            system_prompt: str = "You are a helpful assistant!"
    ):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL
        )
        self.system_prompt = system_prompt

    def set_system_prompt(self, system_prompt: str):
        self.system_prompt = system_prompt

    def call(
            self, 
            query: str, 
            model: str="gpt-4o-mini", 
            temperature: float = 0.2, 
            top_p: float = 1.0, 
            max_tokens: int = 4096, 
            frequency_penalty: float = 0.0
    ):
        message = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": query}
        ]
        completion = self.client.chat.completions.create(
            model=model,
            messages=message,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty
        )
        
        return completion.choices[0].message.content


if __name__ == "__main__":
    llm = OpenAILLM()
    query = "1+1=?"
    print(llm.call(query))