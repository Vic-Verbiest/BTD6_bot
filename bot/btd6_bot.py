import btd6_lib
import data
import time

import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense , Input
from keras.optimizers import Adam
from collections import deque

import gym
from gym import spaces

class DQN:
    def __init__(self, state_size, action_size):
        self.state_size = state_size # aantal inputs
        self.action_size = action_size # aantal outputs
        self.memory = deque(maxlen=5000) # memory om keuzes te bepalen
        self.gamma = 0.8  # 1-rekening houden met toekomst 0-geen rekening houden met toekomst
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01 # laagst mogelijke exploration rate
        self.epsilon_decay = 0.995 # vermindering van exploration rate
        self.learning_rate = 0.001 # hoe snel dat het model moet leren (kan noch worden aangepast)
        self.model = self._build_model() # model bouwen

    def _build_model(self):
        model = Sequential()
        model.add(Input(shape=(3,)))
        model.add(Dense(25, activation='relu')) # first hidden layer + inputs
        model.add(Dense(20, activation='relu')) # second hidden layer
        model.add(Dense(15, activation='relu')) # third hidden layer
        model.add(Dense(self.action_size, activation='softmax')) # output layer
        model.compile(loss='mse', optimizer=Adam (learning_rate=self.learning_rate)) #compiling model
        return model

    def remember(self, state, action0, action1, action2, action3, action4, action5, reward, next_state, done):
        self.memory.append((self, state, action0, action1, action2, action3, action4, action5, reward, next_state, done)) # saving data in memory

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            rand = 1
        else:
            rand = 0
        return rand, self.model.predict(state) # best action
    
    
    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for experience in minibatch:
            _, state, action0, action1, action2, action3, action4, action5, reward, next_state, done = experience
            actions = [action0, action1, action2, action3, action4, action5]
            print(actions)
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            for action in actions:
                target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    
class env(gym.Env):
    def __init__(self):
        self.prices = data.get_prices()
        self.lives = 100
        self.money = 650
        self.round = 3
        self.monkeys = btd6_lib.monkeys
        self.map = data.get_map()
        
        self.action_space = spaces.Discrete(51)
        self.observation_space = spaces.Box(low=0, high=5000, shape=(6,))

        self.state = None
        self.stepps_beyond_done = None
    
    def step(self,action, rand):
        
        todo = 0
        #place of upgrade
        if rand == 0:
            if action[0] > action[1] and action[0] > action[2]:
                todo = 0
            elif action[1] > action[0] and action[1] > action[2]:
                todo = 1
            elif action[2] > action[0] and action[2] > action[1]:
                todo = 2
        else:
            todo = random.randint(0,2)

        if todo == 0: print("nothing")
        if todo == 1: print("place")
        if todo == 2: print("upgrade")
        

        upgrade = 0
        #welke upgrade
        if rand == 0:
            if action[3] > action[4] and action[3] > action[5]:
                upgrade = 1
            elif action[4] > action[3] and action[4] > action[5]:
                upgrade = 2
            elif action[5] > action[3] and action[5] > action[4]:
                upgrade = 3
        else:
            upgrade = random.randint(1,3)
        
        #welke monkey upgraden
        if rand == 0:
            index_range_start = 6
            index_range_end = 6 + 20
            filtered_action = action[index_range_start:index_range_end]
            if(len(btd6_lib.monkeys) == 0):
                monkey_upgrade = -1
            else:
                monkey_upgrade= np.argmax(filtered_action) + index_range_start - 1
        else:
            if len(btd6_lib.monkeys) == 0:
                monkey_upgrade = -1
            else:
                monkey_upgrade = random.randint(0,len(btd6_lib.monkeys)-1)

        if monkey_upgrade == -1:
            todo = 1

        else:
            if monkey_upgrade < len(self.monkeys):
                print(data.get_price_upgrade(btd6_lib.monkeys[monkey_upgrade].name, upgrade , btd6_lib.monkeys[monkey_upgrade].upgrades[upgrade-1]+1))
                print(btd6_lib.monkeys[monkey_upgrade].name)
                if btd6_lib.monkeys[monkey_upgrade].name == 0:
                    todo = 1
                else:
                    if self.money < data.get_price_upgrade(btd6_lib.monkeys[monkey_upgrade].name, upgrade , btd6_lib.monkeys[monkey_upgrade].upgrades[upgrade-1]+1):
                        if todo == 2:
                            todo = 0

        #welke monkey plaatsen
        if rand == 0:
            index_range_start = 26
            index_range_end = 24 + 26
            filtered_action = action[index_range_start:index_range_end]
            monkey_place = np.argmax(filtered_action)
            if monkey_place == -1:
                monkey_place = 1
        else:
            monkey_place = random.randint(0,22)
        if self.money < data.get_price_place(monkey_place):
            if todo == 1:
                todo = 0
        if monkey_place == 8 or monkey_place == 9:
            print ("boat or sub")
            todo = 0
            

        #x en y van monkey
        if rand == 0:
            index_range_start = 50
            index_range_end = 50 + 13
            filtered_action = action[index_range_start:index_range_end]
            x_pos = np.argmax(filtered_action) + index_range_start-1
            x = data.get_x(x_pos-49)
        else:
            x_pos = random.randint(0,12)
            x = data.get_x(x_pos)



        if rand == 0:
            index_range_start = 63
            index_range_end = 63 + 9
            filtered_action = action[index_range_start:index_range_end]
            y_pos = np.argmax(filtered_action) + index_range_start-1
            y = data.get_y(y_pos-62)
        else:
            y_pos = random.randint(0,8)
            y = data.get_y(random.randint(0,8))

        posible = btd6_lib.check_place(x, y)
        if posible == False:
            todo = 0


        if todo == 0:
            print("did nothing")
        if todo == 1:
            btd6_lib.place_monkey(monkey_place+1, x, y)
        if todo == 2:
            btd6_lib.upgrade_monkey(monkey_upgrade, upgrade)

        
            

        # update the envirement with the new data
        
        screen_data = data.extract_screen_data()

        try:
            previous_lives = self.lives
            self.lifes = int(screen_data[1])
            print("lives: ", self.lives)
        except:
            print("error lives")
        try:
            self.money = int(screen_data[0])
            print("money: ", self.money)
        except:
            print("error money")
        try:
            previous_round = self.round
            self.round = int(screen_data[2])
            print("round: ", self.round)
        except:
            print("error round")
        
        self.monkeys = btd6_lib.monkeys
        next_state = [[self.money, self.lives, self.round]]

        done = False
        
        #check the termination
        if screen_data[3]==0:
            done = True
        print("done: ", done)
        #reward calculation
        if done:
            reward = -10000
        else:
            reward = 0
            reward = reward - (previous_lives - self.lives) * 1000
            reward = reward + self.money * 1
            reward = reward + (previous_round - self.round) * 3000


        #return the new state reward and termination flag
        true_action = [todo,monkey_upgrade,upgrade,monkey_place,x_pos,y_pos]
        if todo == 0:
            true_action = [-1,-1,-1,-1,-1,-1]
        if todo == 1:
            true_action = [1,-1,-1,monkey_place,x_pos,y_pos]
        if todo == 2:
            true_action = [2,monkey_upgrade,upgrade,-1,-1,-1]

        return np.array(next_state), reward, done, true_action
    
    def reset(self):
        btd6_lib.monkeys = []
        self.state = [[self.money, self.lives, self.round]]
        self.steps_beyond_done = None
        return np.array(self.state)
        



#Define the environment, state size, and action size
state_size = 3
action_size = 71
# Create DQN agent
agent = DQN(state_size, action_size)
envirement = env()

# Training loop
batch_size = 32
EPISODES = 1000
for episode in range(EPISODES):
    btd6_lib.start_game()
    state = envirement.reset()
    state = np.reshape(state, [1, 3])
    for time in range(500):  # Adjust the maximum number of steps per episode
        #env.render()  # Uncomment this if you want to visualize the environment
        rand,action = agent.act(state)
        next_state, reward, done, action = env.step(envirement,action.flatten(), rand)
        reward = reward
        next_state = np.reshape(next_state, [1, 3])
        agent.remember(state, action[0], action[1], action[2], action[3], action[4], action[5],reward, next_state, done)
        state = next_state
        if done:
            print("episode: {}/{}, score: {}, e: {:.2}".format(episode, EPISODES, time, agent.epsilon))
            btd6_lib.restart_game()
            break
    if len(agent.memory) > batch_size:
        agent.replay(batch_size)