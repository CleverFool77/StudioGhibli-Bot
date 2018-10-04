import zulip
import pprint
from ss import sg

pp = pprint.PrettyPrinter(indent=4)


class Bot():
    def __init__(self):
        self.client = zulip.Client(config_file="~/.zuliprcc")
        self.subscribe()
        print("subscribed")

    def subscribe(self):
        stream_data = self.client.get_streams().get("streams")
        temp_dict = {}
        stream_list = []
        for data in stream_data:
            temp_dict["name"] = data.get("name")
            stream_list.append(temp_dict)

        result = self.client.add_subscriptions(stream_list)
        # pp.pprint(r)
        pp.pprint(stream_data)

    def process(self, msg):
        word = msg.get('content').lower().split(" ")
        # s = "Invalid command"
        words = ' '.join(word[1:])

        send_dict = {
            "type": "stream",
            "to": msg.get("display_recipient"),
            "subject": msg.get("subject"),
            "content": "Invalid command"   # <--- ismei doubt hai
        }

        if sg(words) == "Not Found": 
            result = self.client.send_message(send_dict)
        else:
            send_dict["content"] = sg(words)
            result = self.client.send_message(send_dict)
            pp.pprint(result)
            

        return


def main():
    bot = Bot()
    print("listening")
    bot.client.call_on_each_message(bot.process)


main()
