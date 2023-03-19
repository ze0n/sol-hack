# fizzbuzz
# Built with Seahorse v0.2.4
#
# On-chain, persistent FizzBuzz!

from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('11111111111111111111111111111111')

class Status(Enum):
  PENDING = 0
  WON = 1
  FAILED = 2

class Goal(Account):
  winnerAddress: Pubkey
  fundAddress: Pubkey
  amount: f64
  status: Status
  externalGoalId: u128

MANAGER_WALLET:Pubkey = 'CgNcBAHD6tn2ynKDAsnnXAbHTWyuksY5LLh3dPebfrUm'

@instruction
def set_goal(amount:u64, manager:Manager, owner:Signer, goal:Empty[Goal]):  

  # assert owner.key() == calculator.owner, 'This is not your calculator!'
  
  manager = MANAGER_WALLET
  
  key = owner.key()
  
  goal = empty.init(
    payer = signer,
    seeds = ['Goal', signer], # one time
    #authority = signer
    owner = Pubkey.
  )

  goal.owner = owner.key()
  
  owner.lamports -= amount
  goal.lamports += amount

  goal.
  
  
  
  # user_token.init(payer = signer, seeds = ['Token', signer],mint = mint, authority = signer)   
  # user.balance-=manager.ticket_price
  # user.ticket_count+=1                       #increasing both user ticket count and total tickets count
  # manager.ticket_count+=1
  # if(manager.ticket_count==manager.winner_no):
  #   manager.winner_address=user.user_add
  
# @instruction
# def buy_tickets(user:User, manager:Manager, signer:Signer, user_token:Empty[TokenAccount], mint:TokenMint):  


# @instruction
# def buy_tickets(user:User, manager:Manager,signer:Signer, user_token:Empty[TokenAccount],mint:TokenMint):  
#   user_token.init(payer = signer, seeds = ['Token', signer],mint = mint, authority = signer)   
#   user.balance-=manager.ticket_price
#   user.ticket_count+=1                       #increasing both user ticket count and total tickets count
#   manager.ticket_count+=1
#   if(manager.ticket_count==manager.winner_no):
#     manager.winner_address=user.user_add


# @instruction
# def init(signer: Signer, data: Empty[Goal]):
#     init_data = data.init(
#         payer=signer,
#         seeds=[signer],
#         padding=1024
#     )

#     init_data.int_list = [1, 2]
#     init_data.int_list_2d = [[3, 4], [5, 6]]
#     init_data.string = 'Hello'
#     init_data.nested = Nested(7)
#     init_data.nested_list = [Nested(8), Nested(9)]
#     init_data.more_data = MoreData(10)


# @instruction
# def init(owner: Signer, fizzbuzz: Empty[FizzBuzz]):
#   fizzbuzz.init(payer = owner, seeds = ['fizzbuzz', owner])

# @instruction
# def do_fizzbuzz(fizzbuzz: FizzBuzz, n: u64):
#   fizzbuzz.fizz = n % 3 == 0
#   fizzbuzz.buzz = n % 5 == 0
#   if not fizzbuzz.fizz and not fizzbuzz.buzz:
#     fizzbuzz.n = n
#   else:
#     fizzbuzz.n = 0