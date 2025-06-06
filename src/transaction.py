from dataclasses import dataclass
 
@dataclass
class Transaction:
    date: str
    amount: int
    balance: int 