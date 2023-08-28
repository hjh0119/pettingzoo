# export PYTHONPATH="/home/lab304/PettingZoo:$PYTHONPATH"
import sys
print(sys.path)
import simple_tag_v3

env = simple_tag_v3.parallel_env(max_cycles=25,render_mode='human')
env.reset()
for i in range(5000):
    if i % 300 == 0:
        env.reset()
    env.render()