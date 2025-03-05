import uuid 
import pytest

from externalLayer.repositories.auction_repo import in_memory_repository
from infrastructure.repositories.auction_repository import AuctionRepository
from test.utils import create_bid
from usecase.exceptions import AuctionNotFoundError
from usecase.submit_bid_usecase import SubmitBidUseCase

@pytest.fixture
def auctions_repository() -> AuctionRepository:
    return in_memory_repository()

@pytest.fixture
def submit_bid_use_case(auctions_repository: AuctionRepository)-> SubmitBidUseCase:
    return SubmitBidUseCase(auctions_repository)

async def test_auction_not_found(submit_bid_use_case:SubmitBidUseCase):
    bid = create_bid(auction_id=uuid.uuid4)
    with pytest.raises(AuctionNotFoundError):
        await submit_bid_use_case(bid)