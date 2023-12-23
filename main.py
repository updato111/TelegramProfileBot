from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
import time
from telethon import functions , types
from utils import generate_image, delete_image, get_current_time
import config
import cute_numbers
from telethon.sessions import StringSession



#with TelegramClient(StringSession(), config.api_id, config.api_hash) as client:
#    print(client.session.save())


string = 'BAF39SsAh1NI60jY7oJqaHK7bnSB9n_UyWUifw7qvRaf_tbPqVVL64geaNOYfmnNz_nUxo1c9OOgsy9Sl11kAdydt2uUkyUNxLdlMlc9xioi7i9YObgoX-b8OxugDpzJaydZ9MGdB-qf7qk5gHddpIZc4vLeLS0NplPR2U65fIzyhCm9oHJvi75fH7AClwIVLaZr7TLQ_kk071HULWQEC0KHHkiodSoD_0DmadE0jR8aPMqgvtRmB-CJLEuc5EX9aqb7q-QnkaPsF0IhPVSKPz7j4uYgdJAxD3pAitx6n4_qAv-ho4DLwnmLkTzh119O4FYzcrTRQAduCaP6Jd8NyNXs2H_d3QAAAAFTuY5kAA'
client = TelegramClient(StringSession(string), config.api_id, config.api_hash)
client.start()


def main():
    previous_time = ''
    while True:
        if not previous_time == get_current_time():
            current_time = get_current_time()
            previous_time = current_time
            generate_image(current_time)
            #github.com/0x1381
            image = client.upload_file(config.image_filename)
            client(UploadProfilePhotoRequest(image))
            client(DeletePhotosRequest([client.get_profile_photos('me')[-1]]))
            delete_image()
            time.sleep(1)



if __name__ == '__main__':
    main()
