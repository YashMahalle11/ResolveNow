from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_admin
from app.schemas.auth_schema import AdminCreateRequest, AuthUserResponse
from app.services.auth_service import AuthService


router = APIRouter(prefix="/admins", tags=["Admins"])
auth_service = AuthService()


@router.post("", response_model=AuthUserResponse, status_code=status.HTTP_201_CREATED)
async def create_admin(
    payload: AdminCreateRequest,
    _: dict = Depends(get_current_admin),
) -> AuthUserResponse:
    try:
        return await auth_service.create_admin_by_admin(payload)
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while creating the admin account. Please try again.",
        )
