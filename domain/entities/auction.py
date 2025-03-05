from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from domain.entities.bid import Bid
from domain.entities.item import Item
from domain.value_object.price import Price

@dataclass
class Auction:
    item: Item
    seller_id: UUID
    start_date: date
    end_date: date
    start_Price: Price
    bids: list[Bid] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)

    @property
    def is_active(self) -> bool:
        return self.start_date <=date.today() <= self.end_date
    
    @property
    def minimal_bid_price(self) -> Price:
        return max(
            [bid.price for bid in self.bid] + [self.start_date],key=lambda x: x.value
        )
