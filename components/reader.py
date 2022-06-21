from datetime import datetime

from mysql import connector

from components.logger import Logger
from models.collection_description import CollectionDescription
from models.receiver_property import ReceiverProperty


class Reader:
    def __init__(self, processable_dataset):
        self.processable_dataset = processable_dataset

    def SaveData(self, data: CollectionDescription):  # pragma: no cover
        for value in data.historical_collection:
            if value.code == 'CODE_DIGITAL':
                self.SaveValue(value)
            else:
                last_value = self.ReadLastValue(value.code)
                if last_value is None:
                    self.SaveValue(value)
                elif abs(value.receiver_value - last_value) > (last_value * 0.02):
                    self.SaveValue(value)

    def ReadLastValue(self, code):
        try:
            conn = connector.connect(host='localhost', user='student', passwd='password', database='mysql')
            curr = conn.cursor()
            curr.execute("""select value
                             from dataset_%s
                             where code = %s
                             and time_saved = (select max(time_saved) from dataset_%s)""",
                         (self.processable_dataset, code, self.processable_dataset))
            value = curr.fetchone()[0]
            curr.close()
            conn.close()
            return value
        except:
            Logger.LogAction(
                f"[Error]: Failed to read last value for {code}")
            return None

    def SaveValue(self, data: ReceiverProperty):
        try:
            conn = connector.connect(host='localhost', user='student', passwd='password', database='mysql')
            curr = conn.cursor()
            curr.execute("""insert into dataset_%s values(%s, %s, timestamp(%s, %s))""",
                         (self.processable_dataset,
                          data.code.name,
                          int(data.receiver_value),
                          datetime.now().strftime('%Y-%m-%d'),
                          datetime.now().strftime('%H:%M:%S')))
            curr.execute('commit')
            curr.close()
            conn.close()
            Logger.LogAction(
                f"[{self.__str__()}]: Saved -> {data.code.name}\t{int(data.receiver_value)}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        except:
            Logger.LogAction(
                f"[Error]: Failed to save value for {data.code}")
            return False

    def GetValuesByInterval(self,
                            code: str,
                            start_interval_date: str,
                            start_interval_time: str,
                            end_interval_date: str,
                            end_interval_time: str):
        try:
            conn = connector.connect(host='localhost', user='student', passwd='password', database='mysql')
            curr = conn.cursor()
            curr.execute(f"""select value
                             from dataset_%s
                             where code = %s
                             and time_saved > timestamp(%s,  %s)
                             and time_saved < timestamp(%s,  %s)""",
                         (
                             self.processable_dataset,
                             code,
                             start_interval_date,
                             start_interval_time,
                             end_interval_date,
                             end_interval_time
                         ))
            values = curr.fetchall()
            curr.close()
            conn.close()
            if values is None:
                return []

            actual_values = []
            for value in values:
                actual_values.append(value[0])
            return actual_values
        except:
            Logger.LogAction(
                f"[Error]: Failed get data for {code} in interval {start_interval_date} {start_interval_time} - {end_interval_date} {end_interval_time}")
            return None

    def __str__(self):  # pragma: no cover
        return f'Reader {self.processable_dataset}'
