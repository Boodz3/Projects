import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal
from pyke import ask_tty
# Create a Pyke engine

def run():

    engine = knowledge_engine.engine(__file__)
    engine.reset()
    engine.activate('rules')
    print ("doing proof")
    jobs = []
    try :
        with engine.prove_goal('facts.QualifiedForJob($job)') as gen:
            for vars,plan in gen:
                jobs.append(vars['job'])
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    print ()
    print ("done")
    # write results to file
    with open('results.txt', 'w') as f:
        for job in jobs:
            f.write(job + '\n')

run()