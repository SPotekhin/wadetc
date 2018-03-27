# Database queries

`set_statistic`

Запись статистики за прошедший период

Request:

```python
    DatabaseQuery('set_statistic', {
        'end': '2018-02-28_12:00:00',  # конец периода
        'usdk_id': 1,
        'stats': {  # статистика по зонам, id зон - строка
            '1': 10,
            '2': 20,
        }
    })
```

Response:

```python
    DatabaseResponse(True, {})
```

`get_zone_statistic`

Получить статистику по зоне за выбранный период

Request:

```python
    DatabaseQuery('get_zone_statistics', {
                        'usdk_id': 10,
                        'zone_id': 1,
                        'start': '2018-02-28_10-00-00',
                        'end': '2018-02-28_12-00-00',
                    })
```

Response:

```python
    DatabaseResponse(True, {
        '2018-02-28_10-00-00': 10,
        '2018-02-28_10-05-00': 12,
        '2018-02-28_10-10-00': 9,
        ...
        '2018-02-28_11-55-00': 11,
    })

```

`new_write_task`

Новая запись

Request:

```python
    DatabaseQuery("new_write_task", {
                "camera_id": 1,
                "duration": 300,
                "at": '2018-02-28_15-00-00'
            })
```

Response:

```python
    DatabaseResponse(True, {
        'task_id': 1
    })
```

`get_pending_write_tasks`

Получить все незаконченные задания записи

Request:

```python
    DatabaseQuery('get_pending_write_task', {})
```

Response:

```python
    DatabaseResponse(True, {
        'tasks': [
            {
                'camera_id': 1,
                'duration': 300,
                'at': '2018-02-28_15-00-00',
                'task_id': 1,
            },
            ...
        ],
    })
```

`complete_write_task`

Сигнализирует о том, что запись успешно завершена

Request:

```python
    DatabaseQuery('complete_write_task', {
        'task_id': 1
    })
```

Response:

```python
    DatabaseResponse(True, {})
```

`get_telegram_subscribers`

Получение chat_id зарегистрированных в telegram пользователей для отправки сообщений

Request:

```python
    DatabaseQuery('get_telegram_subscribers', {})
```

Response:

```python
    DatabaseResponse(True, {
        'users': [12345, 12344, 12333]
    })
```

`add_telegram_chat_id`

Добавление нового пользователя в telegram, отправляется при получении ботом команды `/start`

Request:

```python
    DatabaseQuery('add_telegram_chat_id', {
        'username': 'user',
        'chat_id': 12345,
    })
```

Response:

```python
    DatabaseResponse(True, {})
```

`check_telegram_user_rights`

Проверка прав пользователя в telegram

Request:

```python
    DatabaseQuery('check_telegram_user_rights', {
        'username': 'user',
    })
```

Response:

```python
    DatabaseResponse(True, {'ok': True})
```

`get_cam_groups`

Request:

Получение группировки камер по перекресткам

```python
    DatabaseQuery('get_cam_groups', {})
```

Response:

```python
    DatabaseResponse(True, {'groups': [
                    {
                        'group_id': 1,
                        'description': "Group #1",
                        'cams': [
                            {
                                'id': 100001,
                                'description': "Camera #100001",
                            }
                        ],
                    },
                    {
                        'group_id': 2,
                        'description': "Group #2",
                        'cams': [
                            {
                                'id': 100002,
                                'description': "Camera #100002",
                            }
                        ],
                    },
                ]})
```

`get_short_camera_config`

Получение конфигурации камеры без параметров зон, только координаты
*Не знаю, стоит ли делать отдельный запрос для этого*

Request:

```python
    DatabaseQuery('get_short_camera_config', {
        'camera_id': 123,
    })
```

Response:

```python
    DatabaseResponse(True, {
                    'stream': 'rtsp://admin:admin@192.168.32.166/av0_1',
                    'coordinates': {
                        '1': {
                          'type': 'count',
                          'points': [[50, 50], [50, 100], [100, 50], [100, 100]],
                        },
                        '101': {
                            'type': 'mgr',
                            'points': [[200, 200], [250, 200], [200, 250], [250, 250]],
                        }
                    },
                })
```

`get_builder_params`
Получение параметров соединения и отпрваки сообщений на УСДК

Request:

```python
    DatabaseQuery('get_builder_params', {
        'usdk_id': 1,
        'type': "count"  # or "mgr"
    })
```

Response:

```python
    DatabaseResponse(True, {
        'interval': 300,  # interval between ticks
        'zones': [1, 2, 3, 4, 5],  # array of zone_ids
        'usdk_ip': '127.0.0.1:1092',  # string address of usdk
    })
```

`get_camera_params`
Получение параметров камеры и зон

Request:

```python
    DatabaseQuery('get_camera_params', {
        'usdk_id': 1,
        'camera_id': 1,
    })
```

Response:

```python
    DatabaseResponse(True, {
        'stream': 'rtsp://admin:admin@192.168.32.166/av0_1',
        'noise': 2.0,
        'count': {
            '3': {
                'points': [[10, 10], [20, 10], [10, 20], [20, 20]],
                'crop': 4.0,
                'direction': 230.0,
                'threshold': 10,
                # additional params
            },
        },
        'mgr': {
            '103': {
                'points': [[10, 10], [20, 10], [10, 20], [20, 20]],
                'crop': 4.0,
                'direction': 0,
                # additional params
            }
        }
    })
```