import requests
import logging
from requests import Response
from configs.settings import base_url
from typing import Optional, Any
logger = logging.getLogger("SATPOL")

def api_request(
        method: str,
        endpoint: str,
        headers: Optional[dict[str, str]] = None,
        params: Optional[dict[str, Any]] = None, # Titik dua sudah dihapus
        data: Optional[dict[str, Any]] = None,
        json_data: Optional[dict[str, Any]] = None,
        files: Any = None
) -> Response:
    """Helper untuk membuat request API"""
    url = f'{base_url}{endpoint}'

    response = requests.request(
        method=method,
        url=url,
        headers=headers or {},
        params=params or {},
        data=data,
        json=json_data, # Tambah koma
        files=files,    # Tambah koma
        timeout=3
    )
    return response

def method_get(endpoint: str, headers: Optional[dict[str, str]] = None, params: Optional[dict[str, Any]] = None) -> Response:
    return api_request('GET', endpoint=endpoint, headers=headers, params=params)

def method_post(endpoint: str,
                json_data: Optional[dict[str, Any]] = None,
                data: Optional[dict[str, Any]] = None,
                files: Optional[dict[str, Any]] = None,
                headers: Optional[dict[str, str]] = None
                ) -> Response:
    logger.info(f'START POST {endpoint.upper()} ENDPOINT ')
    return api_request('POST', endpoint, headers=headers, json_data=json_data, data=data, files=files)

def method_put(endpoint: str, headers: Optional[dict[str, str]] = None, json_data: Optional[dict[str, Any]] = None) -> Response:
    return api_request('PUT', endpoint, headers=headers, json_data=json_data)

def method_patch(endpoint: str, headers: Optional[dict[str, str]] = None, json_data: Optional[dict[str, Any]] = None) -> Response:
    return api_request('PATCH', endpoint, headers=headers, json_data=json_data)

def method_delete(endpoint: str, headers: Optional[dict[str, str]] = None, json_data: Optional[dict[str, Any]] = None ) -> Response:
    return api_request('DELETE', endpoint, headers=headers, json_data=json_data)
