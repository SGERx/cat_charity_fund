from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_project_exists, check_info_none,
    check_name_duplicate, check_update_project_closed,
    check_update_project_invested, check_charity_project_before_delete
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charityproject import charity_project_crud
from app.schemas.charityproject import (
    CharityProjectCreate, CharityProjectDB, CharityProjectUpdate
)
from app.services.donation import func_donation


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_info_none(charity_project.name, session)
    await check_info_none(charity_project.description, session)
    await check_name_duplicate(charity_project.name, session)
    cat_project = await charity_project_crud.create(charity_project, session)
    cat_project = await func_donation(session, cat_project)
    return cat_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_charity_project_all(
    session: AsyncSession = Depends(get_async_session),
):
    project_all = await charity_project_crud.get_multi(session)
    return project_all


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    project_id: int,
    project_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    cat_charity_project = await check_charity_project_exists(
        project_id, session
    )
    if project_in.name is not None:
        await check_name_duplicate(project_in.name, session)
    await check_update_project_closed(project_id, session)
    await check_update_project_invested(
        cat_charity_project, project_in.full_amount
    )
    cat_charity_project = await charity_project_crud.update(
        cat_charity_project, project_in, session
    )
    return cat_charity_project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    cat_charity_project = await check_charity_project_before_delete(
        project_id=project_id,
        session=session
    )
    cat_charity_project = await check_charity_project_exists(
        project_id, session
    )
    cat_charity_project = await charity_project_crud.remove(
        cat_charity_project, session
    )
    return cat_charity_project
