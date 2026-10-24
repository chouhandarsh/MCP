import random
from fastmcp import FastMCP
mcp = FastMCP(name="Demo Server")
@mcp.tool
def roll_dice(n_diece:int=1):
    "Roll n dice and re"
    return [random.randint(1,6) for _ in range(n_diece)]
@mcp.tool
def add_number(a:float,b:float):
    return a+b
if __name__=="__main__":
    mcp.run()
