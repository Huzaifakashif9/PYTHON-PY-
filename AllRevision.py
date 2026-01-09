hunger = 50
happiness = 50
energy = 50
action_history=[]
from datetime import datetime

def display_status():
  print('Pet Status')
  print(f'Hunger:::::{hunger}/100')
  print(f'Happiness:::::{happiness}/100')
  print(f'Energy:::::{energy}/100')

def log_actions(action):
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  action_history.append(f'[{timestamp}] {action}')

def feed_pet():
  global hunger, happiness
  hunger -= 20
  happiness += 5
  print('You fed your pet! Hunger decreased by 20')
  check_boundaries()
  log_actions("Fed the pet") 
  display_status()

def play_pet():
  global hunger, happiness, energy
  hunger += 10
  happiness += 20
  energy -= 15
  log_actions("Played with the pet")
  print('You played with your pet. Happiness increased by 20')
  check_boundaries()
  display_status()

def sleep_pet():
  global hunger, energy
  hunger += 5
  energy += 30
  log_actions("Pet slept")
  print('Your pet is sleeping! Energy increased by 30')
  check_boundaries()
  display_status()

def check_boundaries():
  global hunger, happiness, energy

  if hunger < 0:
    hunger = 0
  if hunger > 100:
    hunger = 100
  if happiness < 0:
    happiness = 0
  if happiness > 100:
    happiness = 100
  if energy < 0:
    energy = 0
  if energy > 100:
    energy = 100

def save_pet():
  try:
    with open('pets.txt','w')as f:
      f.write(str(hunger)+'\n')
      f.write(str(happiness)+'\n')
      f.write(str(energy)+'\n')
  except IOError as e:
        print('Error saving pet: {e}')

def load_pet():
  global hunger, happiness, energy
  try:
    with open('pets.txt', 'r') as f:
      lines = f.readlines()
      hunger = int(lines[0].strip())
      happiness = int(lines[1].strip())
      energy = int(lines[2].strip())
  except FileNotFoundError:
    pass
  except Exception as e:
    print('Error loading your pet', e)
print('Welcome to My Digital Pet Tracker!')
load_pet()
display_status()
while True:
  print('What would you like to do?')
  print('1. Feed Pet')
  print('2. Play with Pet')
  print('3. Put pet to sleep')
  print('4. view history')
  print('5. Exit')
  choice = input('>>>')
  if choice == '1':
    feed_pet()
  elif choice == '2':
    play_pet()
  elif choice == '3':
    sleep_pet()
  elif choice == '4':
    print('---Action History---')
    if not action_history:
      print('No action taken yet')
    else:
      for i in action_history:
        print(i)
  elif choice == '5':
    print('Saving pet data and exiting')
    save_pet()
    break
  else:
    print('Invalid choice. Please enter 1-5')