import asyncio
import json
import random
from datetime import datetime, timedelta

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect, WebSocket

ranges = {
    1: [100, 250],
    2: [750, 3500],
    3: [80, 400],
    4: [500, 3000],
    5: [1200, 2400],
}

machine_ids = [1, 2, 3, 4, 5]
machines = [
    {
        "id": 1,
        "name": "Fridge",
        "producer": "Cool&Cold",
        "model": "BZF539/4",
        "serial": "794385762"
    },
    {
        "id": 2,
        "name": "AC",
        "producer": "Cool&Cold",
        "model": "A1215",
        "serial": "887-665-512378"
    },
    {
        "id": 3,
        "name": "TV",
        "producer": "TTCK",
        "model": "O75K-Y219",
        "serial": "O6-Y9-3218574"
    },
    {
        "id": 4,
        "name": "Vacuum Cleaner",
        "producer": "Professo",
        "model": "PV3R221",
        "serial": "438698"
    },
    {
        "id": 5,
        "name": "Dish Washer",
        "producer": "Professo",
        "model": "PD1R103",
        "serial": "1351681"
    },

]


def machines_endpoint(request: Request):
    return JSONResponse(machines)


def machine_detail_endpoint(request: Request):
    if request.path_params["mid"] not in machine_ids:
        return JSONResponse({"error": f"InvalidIDError: {request.path_params['mid']} is not valid"}, 404)
    else:
        return JSONResponse(machines[request.path_params["mid"] - 1])


async def consumption_endpoint(websocket: WebSocket):
    registered_ids = []

    def generate_messages():
        _messages = []
        for device in sorted(registered_ids):
            usage = random.randint(*ranges[device])
            _messages.append({"id": device, "usage": usage})
        return _messages

    await websocket.accept()
    next_message = datetime.now()
    try:
        while True:
            try:
                raw_data = await asyncio.wait_for(websocket.receive_text(), 0.01)
                data = json.loads(raw_data)
            except asyncio.TimeoutError:
                pass
            except json.JSONDecodeError as e:
                await websocket.send_json({"error": f"JSONDecodeError: {str(e)}"})
            else:
                if not isinstance(data, dict):
                    await websocket.send_json({"error": str(type(data))})
                elif "machine_id" not in data:
                    await websocket.send_json({"error": "KeyError: 'machine_id'"})
                elif data["machine_id"] in registered_ids:
                    await websocket.send_json(
                            {"error": f"DuplicateKeyError: {data['machine_id']} already registered"})
                elif data["machine_id"] not in machine_ids:
                    await websocket.send_json(
                            {"error": f"InvalidIDError: {data['machine_id']} is not valid"})
                else:
                    registered_ids.append(data["machine_id"])

            if datetime.now() > next_message:
                next_message += timedelta(seconds=1)
                messages = generate_messages()
                for message in messages:
                    await websocket.send_json(message)
    except WebSocketDisconnect:
        await websocket.close()

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

application = app = Starlette(debug=True, routes=[
    WebSocketRoute('/consumption/', consumption_endpoint),
    Route('/machines/', machines_endpoint),
    Route('/machines/{mid:int}/', machine_detail_endpoint),
], middleware=middleware)
