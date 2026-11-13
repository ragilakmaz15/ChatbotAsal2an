"""Titik masuk program: dialog loop di terminal."""
from chatbot import get_response
from matcher import match_intent_nlp


def run_chatbot():
    print("Chatbot FAQ UNP (ketik 'keluar' untuk berhenti)")
    while True:
        user_input = input("Anda: ")
        response, mode = get_response(user_input)
        print(f"Bot [{mode}]:", response)
        if match_intent_nlp(user_input)[0] == "goodbye":
            break


if __name__ == "__main__":
    run_chatbot()
