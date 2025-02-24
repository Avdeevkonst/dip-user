import httpx
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

services = {
    "service1": "https://0.0.0.0:8001",
    "service2": "https://0.0.0.0:8002",
    # Add more services if needed
}

gate = APIRouter()


async def forward_request(service_url: str, method: str, path: str, body=None, headers=None):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}{path}"
        response = await client.request(method, url, json=body, headers=headers)
        return response


@gate.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def gateway(service: str, path: str, request: Request):
    if service not in services:
        raise HTTPException(status_code=404, detail="Service not found")

    service_url = services[service]
    body = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    headers = dict(request.headers)

    response = await forward_request(service_url, request.method, f"/{path}", body, headers)

    return JSONResponse(status_code=response.status_code, content=response.json())
