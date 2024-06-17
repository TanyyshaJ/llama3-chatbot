import ollama
# Make sure to pull: ollama pull llama3 to be able to use llama3 model using ollama

# Another way to import the model is using langchain
# pip install langchain-community
# from langchain_community.llms import Ollama
# llm = Ollama(model = "llama3")
# print(llm.invoke(user_input))

class AI_Assistant:
    def __init__(self):

        self.full_transcript = [
            {"role": "system", "content": "You are a language model called Llama 3 created by Meta. Chat with the user in a friendly way and answer the questions in not more than 300 words. Do not bold or asterisk anything."},
        ]

    def chat(self):
        while True:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                break

            self.full_transcript.append({"role": "user", "content": user_input})

            ollama_stream = ollama.chat(
                model="llama3",
                messages=self.full_transcript,
                stream=True,
            )

            print("Llama 3:")

            response = ""
            for chunk in ollama_stream:
                response += chunk['message']['content']
                print(chunk['message']['content'], end="", flush=True)

            self.full_transcript.append({"role": "assistant", "content": response})
            print()

ai_assistant = AI_Assistant()
ai_assistant.chat()

#---------------------------------------------------------------------------------------------
#use the following code for a little bit faster response, it does not save the whole chat, only the latest responses

# import ollama


# class AI_Assistant:
#   def __init__(self):
    
#     self.last_user_input = ""
#     self.last_llama_response = ""

#   def chat(self):
#     while True:
#       user_input = input("User: ")
#       if user_input.lower() == "exit":
#         break

#       self.last_user_input = user_input

#       ollama_stream = ollama.chat(
#           model="llama3",
#           messages=[
#               {"role": "user", "content": self.last_user_input},
#               {"role": "assistant", "content": self.last_llama_response}
#           ],
#           stream=True,
#       )

#       print("Llama 3:")

#       response = ""
#       for chunk in ollama_stream:
#         response += chunk['message']['content']
#         print(chunk['message']['content'], end="", flush=True)

#       self.last_llama_response = response
#       print()

# ai_assistant = AI_Assistant()
# ai_assistant.chat()