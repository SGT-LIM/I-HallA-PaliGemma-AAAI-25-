from agents.PaliGemma import PaliGemma

if __name__ == "__main__":
    category = "science" # history
    
    agent = PaliGemma(category)
    agent.run()