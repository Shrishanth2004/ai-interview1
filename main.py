from langchain_ollama import ChatOllama

def main():
    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    print("Welcome! I am your AI assistant. Type 'quit' to exit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = llm.invoke(user_input)
        print("\nAssistant:", response)

if __name__ == "__main__":
    main()