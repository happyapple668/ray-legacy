import logreg

import argparse
import orchpy as op
import orchpy.worker as worker

import arrays.dist as dist
import arrays.single as single

parser = argparse.ArgumentParser(description='Parse addresses for the worker to connect to.')
parser.add_argument("--scheduler-address", default="127.0.0.1:10001", type=str, help="the scheduler's address")
parser.add_argument("--objstore-address", default="127.0.0.1:20001", type=str, help="the objstore's address")
parser.add_argument("--worker-address", default="127.0.0.1:40001", type=str, help="the worker's address")

if __name__ == '__main__':
  args = parser.parse_args()
  op.connect(args.scheduler_address, args.objstore_address, args.worker_address)
  op.register_module(logreg)
  op.register_module(single)
  op.register_module(single.random)
  op.register_module(dist)
  worker.main_loop()
