import asyncio, asyncpg, json

class DBQuery(object):
    def __new__(cls, rqst=None):
        if rqst == None:
            raise Exception('No defined function!')
            return None
        else:
            return object.__new__(cls)

    def __init__(self, rqst=None, jparm=None):
        self.rqst = rqst
        self.jparam = jparm

        __met = {
        'get_zone_statistic': self.get_zone_statistic,
        'set_statistic': self.set_statistic,
        'new_write_task': self.new_write_task,
        'get_pending_write_task': self.get_pending_write_task,
        'complete_write_task': self.complete_write_task,
        'get_telegram_subscribers': self.get_telegram_subscribers,
        'add_telegram_chat_id': self.add_telegram_chat_id,
        'check_telegram_user_rights': self.check_telegram_user_rights,
        'get_cam_group': self.get_cam_group,
        'get_short_camera_config': self.get_short_camera_config,
        'get_builder_params': self.get_builder_params,
        'get_camera_params': self.get_camera_params
        }

        if rqst not in __met:
            raise Exception('Undefined function!')



    def set_statistic(self):
        print('set_statistic')
        # pass

    def get_zone_statistic(self):
        print('get_zone_statistic')

    def new_write_task(self):
        print('new_write_task')

    def get_pending_write_task(self):
        print('get_pending_write_task')

    def complete_write_task(self):
        print('complete_write_task')

    def get_telegram_subscribers(self):
        print('get_telegram_subscribers')

    def add_telegram_chat_id(self):
        print('add_telegram_chat_id')

    def check_telegram_user_rights(self):
        print('check_telegram_user_rights')

    def get_cam_group(self):
        print('get_cam_group')

    def get_short_camera_config(self):
        print('get_short_camera_config')

    def get_builder_params(self):
        print('get_builder_params')

    def get_camera_params(self):
        print('get_camera_params')

    def __call__(self, *args, **kwargs):
        if not self.rqst:
            return self.retmess
        else:
            if self.rqst in self.met:
                self.met[self.rqst]()

            else:
                self.retmess = 'Undefined function!\nНеизвестная функция!'
                print(self.retmess)
                return self.retmess
        return

    def __str__(self):
        return self.retmess


    def __repr__(self):
        return self.retmess

try:
    q = DBQuery('get_camera_params')
except Exception as e:
    print(e)