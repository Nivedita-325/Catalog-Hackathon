import random

# Dictionary containing states and their capitals
states_and_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata',
    'Andaman and Nicobar Islands': 'Port Blair',
    'Chandigarh (Union Territory)': 'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
    'Lakshadweep': 'Kavaratti',
    'Delhi': 'New Delhi',
    'Puducherry': 'Puducherry',
    'Ladakh': 'Leh',
    'Jammu and Kashmir': 'Srinagar (summer), Jammu (winter)'
}


def conduct_quiz():
    # Shuffle the states
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    score = 0

    # Conduct the quiz
    for i, state in enumerate(states, 1):
        print(f"Question {i}: What is the capital of {state}?")
        answer = input("Your answer: ").strip()

        if answer.lower() == states_and_capitals[state].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {states_and_capitals[state]}.\n")

    print(f"Quiz finished! Your total score is {score} out of {len(states)}.")

if __name__ == "__main__":
    print("Welcome to the States and Capitals Quiz!")
    conduct_quiz()
