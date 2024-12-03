# main.py
import utils
from minimax_with_pruning import fn

def change_depth():
    utils.MAX_DEPTH = 7
    print(f"MAX_DEPTH changed to: {utils.MAX_DEPTH}")

print(f"Original MAX_DEPTH: {utils.MAX_DEPTH}")
change_depth()
print(f"Updated MAX_DEPTH: {utils.MAX_DEPTH}")
fn()
