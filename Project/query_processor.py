import ollama
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    data: dict  

class QueryProcessor:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name

    def answer_question(self, request: QueryRequest):
        query = f"Data: {request.data} \n Question: {request.question}"
        
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": query}])
        
        return response['message']['content']  
