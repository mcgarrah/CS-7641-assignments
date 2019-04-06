
### Simplified gridworld

 https://github.com/dennybritz/reinforcement-learning/blob/master/lib/envs/gridworld.py

 https://github.com/openai/gym/tree/master/gym/envs/toy_text

-

 https://github.com/aharutyu/gym-gridworlds

 https://github.com/maximecb/gym-minigrid

 https://github.com/maximecb/gym-minigrid/tree/master/gym_minigrid/envs

 https://github.com/lcswillems/torch-rl

-

 https://github.com/podondra/gym-gridworlds

 https://pypi.org/project/gym-gridworlds/

-

 https://github.com/yokian/gym-grid

 https://github.com/zuoxingdong/mazelab

### Simple grid-world environment compatible with OpenAI-gym
https://github.com/xinleipan/gym-gridworld

Some GridWorld environments for OpenAI Gym (q-learning)
https://github.com/opocaj92/GridWorldEnvs

Complex gridworlds

https://gym.openai.com/envs/#toy_text

A simple framework for experimenting with Reinforcement Learning in Python.
https://david-abel.github.io/simple_rl/

Q-Learning
https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

https://github.com/simoninithomas/reinforcement-learning-1

https://github.com/simoninithomas/reinforcement-learning-1/tree/master/1-grid-world

Interesting MDP PacMan Problem (but in Java)
https://github.com/kylewest520/CS-7641---Machine-Learning

Jython + BURLAP
https://github.com/danielcy715/CS7641-Machine-Learning/tree/master/Assignment4


Interesting but not practical

https://github.com/mkapnick/pacman

Attempt at fixing random seed issue

```
    if seed is None:
        seed = 0
        #seed = np.random.randint(0, (2 ** 32) - 1)
        # FIX: fix with casting did not work
        #seed = np.random.randint(0, (2 ** 32) - 1, dtype=np.int64)
        # FIX: tried different method and sys values
        #import sys
        #seed = np.random.randint(0, sys.maxsize)
        #seed = np.random.random_integers(0,sys.maxsize, dtype=np.int64)
        logger.info("Using seed {}".format(seed))
        np.random.seed(seed)
        rand.seed(seed)
```