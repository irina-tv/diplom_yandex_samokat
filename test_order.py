# Ирина Твердикова, 22-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from sendor_stand_request import create_order, get_order
# Автотест
def test_order_creation_and_retrieval():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
