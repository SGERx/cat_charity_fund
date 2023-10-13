from fastapi import APIRouter

from app.api.endpoints import charity_router, donation_router, user_router


main_router_v1 = APIRouter()
main_router_v1.include_router(charity_router, prefix='/charity_project', tags=['Charity Project'])
main_router_v1.include_router(donation_router, prefix='/donation', tags=['Donation'])
main_router_v1.include_router(user_router)