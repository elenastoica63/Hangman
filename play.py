import random
import time

word_list = ['Kabul', 'Albania', 'Tirana', 'Algeria', 'Algiers', 'Andorra', 'Angola', 'Luanda', 'Armenia', 'Yerevan', 'Austria', 'Vienna', 'Baku', 'Bahamas', 'Nassau', 'Bahrain', 'Manama', 'Dhaka', 'Belarus', 'Minsk', 'Belgium', 'Belize', 'Bhutan', 'Thimphu', 'Bolivia', 'La Paz', 'Brazil', 'Brunei', 'Sofia', 'Burundi', 'Praia', 'Yaounde', 'Canada', 'Ottawa', 'Bangui', 'Chile', 'China', 'Beijing', 'Colombia', 'Bogota', 'Comoros', 'Moroni', 'San Jose', 'Croatia', 'Zagreb', 'Cuba', 'Havana', 'Cyprus', 'Nicosia', 'Prague', 'Denmark', 'Roseau', 'Ecuador', 'Quito', 'Egypt', 'Cairo', 'Malabo', 'Eritrea', 'Asmara', 'Estonia', 'Tallinn', 'Fiji', 'Suva', 'Finland', 'France', 'Paris', 'Gabon', 'Gambia', 'Banjul', 'Georgia', 'Tbilisi', 'Germany', 'Berlin', 'Ghana', 'Accra', 'Greece', 'Athens', 'Guinea', 'Conakry', 'Bissau', 'Guyana', 'Hungary', 'Iceland', 'India', 'Jakarta', 'Iran', 'Tehran', 'Iraq', 'Baghdad', 'Ireland', 'Dublin', 'Israel', 'Italy', 'Rome', 'Jamaica', 'Japan', 'Tokyo', 'Jordan', 'Amman', 'Astana', 'Kenya', 'Nairobi', 'Kosovo', 'Kuwait', 'Bishkek', 'Laos', 'Latvia', 'Riga', 'Lebanon', 'Beirut', 'Lesotho', 'Maseru', 'Liberia', 'Libya', 'Tripoli', 'Vaduz', 'Vilnius', 'Skopje', 'Malawi', 'Male', 'Mali', 'Bamako', 'Malta', 'Mexico', 'Palikir', 'Moldova', 'Monaco', 'Monaco', 'Morocco', 'Rabat', 'Maputo', 'Namibia', 'Nauru', 'Nepal', 'Managua', 'Niger', 'Niamey', 'Nigeria', 'Abuja', 'Norway', 'Oslo', 'Oman', 'Muscat', 'Palau', 'Panama', 'Peru', 'Lima', 'Manila', 'Poland', 'Warsaw', 'Lisbon', 'Qatar', 'Doha', 'Romania', 'Russia', 'Moscow', 'Rwanda', 'Kigali', 'Samoa', 'Apia', 'Riyadh', 'Senegal', 'Dakar', 'Serbia', 'Honiara', 'Somalia', 'Seoul', 'Juba', 'Spain', 'Madrid', 'Sudan', 'Mbabane', 'Sweden', 'Bern', 'Syria', 'Taiwan', 'Taipei', 'Dodoma', 'Bangkok', 'Togo', 'Lome', 'Tunisia', 'Tunis', 'Turkey', 'Ankara', 'Tuvalu', 'Uganda', 'Kampala', 'Ukraine', 'Kyiv', 'London', 'Uruguay', 'Vanuatu', 'Caracas', 'Vietnam', 'Hanoi', 'Zambia', 'Lusaka', 'Harare']
word_list1 = ['Argentina', 'Australia', 'Canberra', 'Azerbaijan', 'Bangladesh', 'Barbados', 'Bridgetown', 'Brussels', 'Belmopan', 'Sarajevo', 'Botswana', 'Gaborone', 'Brasilia', 'Bulgaria', 'Bujumbura', 'Cabo Verde', 'Cambodia', 'Phnom Penh', 'Cameroon', 'Santiago', 'Kinshasa', 'Costa Rica', 'Copenhagen', 'Dominica', 'El Salvador', 'Ethiopia', 'Addis Ababa', 'Helsinki', 'Libreville', 'Guatemala', 'Georgetown', 'Honduras', 'Budapest', 'Reykjavik', 'New Delhi', 'Indonesia', 'Jerusalem', 'Kingston', 'Kazakhstan', 'Kiribati', 'Pristina', 'Kuwait City', 'Kyrgyzstan', 'Vientiane', 'Monrovia', 'Lithuania', 'Luxembourg', 'Luxembourg', 'Macedonia', 'Madagascar', 'Lilongwe', 'Malaysia', 'Maldives', 'Valletta', 'Majuro', 'Mauritania', 'Nouakchott', 'Mauritius', 'Port Louis', 'Mexico City', 'Micronesia', 'Chisinau', 'Mongolia', 'Montenegro', 'Podgorica', 'Mozambique', 'Windhoek', 'Kathmandu', 'Amsterdam', 'New Zealand', 'Wellington', 'Nicaragua', 'North Korea', 'Pyongyang', 'Pakistan', 'Islamabad', 'Ngerulmud', 'Palestine', 'Ramallah', 'Panama City', 'Paraguay', 'Asunción', 'Portugal', 'Bucharest', 'Basseterre', 'Saint Lucia', 'Castries', 'Kingstown', 'San Marino', 'San Marino', 'Belgrade', 'Seychelles', 'Victoria', 'Freetown', 'Singapore', 'Singapore', 'Slovakia', 'Bratislava', 'Slovenia', 'Ljubljana', 'Mogadishu', 'Pretoria', 'South Korea', 'South Sudan', 'Khartoum', 'Suriname', 'Paramaribo', 'Swaziland', 'Stockholm', 'Damascus', 'Tajikistan', 'Dushanbe', 'Tanzania', 'Thailand', 'Ashgabat', 'Funafuti', 'Abu Dhabi', 'Washington', 'Montevideo', 'Uzbekistan', 'Tashkent', 'Port Vila', 'Venezuela', 'Zimbabwe']
word_list2 = ['Afghanistan', 'Andorra la Vella', 'Buenos Aires', 'Bosnia and Herzegovina', 'Bandar Seri Begawan', 'Burkina Faso', 'Ouagadougou', 'Central African Republic', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Brazzaville', 'Czech Republic', 'Dominican Republic', 'Santo Domingo', 'San Salvador', 'Equatorial Guinea', 'Guatemala City', 'Guinea-Bissau', 'Tegucigalpa', 'South Tarawa', 'Liechtenstein', 'Antananarivo', 'Kuala Lumpur', 'Marshall Islands', 'Ulaanbaatar', 'Yaren District', 'Netherlands', 'Papua New Guinea', 'Port Moresby', 'Philippines', 'Saint Kitts and Nevis', 'Saint Vincent and the Grenadines', 'Saudi Arabia', 'Sierra Leone', 'Solomon Islands', 'South Africa', 'Switzerland', 'Trinidad and Tobago', 'Port of Spain', 'Turkmenistan', 'United Arab Emirates', 'United Kingdom', 'United States of America']


def get_hello_message():
    name = input("Hello, What is your name? ")
    return input("Well, " + name.capitalize() + ", Welcome to Hangman!")

print(get_hello_message())

time.sleep(1)

def pick_difficulty():
    prompt = "Pick a difficulty, please. (Easy, Medium, Hard)\n>"
    choice = ""
    while choice not in ["easy", "medium", "hard"]:
        choice = input(prompt)
        choice = choice.lower()
    return choice

y = pick_difficulty()


def choose_word(choice):
    if choice == "easy":
        secretWord = random.choice(word_list)
    elif choice == "medium":
        secretWord1 = random.choice(word_list1)
    elif choice == "hard":
        secretWord2 = random.choice(word_list2)
    return secretWord

x = choose_word(y)
print(x)

def play(word, lives):
    blanks = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 7
    print("Let's play Hangman!")
    print(blanks)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ")
        if len(guess) == 1:
