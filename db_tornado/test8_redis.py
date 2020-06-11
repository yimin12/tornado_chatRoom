import uuid
import pickle

class Session(object):
    def __int__(self):
        self._sessionid = uuid.uuid4().hex
        self.cache={}

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key, default=None):
        return self.cache.get(key,default)
    def clear(self):
        self.cache.clear()
    @property
    def sessionid(self):
        return self._sessionid
    # 序列化session对象, 往数据库里面插数据需要序列化
    def serialization(self):
        return pickle.dumps(self)
    # 反序列化session对象
    @staticmethod
    def deserialization(str):
        return pickle.loads(str)

import redis
class SessionManager(object):
    # 建立redis数据库连接
    conn = redis.Redis(host='localhost',port=6379,db=0)

    @classmethod
    def cache2reids(cls,sessionobj):
        cls.conn.set(sessionobj.sessionid, sessionobj.serialization(), ex=14*24*60*60)

    @classmethod
    def getSessionObjBySid(cls,sessionid):
        sessionobj = Session.deserialization(cls.conn.get(sessionid)) if cls.conn.get(sessionid) else None
        if not sessionobj:
            sessionid = Session()
        return sessionobj
