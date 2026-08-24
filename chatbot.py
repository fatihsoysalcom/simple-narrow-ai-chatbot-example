import re

def simple_narrow_ai_chatbot():
    """
    A simple rule-based chatbot demonstrating 'Narrow AI'.
    It responds to specific patterns but explicitly states its limitations,
    highlighting that it's a program, not a conscious entity.
    """
    print("Merhaba! Ben basit bir sohbet botuyum. (Hello! I am a simple chatbot.)")
    print("Bana 'Yapay zeka nedir?', 'Kendini nasıl hissediyorsun?' gibi sorular sorabilirsin.")
    print("Çıkmak için 'çıkış' yazabilirsin.")
    print("-" * 50)

    # Define patterns and responses. This is the core of the "narrow intelligence".
    # Each pattern is a regex, and the response is a string.
    # Responses are crafted to emphasize the AI's nature as a tool/program,
    # rather than a conscious or generally intelligent entity.
    responses = {
        r"(merhaba|selam)": "Merhaba! Size nasıl yardımcı olabilirim? (Hello! How can I help you?)",
        r"yapay zeka nedir\?": "Yapay zeka, belirli görevleri yerine getirmek üzere tasarlanmış algoritmalar ve veri işleme sistemleridir. Bilinçli bir varlık değildir.", # Explicitly states AI is not conscious.
        r"kendini nasıl hissediyorsun\?": "Benim duygularım yok. Ben bir bilgisayar programıyım. (I don't have feelings. I am a computer program.)", # Emphasizes lack of consciousness/emotions.
        r"kimsin\?": "Ben bir yapay zeka programıyım, insan değilim. (I am an AI program, not a human.)",
        r"ne yapabilirsin\?": "Belirli sorulara yanıt verebilirim ve basit sohbetler yapabilirim. Ancak genel bir anlayışa veya bilince sahip değilim.", # Highlights task-specific ability and lack of general understanding.
        r"teşekkürler|sağ ol": "Rica ederim! Başka bir konuda yardımcı olabilir miyim? (You're welcome! Can I help with anything else?)",
        r"hava durumu": "Üzgünüm, hava durumu bilgisi sağlayamam. Ben sadece belirli sorulara yanıt vermek üzere tasarlanmış bir programım.", # Explicitly states a limitation outside its narrow scope.
        r"saat kaç\?": "Üzgünüm, şu anki saati söyleyemem. Ben bir saat değilim. (Sorry, I cannot tell the current time. I am not a clock.)", # Another clear limitation.
        r"çıkış|güle güle|hoşça kal": "Güle güle! Tekrar görüşmek üzere. (Goodbye! See you again.)",
    }

    while True:
        user_input = input("Sen: ").strip().lower()

        if user_input in ["çıkış", "güle güle", "hoşça kal"]:
            print(responses["çıkış|güle güle|hoşça kal"])
            break

        found_response = False
        for pattern, response in responses.items():
            if re.search(pattern, user_input):
                print(f"Bot: {response}")
                found_response = True
                break

        if not found_response:
            # This default response clearly demonstrates the 'narrowness' of the AI.
            print("Bot: Üzgünüm, bu konuyu anlamadım. Benim bilgim sınırlıdır ve sadece belirli kalıplara yanıt verebilirim.")
            print("     (Sorry, I didn't understand that topic. My knowledge is limited and I can only respond to specific patterns.)")

if __name__ == "__main__":
    simple_narrow_ai_chatbot()
